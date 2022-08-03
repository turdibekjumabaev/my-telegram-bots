from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Qayta iske túsiriw"),
            types.BotCommand("help", "Járdem soraw"),
        ]
    )
