# blocks.py

from enum import Enum
from typing import List
from pydantic import BaseModel

from slackbot.schemas import block_elements
from slackbot.schemas.composition_objects import PlainTextObject, MarkdownObject


class BlockType(str, Enum):
    """
    TBA
    """
    CONTEXT = "context"
    SECTION = "section"
    DIVIDER = "divider"
    HEADER = "header"
    ACTIONS = "actions"


class BlockModel(BaseModel):
    type: BlockType

    class Config:
        use_enum_values = True


class ContextBlockModel(BlockModel):
    """
    TBA
    """
    type: BlockType = BlockType.CONTEXT
    elements: List[
        block_elements.ImageElement |
        PlainTextObject |
        MarkdownObject
        ]


class DividerBlockModel(BlockModel):
    """
    TBA
    """
    type: BlockType = BlockType.DIVIDER


class HeaderBlockModel(BlockModel):
    """
    TBA
    """
    type: BlockType = BlockType.HEADER
    text: PlainTextObject


class SectionBlockTextModel(BlockModel):
    """
    TBA
    """
    type: BlockType = BlockType.SECTION
    text: PlainTextObject | MarkdownObject


class SectionBlockTextFieldsModel(BlockModel):
    """
    TBA
    """
    type: BlockType = BlockType.SECTION
    fields: List[PlainTextObject | MarkdownObject]


class SectionBlockAccessoryModel(BaseModel):
    """
    TBA
    """
    type: BlockType = BlockType.SECTION
    text: PlainTextObject | MarkdownObject
    accessory: block_elements.Element


class SectionBlockUsersSelectModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.UserSelectElement
    text: PlainTextObject


class SectionBlockStaticSelectModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.StaticSelectElement
    text: PlainTextObject


class SectionBlockMultiStaticSelectModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.MultiStaticSelectElement
    text: PlainTextObject


class SectionBlockMultiConversationsSelectModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.MultiConversationsSelectElement
    text: PlainTextObject


class SectionBlockButtonModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.ButtonElement
    text: PlainTextObject


class SectionBlockRadioButtonsModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.RadioButtonsElement


class SectionBlockCheckboxesModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.CheckboxElement


class SectionBlockOverflowModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.OverflowElement
    text: PlainTextObject


class SectionBlockDatepickerModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.DatePickerElement
    text: PlainTextObject


class SectionBlockTimepickerReturn(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.TimePickerElement
    text: PlainTextObject


class SectionBlockImageModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.ImageElement


class SectionBlockLinkButtonModel(SectionBlockAccessoryModel):
    """
    TBA
    """
    accessory: block_elements.LinkButtonElement


class ActionsBlockElementsModel(BaseModel):
    """
    TBA
    """
    type: BlockType = BlockType.ACTIONS
    elements: List[block_elements.Element]


class ActionsBlockButtonModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[block_elements.ButtonElement]


class ActionsBlockDatepickerModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[block_elements.DatePickerElement]


class ActionsBlockCheckboxesModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[block_elements.CheckboxElement]


class ActionsBlockRadioButtonsModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[block_elements.RadioButtonsElement]


class ActionsBlockTimePickerModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[
        block_elements.TimePickerElement | block_elements.ButtonElement
    ]


class ActionsBlockSelectsWithInitialOptionsModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[
        block_elements.ConversationsSelectElement |
        block_elements.ChannelsSelectElement |
        block_elements.UserSelectElement
        ]


class ActionsBlockFilteredConversationsSelectModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[block_elements.ConversationsSelectElement]


class ActionsBlockAllSelectsModel(ActionsBlockElementsModel):
    """
    TBA
    """
    elements: List[
        block_elements.ConversationsSelectElement |
        block_elements.ChannelsSelectElement |
        block_elements.UserSelectElement |
        block_elements.StaticSelectElement
        ]