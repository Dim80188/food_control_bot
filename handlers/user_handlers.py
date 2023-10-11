from aiogram import Router
from aiogram import F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard_utils import write_show_kb
from services.simple_calendar import calendar_callback_filter, SimpleCalendar
from states.states import Select_date, Delete_data
from database.database import Request

router: Router = Router()

# реагирует на команду старт и предлагает 2 варианта действий - внести данные и посмотреть данные
@router.message(CommandStart())
async def process_start_command(message: Message, request: Request):
    await request.add_user(message.from_user.id)
    await message.answer(text='Выбери действие', reply_markup=write_show_kb)

@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer('Вы прервали действие.\n\nВыберите дальнейшие действия', reply_markup=write_show_kb)
    await state.clear()

@router.callback_query(F.data == 'complete', ~StateFilter(default_state))
async def process_complete(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Вы завершили введение данных\nВыберите следующее действие', reply_markup=write_show_kb)
    await state.clear()


@router.callback_query(F.data == 'output_data')
async def output_data_func(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Вы выбрали просмотр данных\n\nВыберите начало периода', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(Select_date.start_period)

@router.callback_query(calendar_callback_filter, StateFilter(Select_date.start_period))
async def start_period_change(callback_query: CallbackQuery, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}\n\nВыберите окончание периода',
                                            reply_markup=await SimpleCalendar().start_calendar())
        date = date.date()
        await state.update_data(start_period=date)
        await state.set_state(Select_date.end_period)

@router.callback_query(calendar_callback_filter, StateFilter(Select_date.end_period))
async def end_period_change(callback_query: CallbackQuery, state: FSMContext, request: Request):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}')
        await state.update_data(end_period=date.date())
        period = await state.get_data()
        period_id = callback_query.from_user.id
        read = await request.sql_read(period, period_id)

        for ret in read:
            await callback_query.message.answer(f'Продукт {ret[0]}. Содержит {ret[1]} ккал, {round(ret[2], 2)}гр белка, {round(ret[3], 2)}гр углеводов, {round(ret[4], 2)}гр жиров.\n')
        total = await request.total_data(read)
        await callback_query.message.answer(f'Итого {total[0]}ккал, {round(total[1], 2)}гр белка, {round(total[2], 2)}гр углеводов, {round(total[3], 2)}гр жиров')


@router.message(Command(commands='delete'))
async def process_delete_command_state(message: Message, state: FSMContext):
    await message.answer('Вы выбрали удалить запись.\nВыберите дату', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(Delete_data.change_date)

@router.callback_query(calendar_callback_filter, StateFilter(Delete_data.change_date))
async def show_deletion_data(callback_query: CallbackQuery, state: FSMContext, request: Request):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}')
        await state.update_data(day_deletion_data=date.date())
        period = await state.get_data()
        period_id = await request.get_user_id(callback_query.from_user.id)
        read = await request.sql_read_one_day(period, period_id)
        for ret in read:
            await callback_query.message.answer(f'Дата{ret[2]}. Продукт {ret[3]}. Вес{ret[4]}.\n', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Удалить', callback_data=f'del {ret[0]}')],]))
        await state.set_state(Delete_data.change_data)

@router.callback_query(lambda x: x.data and x.data.startswith('del '), StateFilter(Delete_data.change_data))
async def del_callback_run(callback: CallbackQuery, state: FSMContext, request: Request):
    data_1 = int(callback.data.replace('del ', ''))
    await request.sql_delete_command(data_1)
    await callback.message.answer('Запись удалена.\n Выберите дальнейшие действия', reply_markup=write_show_kb)

























