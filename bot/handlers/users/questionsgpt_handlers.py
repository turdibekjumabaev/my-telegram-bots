from aiogram import types
from aiogram.dispatcher.filters.builtin import ContentTypeFilter

from loader import dp
from utils.chatgpt import ask_gpt


@dp.message_handler(ContentTypeFilter(types.ChatType.PRIVATE))
async def bot_echo(message: types.Message):
    await message.answer(ask_gpt(message.text))
