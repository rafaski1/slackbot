# test_divider.py

from slackbot.blocks.divider import DividerBlock


def test_get_divider():

    expected_result = {
        "type": "divider"
    }
    result = DividerBlock.get_divider()
    assert result.dict() == expected_result
