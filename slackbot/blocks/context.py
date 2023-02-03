# context.py

from typing import List, Union

from slackbot.schemas.blocks import BlockType, ContextBlockModel
from slackbot.schemas.block_elements import ImageElement
from slackbot.schemas.composition_objects import PlainTextObject, MarkdownObject


class ContextBlock:
    """
    TBA
    """
    block_type = BlockType.CONTEXT

    def __init__(self):
        self.elements: List[Union[
            ImageElement,
            PlainTextObject,
            MarkdownObject
        ]] = list()

    def build(self) -> ContextBlockModel:
        """
        TBA
        :return:
        """
        if not self.elements:
            raise Exception  # TODO custom error

        return ContextBlockModel(
            type=self.block_type,
            elements=self.elements
        )

    def add_image(self, image: ImageElement) -> None:
        """
        TBA
        :param image:
        :return:
        """
        if image.title is not None:
            image.title = None  # TODO log warning

        self.elements.append(image)

    def get_image(self, image: ImageElement) -> ContextBlockModel:
        """
        TBA
        :param image:
        :return:
        """
        self.add_image(image=image)
        return self.build()

    def add_plain_text(self, text: PlainTextObject) -> None:
        """
        TBA
        :param text:
        :return:
        """
        self.elements.append(text)

    def get_plain_text(self, text: PlainTextObject) -> ContextBlockModel:
        """
        TBA
        :param text:
        :return:
        """
        self.add_plain_text(text)
        return self.build()

    def add_markdown(self, text: MarkdownObject) -> None:
        """
        TBA
        :param text:
        :return:
        """
        self.elements.append(text)

    def get_markdown(self, text: MarkdownObject) -> ContextBlockModel:
        """
        TBA
        :param text:
        :return:
        """
        self.add_markdown(text=text)
        return self.build()
