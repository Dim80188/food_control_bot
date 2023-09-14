from aiogram import Router
from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards_input import product_categories_kb, meat_kb, bird_kb, vegetables_kb, fruits_kb, pasta_kb
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


@router.callback_query(F.data.in_({'beef', 'pork', 'mutton'}), StateFilter(Input_products.change_product_categories))
async def change_weight_beef(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)


@router.callback_query(F.data == 'bird')
async def change_bird(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию птица\nВыберите продукт', reply_markup=bird_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'chicken', 'turkey', 'duck'}), StateFilter(Input_products.change_product_categories))
async def change_weight_chicken(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'vegetables')
async def change_vegetables(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию овощи\nВыберите продукт', reply_markup=vegetables_kb)
    await state.set_state(Input_products.change_product_categories)


@router.callback_query(F.data.in_({'cabbage', 'cucumbers', 'potato'}), StateFilter(Input_products.change_product_categories))
async def change_weight_vegetables(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'fruits')
async def change_fruits(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию фрукты\nВыберите продукт', reply_markup=fruits_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'apple', 'orange', 'banana'}), StateFilter(Input_products.change_product_categories))
async def change_weight_fruits(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.callback_query(F.data == 'pasta')
async def change_pasta(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию паста\nВыберите продукт', reply_markup=pasta_kb)
    await state.set_state(Input_products.change_product_categories)

@router.callback_query(F.data.in_({'spaghetti'}))
async def change_weight_pasta(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_meal=datetime.now().date())
    await state.update_data(name=LEXICON_PRODUCTS[callback.data])
    await callback.message.answer('Запишите вес')
    await state.set_state(Input_products.change_weight)

@router.message(StateFilter(Input_products.change_weight))
async def write_weight(message: Message, state: FSMContext, request: Request):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    print(data)

















