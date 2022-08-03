from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (f"<b>{message.from_user.first_name}, bot islewine biraz túsinbegenge uqsaysız, keliń sizge járdem bermen.\n</b> ",
            "Bottan tuwrı paydalanıw ushın tómendegi kóriniste xabar jazıń:\n<b>{surah}:{ayah}\n</b>",
            "Mısal ushın Baqara súresi, 255-ayat kerek bolsa. \"<b>2:255</b>\" ti jiberesiz.")

    await message.answer("\n".join(text))
