from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    msg = f"<b>Assalawma aleykum {message.from_user.full_name}</b>\n\n"
    msg += "Bottan paydalanıw ushın tómendegi kóriniste xabar jazıń:\n"
    msg += "{súre tártip nomeri}:{ayat tártip nomeri}\n\n"
    msg += "<b>Mısalı: 2:255</b>"
    await message.answer(msg)
