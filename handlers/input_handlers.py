from aiogram import Router
from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards_products import (meat_kb, bird_kb, vegetables_kb, fruits_kb, pasta_kb, milk_kb, eggs_kb, cheese_kb,
                                          cereals_kb, chocolate_kb, candies_kb, juice_kb, bread_kb, sausages_kb, fish_kb,
                                          seafood_kb, nuts_kb, dried_fruits_kb, honey_kb, jam_kb, berry_kb)
from keyboards.keyboards_product_categories import product_categories_kb
from keyboards.keyboard_utils import continue_complete_kb
from states.states import Input_products
from lexicon.lexicon_ru import LEXICON_PRODUCTS
from datetime import datetime
from database.database import Request


router: Router = Router()
# Принимаю выбор внести данные
# Предлагаю выбрать категорию
@router.callback_query(F.data == 'enter_data')
async def change_enter_data(callback: CallbackQuery):
    await callback.message.answer(text='Вы выбрали внести данные\nВыберите катерию продукта', reply_markup=product_categories_kb)

# предлагаю выбрать продукт из категории


@router.callback_query(F.data == 'meat')
async def change_meat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию мясо\nВыберите продукт', reply_markup=meat_kb)
    await state.set_state(Input_products.change_product_categories)


@router.callback_query(F.data.in_({'beef', 'pork', 'mutton', 'beef_tenderloin', 'beef_soup', 'pork_tenderloin',
                                   'bacon', 'salo'}), StateFilter(Input_products.change_product_categories))
async def change_weight_beef(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)


@router.callback_query(F.data == 'bird')
async def change_bird(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию птица\nВыберите продукт', reply_markup=bird_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'chicken', 'chicken_breast', 'chicken_thigh', 'chicken_leg', 'chicken_wing', 'turkey_breast', 'turkey', 'duck'}), StateFilter(Input_products.change_product_categories))
async def change_weight_chicken(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'vegetables')
async def change_vegetables(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию овощи\nВыберите продукт', reply_markup=vegetables_kb)
    await state.set_state(Input_products.change_product_categories)


@router.callback_query(F.data.in_({'cabbage', 'cucumbers', 'potato', 'carrot', 'zucchini', 'eggplant', 'tomato', 'onion'}), StateFilter(Input_products.change_product_categories))
async def change_weight_vegetables(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'fruits')
async def change_fruits(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию фрукты\nВыберите продукт', reply_markup=fruits_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'apple', 'orange', 'banana', 'grape', 'pears'}), StateFilter(Input_products.change_product_categories))
async def change_weight_fruits(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'pasta')
async def change_pasta(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию паста\nВыберите продукт', reply_markup=pasta_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'spaghetti'}), StateFilter(Input_products.change_product_categories))
async def change_weight_pasta(callback: CallbackQuery, state: FSMContext, request: Request):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'milk')
async def change_milk(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию молоко\nВыберите продукт', reply_markup=milk_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'milk_3_2', 'kefir_3_2', 'yogurt', 'cottage_cheese_9', 'cottage_cheese_5', 'cottage_cheese_1',
                                   'sour_cream_25', 'sour_cream_20', 'sour_cream_15', 'butter_82', 'cream_20'}), StateFilter(Input_products.change_product_categories))
async def change_weight_milk(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'eggs')
async def change_eggs(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию яйца\nВыберите продукт', reply_markup=eggs_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'selected_eggs', 'eggs_1'}), StateFilter(Input_products.change_product_categories))
async def change_weight_eggs(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'cheese')
async def change_cheese(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию сыр\nВыберите продукт', reply_markup=cheese_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'hard_cheese', 'processed_cheese'}), StateFilter(Input_products.change_product_categories))
async def change_weight_cheese(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'cereals')
async def change_cereals(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию крупы\nВыберите продукт', reply_markup=cereals_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'rice', 'buckwheat', 'peas', 'beans_beans'}), StateFilter(Input_products.change_product_categories))
async def change_weight_cereals(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'chocolate')
async def change_chocolate(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию шоколад\nВыберите продукт', reply_markup=chocolate_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'dark_chocolate', 'milk_chocolate'}), StateFilter(Input_products.change_product_categories))
async def change_weight_chocolate(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'candies')
async def change_candies(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию конфеты\nВыберите продукт', reply_markup=candies_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'lollipops',}), StateFilter(Input_products.change_product_categories))
async def change_weight_candies(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'juices')
async def change_juices(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию соки\nВыберите продукт', reply_markup=juice_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'apple_juice', 'orange_juice', 'pomegranate_juice', 'tomato juice'}), StateFilter(Input_products.change_product_categories))
async def change_weight_juices(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'bread')
async def change_bread(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию хлеб\nВыберите продукт', reply_markup=bread_kb)
    await state.set_state(Input_products.change_product_categories)


@router.callback_query(F.data.in_({'wheat_bread', 'rye_bread', 'bread'}), StateFilter(Input_products.change_product_categories))
async def change_weight_juices(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'sausage')
async def change_sausage(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию колбаса\nВыберите продукт', reply_markup=sausages_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'milk_sausages', 'doctors_sausages', 'doctors_sausage'}), StateFilter(Input_products.change_product_categories))
async def change_weight_sausages(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'fish')
async def change_fish(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию рыба\nВыберите продукт', reply_markup=fish_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'trout', 'salmon', 'cod', 'coho_salmon', 'navaga'}), StateFilter(Input_products.change_product_categories))
async def change_weight_fish(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'seafood')
async def change_seafood(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию морепродукты\nВыберите продукт', reply_markup=seafood_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'mussels', }), StateFilter(Input_products.change_product_categories))
async def change_weight_seafood(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'nuts')
async def change_nuts(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию орехи\nВыберите продукт', reply_markup=nuts_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'walnut', 'pistachios', 'hazelnut', 'peanut'}), StateFilter(Input_products.change_product_categories))
async def change_weight_nuts(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'dried_fruits')
async def change_dried_fruits(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию сухофрукты\nВыберите продукт', reply_markup=dried_fruits_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'raisin', 'dried_apricots'}), StateFilter(Input_products.change_product_categories))
async def change_weight_dried_fruits(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'honey')
async def change_honey(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию мед\nВыберите продукт', reply_markup=honey_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'buckwheat_honey', 'flower_honey'}), StateFilter(Input_products.change_product_categories))
async def change_weight_honey(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'jam')
async def change_jam(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию варенье\nВыберите продукт', reply_markup=jam_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'strawberry_jam', 'apricot_jam'}), StateFilter(Input_products.change_product_categories))
async def change_weight_honey(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'berry')
async def change_berry(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию ягоды\nВыберите продукт', reply_markup=berry_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'strawberry', 'blueberry', 'cherry', 'cherries'}),
                           StateFilter(Input_products.change_product_categories))
async def change_weight_honey(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)


@router.message(StateFilter(Input_products.change_weight))
async def write_weight(message: Message, state: FSMContext, request: Request):
    user_id = await request.get_user_id(message.from_user.id)
    await state.update_data(user_id=user_id)
    # await state.update_data(weight=message.text)
    weight = message.text
    if ',' in weight:
        weight_in_base = weight.replace(',', '.')
    else:
        weight_in_base = weight
    weight_1 = weight_in_base.replace('.', '')
    if weight_1.isdigit():
        await state.update_data(weight=weight_in_base)
        data = await state.get_data()
        await request.add_meal(data)
        await message.answer('Данные внесены. Продолжаем вносить?', reply_markup=continue_complete_kb)
    else:

        await message.answer('<b>Вес должен быть числом.</b>\n'
                              '<b>Пожалуйста, введите данные заново</b>', reply_markup=product_categories_kb)

















