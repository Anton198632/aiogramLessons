from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from loader import dp


class RegistrationState(StatesGroup):
    input_phone = State()
    input_code = State()


@dp.message(Command("reg"))
async def command_reg(message: Message, state: FSMContext):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!\nInput phone:")
    await state.set_state(RegistrationState.input_phone)


@dp.message(RegistrationState.input_phone)
async def input_phone_handle(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Input code:")
    await state.set_state(RegistrationState.input_code)


@dp.message(RegistrationState.input_code)
async def input_phone_handle(message: Message, state: FSMContext):
    await state.update_data(code=message.text)
    user_data = await state.get_data()
    await message.answer(f"Phone: {user_data['phone']}, code: {user_data['code']}")
    await state.clear()
