from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Sálem {message.from_user.full_name}, men sizge Qaraqalpaq tilindegi sózlerdi tuwrı jazılıwın tekserip alıwıńızģa járdem beremen.\n🤖 @kaaimla_bot")
