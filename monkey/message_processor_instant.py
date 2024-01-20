import logging

import config
from code_executor import CodeExecutor
from mailer import Mailer
from message_analyzer import MessageAnalyzer
from message_processor import MessageProcessor

log = logging.getLogger(__name__)


class InstantMessageProcessor(MessageProcessor):
    """Analyze message content and respond to sender."""

    def __init__(self, email_sender: Mailer, code_executor: CodeExecutor) -> None:
        self.email_sender = email_sender
        self.code_executor = code_executor

    def process_message(self, message_id: str, message_body: bytes) -> bool:
        try:
            self._process_message(message_id, message_body)
            return True
        except Exception:
            log.exception("Error while processing message data.")
            return False

    def _process_message(self, message_id: str, message_body: bytes) -> None:
        message = MessageAnalyzer(message_id, message_body)
        if not message.contains_keyword(config.CONTROL_KEYWORD):
            self._send_response(message, b"Invalid keyword")
        else:
            if code_to_execute := message.get_attachment_content():
                body = self.code_executor.execute_code(
                    code_to_execute, config.CODE_EXECUTE_TIMEOUT
                )
                self._send_response(message, body)
            else:
                self._send_response(message, b"Attachment missing")

    def _send_response(self, message: MessageAnalyzer, body: bytes) -> None:
        self.email_sender.send_response(message.sender, f"Re: {message.subject}", body)
