# test_header.py

from slackbot.blocks.header import HeaderBlock

from tests.test_blocks.constants import PLAIN_TEXT, TEXT


def test_get_header():

    expected_result = {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": TEXT,
            "emoji": True
        }
    }

    result = HeaderBlock.get_header(text=PLAIN_TEXT)
    assert result.dict() == expected_result
