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

button_milk: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['milk'],
    callback_data='milk'
)

button_eggs: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['eggs'],
    callback_data='eggs'
)

button_cheese: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['cheese'],
    callback_data='cheese'
)

button_cereals: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['cereals'],
    callback_data='cereals'
)

button_chocolate: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['chocolate'],
    callback_data='chocolate'
)

button_candies: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['candies'],
    callback_data='candies'
)
button_juices: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['juices'],
    callback_data='juices'
)

button_bread: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['bread'],
    callback_data='bread'
)
button_sausage: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['sausage'],
    callback_data='sausage'
)
button_fish: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['fish'],
    callback_data='fish'
)

button_seafood: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['seafood'],
    callback_data='seafood'
)
button_nuts: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['nuts'],
    callback_data='nuts'
)

button_dried_fruits: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['dried_fruits'],
    callback_data='dried_fruits'
)

button_honey: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['honey'],
    callback_data='honey'
)
button_jam: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['jam'],
    callback_data='jam'
)
button_berry: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCT_CATEGORIES['berry'],
    callback_data='berry'
)

product_categories_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
product_categories_builder.row(button_meat, button_bird, button_vegetables, button_fruits, button_pasta, button_milk,
                               button_eggs, button_cheese, button_cereals, button_chocolate, button_candies, button_juices,
                               button_bread, button_sausage, button_fish, button_seafood, button_nuts, button_dried_fruits,
                               button_honey, button_jam, button_berry, width=3)
product_categories_kb: InlineKeyboardMarkup = product_categories_builder.as_markup()










































