from aiogram.filters import CommandStart, Command
from aiogram import types, Bot, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold
from loader import dp


@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:

    # Обычные кнопки, привязанные к клавиатуре
    kb = [
        [types.KeyboardButton(text="Робот")],
        [types.KeyboardButton(text="Не робот")],
        [types.KeyboardButton(text="Робот, но мне сказали я не робот")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # кнопки полностью занимают место
        input_field_placeholder="Какой-нибудь текст над кнопками"  # placeholder

    )

    # отправка ответа с разметкой (утолщенный шрифт)
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!', reply_markup=keyboard)

    # инлайн кнопки
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="pressed_my_button"))
    builder.add(types.InlineKeyboardButton(text="Yandex сайт", url="https://ya.ru"))
    builder.add(types.InlineKeyboardButton(text="Чат с админом", url=f'tg://user?id={245391590}'))
    builder.adjust(1, 2)  # 1-я строка 1 кнопка, 2-я две

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='12345', callback_data="pressed_12345")]
    ])
    builder.attach(InlineKeyboardBuilder.from_markup(markup))  # добавление разметки кнопок к кнопкам

    await message.answer(f'Сообщение с инлайн кнопками', reply_markup=builder.as_markup())


# @dp.message(Command(BotCommand(command="stickers", description="STICKERS")))
@dp.message(Command("stickers"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEKylVlXGJiYeK0IauZl0oifvrrjsgu3AACZAADWbv8JToS9CchlsxoMwQ')


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:

        if message.text == 'Робот':
            # удаляем кнопки
            await message.reply("Удаляю кнопки", reply_markup=types.ReplyKeyboardRemove())

        # отправка копии последнего сообщения
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Технические шоколадки!')


# обработчик нажатия на кнопку
# @dp.callback_query(lambda query: query.data == 'pressed_my_button')
@dp.callback_query(F.data == 'pressed_my_button')
async def process_button(query: types.CallbackQuery):
    await query.message.answer('12345')

    # обязательный ответ, даже пустой: query.answer(), чтоб убрать значек ожидания на кнопке
    await query.answer("Вы нажали на кнопку!")  # всплывающее сообщение (toast)



