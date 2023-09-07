from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard_utils import write_show_kb

router: Router = Router()

# реагирует на команду старт и предлагает 2 варианта действий - внести данные и посмотреть данные
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Выбери действие', reply_markup=write_show_kb)









