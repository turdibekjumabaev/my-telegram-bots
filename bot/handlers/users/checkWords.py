from aiogram import types
from matplotlib.style import available

from loader import dp
from handlers.users.kaawords import words

from difflib import get_close_matches


def checkWords(word: str, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word

    return {'available': available, 'matches': matches}


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    word = message.text
    result = checkWords(word=message.text)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"

    await message.answer(response)
