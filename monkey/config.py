import os

# override in ENV, see env/monkey.env

CONTROL_KEYWORD = os.getenv("CONTROL_KEYWORD", "banana").encode("utf-8")  # bytes

IMAP_HOST = os.getenv("IMAP_HOST", "valid.imap.host")
IMAP_FOLDER = os.getenv("IMAP_FOLDER", "Inbox")
IMAP_BATCH_SIZE = int(os.getenv("IMAP_BATCH_SIZE", "5"))

INCOMING_EMAIL_PATTERN = os.getenv("INCOMING_EMAIL_PATTERN", "rapid7.com")

MAIL_USER = os.getenv("MAIL_USER", "valid.user")
MAIL_PASS = os.getenv("MAIL_PASS", "valid.pass")

SMTP_HOST = os.getenv("SMTP_HOST", "valid.smtp.host.here")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))

SENDER_EMAIL = os.getenv("SENDER_EMAIL", "valid@sender.here")

TEMP_DIR_FOR_ATTACHMENTS = os.getenv("TEMP_DIR_FOR_ATTACHMENTS", "/tmp")
CODE_EXECUTE_TIMEOUT = int(os.getenv("CODE_EXECUTE_TIMEOUT", "3"))
