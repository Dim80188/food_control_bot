from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_PRODUCT_CATEGORIES, LEXICON_PRODUCTS
from aiogram.utils.keyboard import InlineKeyboardBuilder


button_beef: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['beef'],
    callback_data='beef'
)

button_beef_tederloin: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['beef_tenderloin'],
    callback_data='beef_tenderloin'
)

button_beef_soup: InlineKeyboardButton =  InlineKeyboardButton(
    text=LEXICON_PRODUCTS['beef_soup'],
    callback_data='beef_soup'
)

button_pork: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['pork'],
    callback_data='pork'
)

button_pork_tenderloin: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['pork_tenderloin'],
    callback_data='pork_tenderloin'
)

button_bacon: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['bacon'],
    callback_data='bacon'
)

button_salo: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['salo'],
    callback_data='salo'
)

button_mutton: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['mutton'],
    callback_data='mutton'
)
meat_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
meat_builder.row(button_beef, button_beef_tederloin, button_pork, button_mutton, button_beef_soup,
                 button_pork_tenderloin, button_bacon, button_salo, width=1)
meat_kb: InlineKeyboardMarkup = meat_builder.as_markup()

button_chicken: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['chicken'],
    callback_data='chicken'
)

button_chicken_breast: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['chicken_breast'],
    callback_data='chicken_breast'
)

button_chicken_thigh: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['chicken_thigh'],
    callback_data='chicken_thigh'
)

button_chicken_leg: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['chicken_leg'],
    callback_data='chicken_leg'
)

button_chicken_wing: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['chicken_wing'],
    callback_data='chicken_wing'
)

button_turkey_breast: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['turkey_breast'],
    callback_data='turkey_breast'
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
bird_builder.row(button_chicken, button_chicken_breast,button_chicken_thigh, button_chicken_leg,
                 button_chicken_wing, button_turkey, button_turkey_breast, button_duck, width=1)
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

button_carrot: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['carrot'],
    callback_data='carrot'
)

button_zucchini: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['zucchini'],
    callback_data='zucchini'
)

button_eggplant: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['eggplant'],
    callback_data='eggplant'
)

button_tomato: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['tomato'],
    callback_data='tomato'
)

button_onion: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['onion'],
    callback_data='onion'
)

vegetables_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
vegetables_builder.row(button_cabbage, button_cucumbers, button_potato, button_carrot, button_zucchini, button_eggplant,
                       button_tomato, button_onion, width=2)
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

button_grape: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['grape'],
    callback_data='grape'
)

button_pears: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['pears'],
    callback_data='pears'
)


fruits_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
fruits_builder.row(button_apple, button_orange, button_banana, button_grape, button_pears, width=2)
fruits_kb: InlineKeyboardMarkup = fruits_builder.as_markup()

button_spaghetti: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['spaghetti'],
    callback_data='spaghetti'
)
pasta_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
pasta_builder.row(button_spaghetti)
pasta_kb: InlineKeyboardMarkup = pasta_builder.as_markup()

button_milk_3_2: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['milk_3_2'],
    callback_data='milk_3_2'
)

button_kefir_3_2: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['kefir_3_2'],
    callback_data='kefir_3_2'
)

button_yogurt: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['yogurt'],
    callback_data='yogurt'
)
button_cottage_cheese_9: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cottage_cheese_9'],
    callback_data='cottage_cheese_9'
)
button_cottage_cheese_5: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cottage_cheese_5'],
    callback_data='cottage_cheese_5'
)

button_cottage_cheese_1: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cottage_cheese_1'],
    callback_data='cottage_cheese_1'
)

button_sour_cream_25: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['sour_cream_25'],
    callback_data='sour_cream_25'
)

button_sour_cream_20: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['sour_cream_20'],
    callback_data='sour_cream_25'
)

button_sour_cream_15: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['sour_cream_15'],
    callback_data='sour_cream_15'
)
button_butter: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['butter_82'],
    callback_data='butter_82'
)
button_cream: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cream_20'],
    callback_data='cream_20'
)

milk_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
milk_builder.row(button_milk_3_2, button_kefir_3_2, button_yogurt, button_cottage_cheese_9, button_cottage_cheese_5,
                 button_cottage_cheese_1, button_sour_cream_25, button_sour_cream_20, button_sour_cream_15, button_butter,
                 button_cream, width=3)
milk_kb: InlineKeyboardMarkup = milk_builder.as_markup()

button_selected_eggs: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['selected_eggs'],
    callback_data='selected_eggs'
)

button_eggs_1: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['eggs_1'],
    callback_data='eggs_1'
)
eggs_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
eggs_builder.row(button_selected_eggs, button_eggs_1, width=2)
eggs_kb: InlineKeyboardMarkup = eggs_builder.as_markup()

button_hard_cheese: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['hard_cheese'],
    callback_data='hard_cheese'
)
button_processed_cheese: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['processed_cheese'],
    callback_data='processed_cheese'
)

cheese_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
cheese_builder.row(button_hard_cheese, button_processed_cheese, width=2)
cheese_kb: InlineKeyboardMarkup = cheese_builder.as_markup()

button_rice: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['rice'],
    callback_data='rice'
)

button_buckwheat: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['buckwheat'],
    callback_data='buckwheat'
)

button_peas: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['peas'],
    callback_data='peas'
)

button_beans_beans: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['beans_beans'],
    callback_data='beans_beans'
)

cereals_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
cereals_builder.row(button_rice, button_buckwheat, button_peas, button_beans_beans, width=2)
cereals_kb: InlineKeyboardMarkup = cereals_builder.as_markup()

button_dark_chocolate: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['dark_chocolate'],
    callback_data='dark_chocolate'
)

button_milk_chocolate: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['milk_chocolate'],
    callback_data='milk_chocolate'
)
chocolate_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
chocolate_builder.row(button_dark_chocolate, button_milk_chocolate, width=2)
chocolate_kb: InlineKeyboardMarkup = chocolate_builder.as_markup()

button_lollipops: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['lollipops'],
    callback_data='lollipops'
)

candies_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
candies_builder.row(button_lollipops)
candies_kb: InlineKeyboardMarkup = candies_builder.as_markup()

button_apple_juice: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['apple_juice'],
    callback_data='apple_juice'
)

button_orange_juice: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['orange_juice'],
    callback_data='orange_juice'
)

button_pomegranate_juice: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['pomegranate_juice'],
    callback_data='pomegranate_juice'
)

button_tomato_juice: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['tomato juice'],
    callback_data='tomato juice'
)
juice_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
juice_builder.row(button_apple_juice, button_orange_juice, button_pomegranate_juice, button_tomato_juice, width=2)
juice_kb: InlineKeyboardMarkup = juice_builder.as_markup()

button_wheat_bread: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['wheat_bread'],
    callback_data='wheat_bread'
)
button_rye_bread: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['rye_bread'],
    callback_data='rye_bread'
)

button_bread: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['bread'],
    callback_data='bread'
)
bread_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
bread_builder.row(button_wheat_bread, button_rye_bread, button_bread, width=2)
bread_kb: InlineKeyboardMarkup = bread_builder.as_markup()

button_milk_sausages: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['milk_sausages'],
    callback_data='milk_sausages'
)

button_doctors_sausages: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['doctors_sausages'],
    callback_data='doctors_sausages'
)
button_doctors_sausage: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['doctors_sausage'],
    callback_data='doctors_sausage'
)

sausages_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
sausages_builder.row(button_milk_sausages, button_doctors_sausages, button_doctors_sausage, width=2)
sausages_kb: InlineKeyboardMarkup = sausages_builder.as_markup()

button_trout: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['trout'],
    callback_data='trout'
)
button_salmon: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['salmon'],
    callback_data='salmon'
)
button_cod: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cod'],
    callback_data='cod'
)
button_coho_salmon: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['coho_salmon'],
    callback_data='coho_salmon'
)
button_navaga: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['navaga'],
    callback_data='navaga'
)
fish_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
fish_builder.row(button_trout, button_salmon, button_cod, button_coho_salmon, button_navaga, width=2)
fish_kb: InlineKeyboardMarkup = fish_builder.as_markup()

button_mussels: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['mussels'],
    callback_data='mussels'
)
seafood_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
seafood_builder.row(button_mussels)
seafood_kb: InlineKeyboardMarkup = seafood_builder.as_markup()

button_walnut: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['walnut'],
    callback_data='walnut'
)
button_pistachios: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['pistachios'],
    callback_data='pistachios'
)
button_hazelnut: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['hazelnut'],
    callback_data='hazelnut'
)
button_peanut: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['peanut'],
    callback_data='peanut'
)
nuts_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
nuts_builder.row(button_walnut, button_pistachios, button_hazelnut, button_peanut, width=3)
nuts_kb: InlineKeyboardMarkup = nuts_builder.as_markup()

button_raisin: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['raisin'],
    callback_data='raisin'
)
button_dried_apricots: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['dried_apricots'],
    callback_data='dried_apricots'
)
dried_fruits_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
dried_fruits_builder.row(button_raisin, button_dried_apricots, width=2)
dried_fruits_kb: InlineKeyboardMarkup = dried_fruits_builder.as_markup()

button_buckwheat_honey: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['buckwheat_honey'],
    callback_data='buckwheat_honey'
)
button_flower_honey: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['flower_honey'],
    callback_data='flower_honey'
)
honey_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
honey_builder.row(button_buckwheat_honey, button_flower_honey, width=2)
honey_kb: InlineKeyboardMarkup = honey_builder.as_markup()

button_strawberry_jam: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['strawberry_jam'],
    callback_data='strawberry_jam'
)
button_apricot_jam: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['apricot_jam'],
    callback_data='apricot_jam'
)
jam_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
jam_builder.row(button_strawberry_jam, button_apricot_jam, width=2)
jam_kb: InlineKeyboardMarkup = jam_builder.as_markup()


button_strawberry: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['strawberry'],
    callback_data='strawberry'
)

button_blueberry: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['blueberry'],
    callback_data='blueberry'
)
button_cherry: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cherry'],
    callback_data='cherry'
)
button_cherries: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_PRODUCTS['cherries'],
    callback_data='cherries'
)

berry_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
berry_builder.row(button_strawberry, button_blueberry, button_cherry, button_cherries, width=2)
berry_kb: InlineKeyboardMarkup = berry_builder.as_markup()

























