import logging
import signal
import time
from typing import Any

import config
from code_executor import SubprocessExecutor
from consumer import BatchConsumer
from imap_consumer import IMAPConsumer
from mailer import Mailer
from message_processor_instant import InstantMessageProcessor

SLEEP_AFTER_ERROR = 5
SLEEP_AFTER_EMPTY_BATCH = 5

log_format = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format)

log = logging.getLogger(__name__)


class App:
    def __init__(self, batch_consumer: BatchConsumer) -> None:
        self.is_running = True
        self.consumer = batch_consumer

    def setup_signal_handlers(self) -> None:
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def shutdown(self, *args: Any) -> None:
        log.info("Shutting down batch consumer gracefully.")
        self.is_running = False

    def run(self) -> None:
        self.setup_signal_handlers()

        log.info("Starting batch consumer.")
        while self.is_running:
            try:
                with self.consumer:
                    remaining_cnt = self.consumer.process_one_batch(
                        max_size=config.IMAP_BATCH_SIZE
                    )
                    if remaining_cnt == 0:
                        self.sleep(SLEEP_AFTER_EMPTY_BATCH, "folder is empty")
            except Exception:
                log.exception("Exception during processing.")
                self.sleep(SLEEP_AFTER_ERROR, "before next attempt")

        log.info("Batch consumer finished.")

    def sleep(self, seconds: int, reason: str) -> None:
        if not self.is_running:
            return
        log.info(f"Sleeping %ss %s.", seconds, reason)
        time.sleep(seconds)


if __name__ == "__main__":
    processor = InstantMessageProcessor(
        email_sender=Mailer(), code_executor=SubprocessExecutor()
    )
    batch_consumer = IMAPConsumer(message_processor=processor)
    App(batch_consumer).run()
