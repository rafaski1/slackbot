# section.py

from typing import List

from slackbot.schemas import block_elements
from slackbot.schemas import blocks
from slackbot.schemas.composition_objects import PlainTextObject, MarkdownObject


class SectionBlock:
    """
    TBA
    """
    block_type = blocks.BlockType.SECTION

    @staticmethod
    def get_plain_text(
        text: PlainTextObject
    ) -> blocks.SectionBlockTextModel:
        """
        TBA
        :param text:
        :return:
        """
        return blocks.SectionBlockTextModel(text=text)

    @staticmethod
    def get_markdown(
        text: MarkdownObject
    ) -> blocks.SectionBlockTextModel:
        """
        TBA
        :param text:
        :return:
        """
        return blocks.SectionBlockTextModel(text=text)

    @staticmethod
    def get_text_fields(
        fields: List[PlainTextObject | MarkdownObject]
    ) -> blocks.SectionBlockTextFieldsModel:
        """
        TBA
        :param fields:
        :return:
        """
        return blocks.SectionBlockTextFieldsModel(fields=fields)

    @staticmethod
    def get_user_select(
        text: PlainTextObject,
        accessory: block_elements.UserSelectElement
    ) -> blocks.SectionBlockUsersSelectModel:
        """
        TBA
        :param text:
        :param accessory:
        :return:
        """
        return blocks.SectionBlockUsersSelectModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_static_select(
        text: PlainTextObject,
        accessory: block_elements.StaticSelectElement
    ) -> blocks.SectionBlockStaticSelectModel:
        return blocks.SectionBlockStaticSelectModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_multi_static_select(
        text: PlainTextObject,
        accessory: block_elements.MultiStaticSelectElement
    ) -> blocks.SectionBlockMultiStaticSelectModel:
        return blocks.SectionBlockMultiStaticSelectModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_multi_conversations_select(
        text: PlainTextObject,
        accessory: block_elements.MultiConversationsSelectElement
    ) -> blocks.SectionBlockMultiConversationsSelectModel:
        return blocks.SectionBlockMultiConversationsSelectModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_button(
        text: PlainTextObject,
        accessory: block_elements.ButtonElement
    ) -> blocks.SectionBlockButtonModel:
        return blocks.SectionBlockButtonModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_link_button(
        text: PlainTextObject,
        accessory: block_elements.LinkButtonElement
    ) -> blocks.SectionBlockLinkButtonModel:
        return blocks.SectionBlockLinkButtonModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_image(
        text: PlainTextObject | MarkdownObject,
        accessory: block_elements.ImageElement
    ) -> blocks.SectionBlockImageModel:
        return blocks.SectionBlockImageModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_overflow(
        text: PlainTextObject,
        accessory: block_elements.OverflowElement
    ) -> blocks.SectionBlockOverflowModel:
        return blocks.SectionBlockOverflowModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_datepicker(
        text: PlainTextObject,
        accessory: block_elements.DatePickerElement
    ) -> blocks.SectionBlockDatepickerModel:
        return blocks.SectionBlockDatepickerModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_checkboxes(
        text: PlainTextObject | MarkdownObject,
        accessory: block_elements.CheckboxElement
    ) -> blocks.SectionBlockCheckboxesModel:
        return blocks.SectionBlockCheckboxesModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_radio_buttons(
        text: PlainTextObject | MarkdownObject,
        accessory: block_elements.RadioButtonsElement
    ) -> blocks.SectionBlockRadioButtonsModel:
        return blocks.SectionBlockRadioButtonsModel(
            text=text,
            accessory=accessory
        )

    @staticmethod
    def get_timepicker(
        text: PlainTextObject,
        accessory: block_elements.TimePickerElement
    ) -> blocks.SectionBlockTimepickerReturn:
        return blocks.SectionBlockTimepickerReturn(
            text=text,
            accessory=accessory
        )
