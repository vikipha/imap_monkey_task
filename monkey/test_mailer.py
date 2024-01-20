import config
from mailer import Mailer


def test_make_message() -> None:
    msg_text = Mailer._make_message("a@a.aa", "subj", b"content").as_string()
    assert "Subject: =?utf-8?q?subj?=" in msg_text
    assert f"From: {config.SENDER_EMAIL}" in msg_text
    assert "Y29udGVudA==" in msg_text  # content
