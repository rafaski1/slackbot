# test_image.py

from tests.test_blocks.constants import (
    IMAGE, IMAGE_WITH_TITLE, IMAGE_URL, TEXT
)


def test_get_image_no_title():

    expected_result = {
        "type": "image",
        "image_url": IMAGE_URL,
        "alt_text": TEXT
    }

    assert IMAGE.dict() == expected_result


def test_get_image_with_title():

    expected_result = {
        "type": "image",
        "image_url": IMAGE_URL,
        "alt_text": TEXT,
        "title": {
            "type": "plain_text",
            "text": TEXT,
            "emoji": True
        }
    }

    assert IMAGE_WITH_TITLE.dict() == expected_result


