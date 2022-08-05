from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Bottı iske túsiriw"),
            types.BotCommand("help", "Járdem"),
            types.BotCommand("set_photo", "Gruppa súwretin ózgertiw"),
            types.BotCommand("set_title", "Gruppa atın ózgertiw "),
            types.BotCommand("set_description",
                             "Gruppa haqqindaģı maģlumattı ózgertiw"),
            types.BotCommand(
                "ro", "Paydalanıwshını Read Only rejimge ótkiziw"),
            types.BotCommand("unro", "Read Only rejimden shıģarıw"),
            types.BotCommand("ban", "Ban"),
            types.BotCommand("unban", "Bannan shiģarıw"),
        ]
    )
