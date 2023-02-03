# constants.py

from slackbot.schemas import block_elements
from slackbot.schemas import composition_objects


IMAGE_URL = "https://example.com/xyz.jpg"
IMAGE_TITLE = "This is image title"
TEXT = "hello world"

PLAIN_TEXT = block_elements.PlainTextObject(text=TEXT)
MARKDOWN_TEXT = composition_objects.MarkdownObject(text=TEXT)

IMAGE = block_elements.ImageElement(
    image_url=IMAGE_URL,
    alt_text=TEXT
)

IMAGE_WITH_TITLE = block_elements.ImageElement(
    image_url=IMAGE_URL,
    alt_text=TEXT,
    title=PLAIN_TEXT
)

