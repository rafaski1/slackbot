# composition_objects.py

from enum import Enum
from pydantic import BaseModel
from typing import Optional, List


class CompositionObjectType(str, Enum):
    """
    TBA
    """
    MARKDOWN = "mrkdwn"
    PLAIN_TEXT = "plain_text"


class FilterIncludeType(str, Enum):
    """
    TBA
    """
    IM = "im"
    MPIM = "mpim"
    PRIVATE = "private"
    PUBLIC = "public"


class TriggerActionsOnType(str, Enum):
    """
    TBA
    """
    ON_ENTER_PRESSED = "on_enter_pressed"
    ON_CHARACTER_ENTERED = "on_character_entered"


""" Text Objects: Plain text & markdown """


class Object(BaseModel):
    """
    TBA
    """

    class Config:
        use_enum_values = True


class PlainTextObject(Object):
    """
    TBA
    """
    type: CompositionObjectType = CompositionObjectType.PLAIN_TEXT
    text: str
    emoji: Optional[bool] = None
    verbatim: Optional[bool] = None


class MarkdownObject(Object):
    """
    TBA
    """
    type: CompositionObjectType = CompositionObjectType.MARKDOWN
    text: str
    verbatim: Optional[bool] = None


""" Confirm Object """


class ConfirmationDialogObject(BaseModel):
    """
    TBA
    """
    title: PlainTextObject
    text: PlainTextObject
    confirm: PlainTextObject
    deny: PlainTextObject
    style: Optional[str] = None


""" Option Object """


class OptionObject(BaseModel):
    """
    TBA
    """
    text: PlainTextObject
    value: str
    description: Optional[PlainTextObject] = None
    url: Optional[str] = None


""" Option Group Object """


class OptionGroupObject(BaseModel):
    """
    TBA
    """
    label: PlainTextObject
    options: List[OptionObject]


""" Dispatch Action Object """


class DispatchActionConfigObject(BaseModel):
    """
    TBA
    """
    trigger_actions_on: Optional[List[TriggerActionsOnType]] = None


""" Filter Object """


class FilterObject(BaseModel):
    """
    TBA
    """
    include: Optional[List[FilterIncludeType]] = None
    exclude_external_shared_channels: Optional[bool] = None
    exclude_bot_users: Optional[bool] = None
