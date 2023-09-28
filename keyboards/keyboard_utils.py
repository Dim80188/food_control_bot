from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON
from aiogram.utils.keyboard import InlineKeyboardBuilder

button_write: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['enter_data'],
    callback_data='enter_data'
)

button_output: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['output_data'],
    callback_data='output_data'
)
write_show_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
write_show_builder.row(button_write, button_output, width=1)
write_show_kb: InlineKeyboardMarkup = write_show_builder.as_markup()

button_continue: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['continue_to_contribute'],
    callback_data='enter_data'
)
button_complete: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['complete'],
    callback_data='complete'
)
continue_complete_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
continue_complete_builder.row(button_continue, button_complete, width=1)
continue_complete_kb: InlineKeyboardMarkup = continue_complete_builder.as_markup()

















