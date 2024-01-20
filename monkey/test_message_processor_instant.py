from typing import cast
from unittest import mock
from unittest.mock import Mock

import message_samples
import pytest
from code_executor import CodeExecutor
from mailer import Mailer
from message_analyzer import MessageAnalyzer
from message_processor_instant import InstantMessageProcessor

SOME_ID = "1"


@pytest.fixture()
def email_sender() -> Mock:
    return Mock()


@pytest.fixture()
def code_executor() -> Mock:
    executor = Mock()
    executor.execute_code.return_value = "OK"
    return executor


class MessageMock:
    def __init__(self) -> None:
        self.subject = "Test subject"
        self.sender = "a@a.aa"


@pytest.fixture()
def message_analyzer() -> MessageMock:
    return MessageMock()


@pytest.fixture()
def processor(
    email_sender: Mailer, code_executor: CodeExecutor
) -> InstantMessageProcessor:
    return InstantMessageProcessor(email_sender, code_executor)


def test_send_response(
    processor: InstantMessageProcessor, message_analyzer: MessageAnalyzer
) -> None:
    processor._send_response(message_analyzer, b"yes")
    email_sender_mock = cast(Mock, processor.email_sender)
    assert len(email_sender_mock.mock_calls) == 1
    assert email_sender_mock.mock_calls[0].args == (
        "a@a.aa",
        "Re: Test subject",
        b"yes",
    )


def test_proces_message_does_not_raise_exceptions(
    processor: InstantMessageProcessor,
) -> None:
    with mock.patch.object(
        processor,
        "_process_message",
    ) as _process:
        assert processor.process_message(SOME_ID, b"")
        assert _process.called

    with mock.patch.object(
        processor, "_process_message", side_effect=Exception("Fatal")
    ) as _process:
        assert not processor.process_message(SOME_ID, b"")
        assert _process.called


def test_process_message_ok(processor: InstantMessageProcessor) -> None:
    assert processor.process_message(SOME_ID, message_samples.BANANA_MESSAGE)

    email_sender_mock = cast(Mock, processor.email_sender)
    code_executor_mock = cast(Mock, processor.code_executor)

    assert len(email_sender_mock.mock_calls) == 1
    assert email_sender_mock.mock_calls[0].args == (
        "viktor.lacina@gmail.com",
        "Re: Test",
        "OK",
    )

    assert len(code_executor_mock.mock_calls) == 1
    assert code_executor_mock.mock_calls[0].args == (b'print("Banaaaaaana")\n\n', 3)


def test_process_message_invalid_keyword(processor: InstantMessageProcessor) -> None:
    assert processor.process_message(SOME_ID, message_samples.NO_BANANA_MESSAGE)

    email_sender_mock = cast(Mock, processor.email_sender)

    assert len(email_sender_mock.mock_calls) == 1
    assert email_sender_mock.mock_calls[0].args == (
        "viktor.lacina@gmail.com",
        "Re: Test",
        b"Invalid keyword",
    )


def test_process_message_attachment_missing(processor: InstantMessageProcessor) -> None:
    assert processor.process_message(
        SOME_ID, message_samples.MISSING_ATTACHMENT_BANANA_MESSAGE
    )

    email_sender_mock = cast(Mock, processor.email_sender)

    assert len(email_sender_mock.mock_calls) == 1
    assert email_sender_mock.mock_calls[0].args == (
        "viktor.lacina@gmail.com",
        "Re: Test",
        b"Attachment missing",
    )
