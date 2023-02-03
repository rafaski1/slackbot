# test_section.py

from slackbot.blocks.section import SectionBlock

from tests.test_blocks.constants import (
    TEXT, PLAIN_TEXT, MARKDOWN_TEXT
)


def test_get_plain_text():

    expected_result = {
        "type": "section",
        "text": {
            "type": "plain_text",
            "text": TEXT,
            "emoji": True
        }
    }

    result = SectionBlock.get_plain_text(text=PLAIN_TEXT)
    assert result.dict() == expected_result


def test_get_markdown():  # TODO NOT WORKING

    expected_result = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": TEXT
        }
    }

    result = SectionBlock.get_markdown(text=MARKDOWN_TEXT)
    assert result.dict() == expected_result


def test_get_text_fields():  # TODO NOT WORKING

    expected_result = {
        "type": "section",
        "fields": [
            {
                "type": "plain_text",
                "text": TEXT,
                "emoji": True
            },
            {
                "type": "plain_text",
                "text": TEXT,
                "emoji": True
            },
            {
                "type": "mrkdwn",
                "text": TEXT
            }
        ]
    }

    result = SectionBlock.get_text_fields(
        fields=[PLAIN_TEXT, PLAIN_TEXT, MARKDOWN_TEXT]
    )
    assert result.dict() == expected_result


def test_get_user_select():

    expected_result = {}

    result = SectionBlock.get_user_select()

    assert result.dict() == expected_result


def test_get_static_select():

    expected_result = {}

    result = SectionBlock.get_static_select()

    assert result.dict() == expected_result


def test_get_multi_static_select():

    expected_result = {}

    result = SectionBlock.get_multi_static_select()

    assert result.dict() == expected_result


def test_get_multi_conversations_select():

    expected_result = {}

    result = SectionBlock.get_multi_conversations_select()

    assert result.dict() == expected_result


def test_get_button():

    expected_result = {}

    result = SectionBlock.get_button()

    assert result.dict() == expected_result


def test_get_link_button():

    expected_result = {}

    result = SectionBlock.get_link_button()

    assert result.dict() == expected_result


def test_get_image():

    expected_result = {}

    result = SectionBlock.get_image()

    assert result.dict() == expected_result


def test_get_overflow():

    expected_result = {}

    result = SectionBlock.get_overflow()

    assert result.dict() == expected_result


def test_get_datepicker():

    expected_result = {}

    result = SectionBlock.get_datepicker()

    assert result.dict() == expected_result


def test_get_checkboxes():

    expected_result = {}

    result = SectionBlock.get_checkboxes()

    assert result.dict() == expected_result


def test_get_radio_buttons():

    expected_result = {}

    result = SectionBlock.get_radio_buttons()

    assert result.dict() == expected_result


def test_get_timepicker():

    expected_result = {}

    result = SectionBlock.get_timepicker()

    assert result.dict() == expected_result
