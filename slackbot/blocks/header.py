# header.py

from slackbot.schemas.blocks import BlockType, HeaderBlockModel
from slackbot.schemas.composition_objects import PlainTextObject


class HeaderBlock:
    """
    TBA
    """
    block_type = BlockType.HEADER

    @staticmethod
    def get_header(text: PlainTextObject) -> HeaderBlockModel:
        """
        TBA
        :param text:
        :return:
        """
        return HeaderBlockModel(text=text)
