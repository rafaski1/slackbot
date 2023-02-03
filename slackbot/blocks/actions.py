# actions.py

from typing import List

from slackbot.schemas import block_elements
from slackbot.schemas import blocks


class ActionsBlock:
    """
    TBA
    """
    block_type = blocks.BlockType.ACTIONS

    @staticmethod
    def get_all_select(
        elements: List[
            block_elements.ConversationsSelectElement |
            block_elements.ChannelsSelectElement |
            block_elements.UserSelectElement |
            block_elements.StaticSelectElement
            ]
    ) -> blocks.ActionsBlockAllSelectsModel:
        """
        TBA
        :param elements:
        :return:
        """
        return blocks.ActionsBlockAllSelectsModel(elements=elements)

    @staticmethod
    def get_filtered_conversations_select(
        elements: List[block_elements.ConversationsSelectElement]
    ) -> blocks.ActionsBlockFilteredConversationsSelectModel:
        return blocks.ActionsBlockFilteredConversationsSelectModel(
            elements=elements
        )

    @staticmethod
    def get_selects_with_initial_options(
        elements: List[
            block_elements.ConversationsSelectElement |
            block_elements.ChannelsSelectElement |
            block_elements.UserSelectElement
            ]
    ) -> blocks.ActionsBlockSelectsWithInitialOptionsModel:
        """
        TBA
        :param elements:
        :return:
        """
        return blocks.ActionsBlockSelectsWithInitialOptionsModel(
            elements=elements
        )

    @staticmethod
    def get_button(
        elements: List[block_elements.ButtonElement]
    ) -> blocks.ActionsBlockButtonModel:
        """
        TBA
        :param elements:
        :return:
        """
        return blocks.ActionsBlockButtonModel(elements=elements)

    @staticmethod
    def get_datepickers(
        elements: List[block_elements.DatePickerElement]
    ) -> blocks.ActionsBlockDatepickerModel:
        """
        TBA
        :param elements:
        :return:
        """
        return blocks.ActionsBlockDatepickerModel(elements=elements)

    @staticmethod
    def get_checkboxes(
        elements: List[block_elements.CheckboxElement]
    ) -> blocks.ActionsBlockCheckboxesModel:
        """
        TBA
        :param elements:
        :return:
        """
        return blocks.ActionsBlockCheckboxesModel(elements=elements)

    @staticmethod
    def get_radio_buttons(
        elements: List[block_elements.RadioButtonsElement]
    ) -> blocks.ActionsBlockRadioButtonsModel:
        """
        TBA
        :param elements:
        :return:
        """
        return blocks.ActionsBlockRadioButtonsModel(elements=elements)

    @staticmethod
    def get_timepicker(
        elements: List[
            block_elements.TimePickerElement | block_elements.ButtonElement
        ]
    ) -> blocks.ActionsBlockTimePickerModel:
        """
        TBA
        :param elements:
        :return:
        """
        return blocks.ActionsBlockTimePickerModel(elements=elements)
