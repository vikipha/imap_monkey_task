import email
import logging
from email.header import decode_header
from email.utils import parseaddr

TEXT_PARTS = ("text/plain", "text/html")
FILE_CONTENT_TYPE = "text/x-python"
FILE_SUFFIX = ".py"

log = logging.getLogger(__name__)


class InvalidMessage(Exception):
    pass


class MessageAnalyzer:
    def __init__(self, message_id: str, message_body: bytes) -> None:
        self.message_id = message_id
        self.text_parts: list[email.message.Message] = []
        self.file_parts: list[email.message.Message] = []

        try:
            self._message = email.message_from_bytes(message_body)
        except Exception:
            log.exception("Loading message %s failed", self.message_id)
            raise InvalidMessage()

        self.sender = parseaddr(self._message.get("From"))[-1]
        self.subject = self._get_decoded_subject()

        self._analyze_content()

    def _get_decoded_subject(self):
        """Try to decode with fallback to raw."""
        raw = self._message.get("Subject")
        try:
            extracted_subj = decode_header(raw)[0][0]
            return (
                extracted_subj.decode("utf-8")
                if isinstance(extracted_subj, bytes)
                else extracted_subj
            )
        except Exception:
            log.exception("Error while decoding subject '%s'.", raw)
            return raw

    def _analyze_content(self) -> None:
        for part in self._message.walk():
            content_type = part.get_content_type()
            if content_type in TEXT_PARTS:
                self.text_parts.append(part)
            elif content_type == FILE_CONTENT_TYPE or (
                (filename := part.get_filename())
                and filename.lower().endswith(FILE_SUFFIX)
            ):
                self.file_parts.append(part)

    def contains_keyword(self, keyword: bytes) -> bool:
        for part in self.text_parts:
            if keyword in part.get_payload(decode=True):
                return True
        return False

    def get_attachment_content(self):
        if not self.file_parts:
            return None

        if files_count := len(self.file_parts) > 1:
            log.warning(
                "Message %s has more than one (%s) file attachment",
                self.message_id,
                files_count,
            )

        return self.file_parts[0].get_payload(decode=True)
