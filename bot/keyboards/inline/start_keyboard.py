from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

startKeyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                "➕", url="https://t.me/username?startgroup=new")
        ]
    ]
)
