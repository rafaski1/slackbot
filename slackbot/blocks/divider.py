# divider.py

from slackbot.schemas.blocks import BlockType, DividerBlockModel


class DividerBlock:
    """
    TBA
    """
    block_type = BlockType.DIVIDER

    @staticmethod
    def get_divider() -> DividerBlockModel:
        return DividerBlockModel()
    