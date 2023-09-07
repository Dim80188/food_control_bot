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

















