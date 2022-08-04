from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.start_keyboard import startKeyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Sálem, {message.from_user.full_name}!\nMeni Telegram gruppalarģa qosıwıńız múmkin.", reply_markup=startKeyboard)
