# test_context.py

from pytest import raises

from slackbot.blocks.context import ContextBlock
from slackbot.schemas.block_elements import ImageElement
from slackbot.schemas.composition_objects import PlainTextObject, MarkdownObject

from tests.test_blocks.constants import (
    IMAGE, IMAGE_URL, TEXT, PLAIN_TEXT, MARKDOWN_TEXT
)


def test_build_error():

    context = ContextBlock()
    with raises(Exception):
        context.build()


def test_build():

    expected_result = {
        "type": "context",
        "elements": [
            {
                "type": "image",
                "image_url": IMAGE_URL,
                "alt_text": TEXT
            },
            {
                "type": "plain_text",
                "text": TEXT,
                "emoji": True
            }
        ]
    }

    context = ContextBlock()
    context.add_image(image=IMAGE)
    context.add_plain_text(text=PLAIN_TEXT)
    result = context.build()

    assert result.dict() == expected_result


def test_add_image():

    context = ContextBlock()
    context.add_image(image=IMAGE)

    assert context.elements is not []
    assert len(context.elements) == 1
    assert isinstance(context.elements[0], ImageElement)


def test_get_image():

    expected_result = {
        "type": "context",
        "elements": [
            {
                "type": "image",
                "image_url": IMAGE_URL,
                "alt_text": TEXT
            }
        ]
    }
    result = ContextBlock().get_image(IMAGE)
    assert result.dict() == expected_result


def test_add_plain_text():

    context = ContextBlock()
    context.add_plain_text(text=PLAIN_TEXT)

    assert context.elements is not []
    assert len(context.elements) == 1
    assert isinstance(context.elements[0], PlainTextObject)


def test_get_plain_text():

    expected_result = {
        "type": "context",
        "elements": [
            {
                "type": "plain_text",
                "text": TEXT,
                "emoji": True
            }
        ]
    }
    result = ContextBlock().get_plain_text(text=PLAIN_TEXT)
    assert result.dict() == expected_result


def test_add_markdown():

    context = ContextBlock()
    context.add_markdown(text=MARKDOWN_TEXT)

    assert context.elements is not []
    assert len(context.elements) == 1
    assert isinstance(context.elements[0], MarkdownObject)


def test_get_markdown():  # TODO not working

    expected_result = {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": TEXT
            }
        ]
    }
    result = ContextBlock().get_markdown(text=MARKDOWN_TEXT)
    assert result.dict() == expected_result

