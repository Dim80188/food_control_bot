from aiogram import Router
from aiogram import F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard_utils import write_show_kb
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








