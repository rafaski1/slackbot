# block_elements.py

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, validator
from typing import Optional, List

from slackbot.schemas.composition_objects import (
    PlainTextObject, ConfirmationDialogObject, OptionGroupObject, FilterObject,
    DispatchActionConfigObject, OptionObject
)


class ElementType(str, Enum):
    """
    TBA
    """
    IMAGE = "image"
    PLAIN_TEXT_INPUT = "plain_text_input"
    BUTTON = "button"
    CHECKBOXES = "checkboxes"
    USERS_SELECT = "users_select"
    STATIC_SELECT = "static_select"
    CONVERSATIONS_SELECT = "conversations_select"
    CHANNELS_SELECT = "channels_select"
    MULTI_CHANNELS_SELECT = "multi_channels_select"
    MULTI_STATIC_SELECT = "multi_static_select"
    MULTI_EXTERNAL_SELECT = "multi_external_select"
    EXTERNAL_SELECT = "external_select"
    MULTI_CONVERSATIONS_SELECT = "multi_conversations_select"
    MULTI_USERS_SELECT = "multi_users_select"
    OVERFLOW = "overflow"
    RADIO_BUTTONS = "radio_buttons"
    DATEPICKER = "datepicker"
    TIMEPICKER = "timepicker"
    DATETIMEPICKER = "datetimepicker"
    EMAIL_TEXT_INPUT = "email_text_input"
    NUMBER_INPUT = "number_input"
    URL_TEXT_INPUT = "url_text_input"


class Element(BaseModel):
    """
    TBA
    """
    type: ElementType

    class Config:
        use_enum_values = True


""" Image element """


class ImageElement(Element):
    image_url: str
    alt_text: str
    type: ElementType = ElementType.IMAGE
    title: Optional[PlainTextObject] = None

    def dict(self, **kwargs) -> dict:
        """
        TBA
        """
        if self.title is None:
            return super().dict(exclude={"title"})
        return super().dict()


""" Button elements: Regular button & button with link """


class ButtonElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.BUTTON
    text: PlainTextObject
    action_id: str
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    confirm: Optional[ConfirmationDialogObject] = None
    accessibility_label: Optional[str] = None

    # TODO style enums


class LinkButtonElement(ButtonElement):
    """
    TBA
    """
    url: str


""" 
Selection elements:
- checkbox, user select, multi conversations select, static select, etc
"""


class CheckboxElement(Element):
    """
    TBA
    """
    type: ElementType.CHECKBOXES
    action_id: str
    options: List[OptionObject]
    initial_options: Optional[List[OptionObject]] = None
    confirm: Optional[ConfirmationDialogObject] = None
    focus_on_load: Optional[bool] = None


class RadioButtonsElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.RADIO_BUTTONS
    action_id: str
    options: List[OptionObject]
    initial_option: Optional[OptionObject] = None
    confirm: Optional[ConfirmationDialogObject] = None
    focus_on_load: Optional[bool] = None


class UserSelectElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.USERS_SELECT
    action_id: str
    initial_user: Optional[str] = None
    confirm: Optional[ConfirmationDialogObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class ConversationsSelectElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.CONVERSATIONS_SELECT
    action_id: str
    initial_conversation: Optional[str] = None
    default_to_current_conversation: Optional[bool] = None
    confirm: Optional[ConfirmationDialogObject] = None
    response_url_enabled: Optional[bool] = None
    filter: Optional[FilterObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class ChannelsSelectElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.CHANNELS_SELECT
    action_id: str
    initial_channel: Optional[str] = None
    confirm: Optional[ConfirmationDialogObject] = None
    response_url_enabled: Optional[bool] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class MultiChannelsSelectElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.MULTI_CHANNELS_SELECT
    action_id: str
    initial_channels: Optional[List[str]] = None
    confirm: Optional[ConfirmationDialogObject] = None
    max_selected_items: Optional[int] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class StaticSelectElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.STATIC_SELECT
    action_id: str
    options: List[OptionObject]
    option_groups: Optional[List[OptionGroupObject]] = None
    initial_option: Optional[OptionObject] = None
    confirm: Optional[ConfirmationDialogObject] = None
    max_selected_items: Optional[int] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class MultiStaticSelectElement(StaticSelectElement):
    """
    TBA
    """
    type: ElementType = ElementType.MULTI_STATIC_SELECT
    option_groups: Optional[List[OptionGroupObject]] = None
    initial_options: Optional[List[OptionObject]] = None
    confirm: Optional[ConfirmationDialogObject] = None
    max_selected_items: Optional[int] = None
    focus_on_load: Optional[bool] = None


class ExternalSelect(Element):
    """
    TBA
    """
    type: ElementType = ElementType.EXTERNAL_SELECT
    action_id: str
    initial_option: Optional[OptionObject] = None
    min_query_length: Optional[int] = None
    confirm: Optional[ConfirmationDialogObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class ExternalDataSource(Element):
    """
    TBA
    """
    type: ElementType = ElementType.MULTI_EXTERNAL_SELECT
    action_id: str
    min_query_length: Optional[int] = None
    initial_options: Optional[List[OptionObject]] = None
    confirm: Optional[ConfirmationDialogObject] = None
    max_selected_items: Optional[int] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class MultiConversationsSelectElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.MULTI_CONVERSATIONS_SELECT
    action_id: str
    initial_conversations: Optional[List[str]] = None
    default_to_current_conversation: Optional[bool] = None
    confirm: Optional[ConfirmationDialogObject] = None
    max_selected_items: Optional[int] = None
    filter: FilterObject
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class OverflowElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.OVERFLOW
    action_id: str
    options: List[OptionObject]
    confirm: Optional[ConfirmationDialogObject] = None


""" Datetime selections """


class DatePickerElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.DATEPICKER
    action_id: str
    initial_date: Optional[str] = None
    confirm: Optional[ConfirmationDialogObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: PlainTextObject = None

    @validator("initial_date")
    def validate_date(cls, value: str):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise
        return value


class TimePickerElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.TIMEPICKER
    action_id: str
    initial_time: Optional[str] = None
    confirm: Optional[ConfirmationDialogObject] = None
    focus_on_load: Optional[bool]
    placeholder: Optional[PlainTextObject] = None
    timezone: Optional[str] = None

    @validator("initial_time")
    def validate_time(cls, value: str):
        try:
            datetime.strptime(value, "%H:%M")
        except ValueError:
            raise
        return value


class DateTimePickerElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.DATETIMEPICKER
    action_id: str
    initial_date_time: Optional[str] = None
    confirm: Optional[ConfirmationDialogObject] = None
    focus_on_load: Optional[bool] = None

    @validator("initial_date_time")
    def validate_time(cls, value: str):
        try:
            datetime.fromtimestamp(int(value))
        except ValueError:
            raise
        return value


class EmailInputElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.EMAIL_TEXT_INPUT
    action_id: str
    initial_value: Optional[str] = None
    dispatch_action_config: Optional[DispatchActionConfigObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class UserList(Element):
    """
    TBA
    """
    type: ElementType = ElementType.MULTI_USERS_SELECT
    action_id: str
    initial_users: Optional[List[str]]
    confirm: Optional[ConfirmationDialogObject] = None
    max_selected_items: Optional[int] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class NumberInput(Element):
    """
    TBA
    """
    type: ElementType = ElementType.NUMBER_INPUT
    is_decimal_allowed: bool
    action_id: Optional[str] = None
    initial_value: Optional[str] = None
    min_value: Optional[str] = None
    max_value: Optional[str] = None
    dispatch_action_config: Optional[DispatchActionConfigObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class PlainTextInputElement(Element):
    """
    TBA
    """
    type: ElementType = ElementType.PLAIN_TEXT_INPUT
    action_id: str
    initial_value: Optional[str] = None
    multiline: Optional[bool] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    dispatch_action_config: Optional[DispatchActionConfigObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None


class UrlInput(Element):
    """
    TBA
    """
    type: ElementType = ElementType.URL_TEXT_INPUT
    action_id: str
    initial_value: Optional[str] = None
    dispatch_action_config: Optional[DispatchActionConfigObject] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[PlainTextObject] = None