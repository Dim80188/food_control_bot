from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_PRODUCT_CATEGORIES, LEXICON_PRODUCTS
from aiogram.utils.keyboard import InlineKeyboardBuilder

button_meat: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['meat'],
    callback_data='meat'
)

button_bird: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['bird'],
    callback_data='bird'
)
button_vegetables: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['vegetables'],
    callback_data='vegetables'
)

button_fruits: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['fruits'],
    callback_data='fruits'
)

button_pasta: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['pasta'],
    callback_data='pasta'
)
product_categories_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
product_categories_builder.row(button_meat, button_bird, button_vegetables, button_fruits, button_pasta, width=1)
product_categories_kb: InlineKeyboardMarkup = product_categories_builder.as_markup()

button_beef: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['beef'],
    callback_data='beef'
)
button_pork: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['pork'],
    callback_data='pork'
)
button_mutton: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['mutton'],
    callback_data='mutton'
)
meat_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
meat_builder.row(button_beef, button_pork, button_mutton, width=1)
meat_kb: InlineKeyboardMarkup = meat_builder.as_markup()

button_chicken: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['chicken'],
    callback_data='chicken'
)

button_turkey: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['turkey'],
    callback_data='turkey'
)
button_duck: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['duck'],
    callback_data='duck'
)
bird_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
bird_builder.row(button_chicken, button_turkey, button_duck, width=1)
bird_kb: InlineKeyboardMarkup = bird_builder.as_markup()

button_cabbage: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cabbage'],
    callback_data='cabbage'
)
button_cucumbers: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cucumbers'],
    callback_data='cucumbers'
)
button_potato: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['potato'],
    callback_data='potato'
)
vegetables_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
vegetables_builder.row(button_cabbage, button_cucumbers, button_potato, width=1)
vegetables_kb: InlineKeyboardMarkup = vegetables_builder.as_markup()

button_apple: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['apple'],
    callback_data='apple'
)
button_orange: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['orange'],
    callback_data='orange'
)
button_banana: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['banana'],
    callback_data='banana'
)

fruits_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
fruits_builder.row(button_apple, button_orange, button_banana, width=1)
fruits_kb: InlineKeyboardMarkup = fruits_builder.as_markup()

button_spaghetti: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['spaghetti'],
    callback_data='spaghetti'
)
pasta_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
pasta_builder.row(button_spaghetti)
pasta_kb: InlineKeyboardMarkup = pasta_builder.as_markup()














