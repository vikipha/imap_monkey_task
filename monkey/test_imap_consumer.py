import logging
from unittest import mock

from _pytest.logging import LogCaptureFixture
from imap_consumer import ConsumerException, IMAPConsumer
from message_processor import MessageProcessor

# OK, this module (imap_consumer.py) is full of imaplib calls, so it would
# require a lot of mocking or testing against some imap server. For demonstration purposes,
# I'm adding a test for one of the methods.


def test_mark_message_as_processed() -> None:
    consumer = IMAPConsumer(MessageProcessor())
    with mock.patch.object(consumer, "_imap") as imap_:
        imap_.store.return_value = ("OK", [b"yay!"])

        consumer._mark_message_as_processed(b"1")

        assert len(imap_.method_calls) == 1
        assert imap_.method_calls[0].args == (b"1", "+FLAGS", "\\Flagged")


def test_process_one_batch(caplog: LogCaptureFixture) -> None:
    consumer = IMAPConsumer(MessageProcessor())
    with (
        mock.patch.object(consumer, "_get_next_message_ids") as get_ids,
        mock.patch.object(consumer, "_process_message") as process_message,
    ):
        # remaining after one batch is 0
        get_ids.return_value = ["1"]
        assert consumer.process_one_batch() == 0

        # remaining after batch is 20 - 10
        get_ids.return_value = [str(x) for x in range(20)]
        assert consumer.process_one_batch(max_size=10) == 10

        # An exception during the processing of single message doesn't break batch.
        get_ids.return_value = ["1"]
        process_message.side_effect = ConsumerException("It went wrong.")
        with caplog.at_level(logging.ERROR):
            assert consumer.process_one_batch() == 0
            assert "Error while processing message" in caplog.text
