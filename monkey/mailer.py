import logging
import smtplib
import ssl
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config

log = logging.getLogger(__name__)


class Mailer:
    def send_response(self, rcpt: str, subject: str, body: bytes) -> None:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            config.SMTP_HOST, config.SMTP_PORT, context=context
        ) as server:
            server.login(config.MAIL_USER, config.MAIL_PASS)
            msg = self._make_message(rcpt, subject, body).as_string()
            server.sendmail(config.SENDER_EMAIL, [rcpt], msg)
            log.info("Response sent to %s", rcpt)

    @staticmethod
    def _make_message(rcpt: str, subject: str, body: bytes) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = config.SENDER_EMAIL
        message["To"] = rcpt
        message["Subject"] = Header(subject, "utf-8")
        message.attach(MIMEText(body.decode("utf-8"), "plain", "utf-8"))
        return message
