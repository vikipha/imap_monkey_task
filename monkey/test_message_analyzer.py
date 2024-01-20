import message_samples
from message_analyzer import MessageAnalyzer

SOME_ID = "1"


def test_contains_both_keyword_and_attachment():
    message = MessageAnalyzer(SOME_ID, message_samples.BANANA_MESSAGE)
    assert message.contains_keyword(keyword=b"banana")
    assert message.get_attachment_content()


def test_missing_keyword():
    message = MessageAnalyzer(SOME_ID, message_samples.NO_BANANA_MESSAGE)
    assert not message.contains_keyword(keyword=b"banana")


def test_contains_keyword_missing_attachment():
    message = MessageAnalyzer(
        SOME_ID, message_samples.MISSING_ATTACHMENT_BANANA_MESSAGE
    )
    assert message.contains_keyword(keyword=b"banana")
    assert not message.get_attachment_content()


def test_data_extracted_from_headers():
    message = MessageAnalyzer(SOME_ID, message_samples.BANANA_MESSAGE)
    assert message.sender == "viktor.lacina@gmail.com"
    assert message.subject == "Test"
