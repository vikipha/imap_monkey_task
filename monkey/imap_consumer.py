import imaplib
import logging
from functools import wraps
from typing import Any, Callable, cast

import config
from consumer import BatchConsumer
from message_processor import MessageProcessor

INCOMING_EMAIL_CONTAINS = "viktor.lacina"

log = logging.getLogger(__name__)


class ConsumerException(Exception):
    pass


class MessageProcessingException(ConsumerException):
    pass


class IMAPOperationException(ConsumerException):
    pass


def wrap_uncaught_exceptions(error_message: str) -> Callable:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                return f(*args, **kwargs)
            except ConsumerException:
                raise
            except Exception as e:
                raise IMAPOperationException(error_message) from e

        return inner

    return decorator


class IMAPConsumer(BatchConsumer):
    def __init__(self, message_processor: MessageProcessor) -> None:
        self.message_processor = message_processor
        self._imap: imaplib.IMAP4_SSL | None = None

    @property
    def imap(self) -> imaplib.IMAP4_SSL:
        if not self._imap:
            raise IMAPOperationException("Preconditions not met.")
        return self._imap

    @wrap_uncaught_exceptions("Error while processing batch.")
    def process_one_batch(self, max_size: int = 10) -> int:
        """
        Process at most `max_size` of messages from folder and return nuber of messages left.
        """
        if not (message_ids := self._get_next_message_ids()):
            return 0

        log.info("Inbox contains %s new messages.", len(message_ids))

        cnt = 0
        for message_id in message_ids[:max_size]:
            try:
                self._process_message(message_id)
                cnt += 1
            except ConsumerException:
                log.exception("Error while processing message %s", message_id)

        log.info("Successfully processed %s messages", cnt)

        remaining_in_queue = len(message_ids) - max_size
        return max(remaining_in_queue, 0)

    @wrap_uncaught_exceptions("Connection initialization failed.")
    def __enter__(self) -> BatchConsumer:
        self._imap = imaplib.IMAP4_SSL(config.IMAP_HOST)
        res, data = self.imap.login(config.MAIL_USER, config.MAIL_PASS)
        if res != "OK":
            raise IMAPOperationException(f"Login failed, error: {data}")
        res_select, data_select = self.imap.select(config.IMAP_FOLDER)
        if res_select != "OK":
            raise IMAPOperationException(
                f"Selection of folder failed, error: {data_select}"
            )
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        try:
            res, data = self.imap.close()
            if res != "OK":
                log.error("Error while closing IMAP connection: %s", data)
        except Exception:
            log.exception("Error while closing IMAP connection.")
        try:
            self.imap.logout()
        except Exception:
            log.exception("Error while IMAP logout.")

    def _process_message(self, message_id: str):
        message_body = self._fetch_message(message_id)
        try:
            res = self.message_processor.process_message(message_id, message_body)
        except Exception as e:
            raise MessageProcessingException(
                f"Processing of message {message_id} failed."
            ) from e

        if res:
            self._mark_message_as_processed(message_id)
            log.info("Message %s marked as processed.", message_id)
        else:
            raise MessageProcessingException(
                f"Processing of message {message_id} failed."
            )

    @wrap_uncaught_exceptions("Search failed.")
    def _get_next_message_ids(self) -> list[str]:
        res, data = self.imap.search(
            None, f'(FROM "{config.INCOMING_EMAIL_PATTERN}" UNFLAGGED)'
        )
        if res != "OK":
            raise IMAPOperationException(f"Search failed, error: {data}")

        return [x.decode() for x in data[0].split()]

    @wrap_uncaught_exceptions("Fetch failed.")
    def _fetch_message(self, message_id: str) -> bytes:
        res, data = self.imap.fetch(message_id, "(RFC822)")
        if res == "OK" and data:
            return cast(list[tuple[bytes, bytes]], data)[0][1]

        raise IMAPOperationException(f"Fetch failed, error: {data}")

    @wrap_uncaught_exceptions("Set flag failed.")
    def _mark_message_as_processed(self, message_id: str) -> None:
        res, data = self.imap.store(message_id, "+FLAGS", "\\Flagged")
        if res != "OK":
            raise IMAPOperationException(f"Set flag failed, error: {data}")
