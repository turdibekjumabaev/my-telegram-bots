from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Túsinigim boyınsha siz bazı nárselerge túsinbedińiz.</b>",
            "\nBottan paydalanıw tómendegishe ámelge asırıladı.",
            "\n<i>Siz ózińiz  qallegen  sózdi botqa jiberesiz. Eger siz jibergen sóz tuwrı jazılģan bolsa, bot onıń tuwrı ekenligin kórsetedi. Keri jaģdayda, sizge tuwrı jazılģan sózler kórsetiledi.</i>")

    await message.answer("\n".join(text))
