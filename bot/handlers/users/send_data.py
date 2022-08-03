from aiogram import types, exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.alQuranCloud import get_sura_name
from utils.quranEnc import get_data
from loader import dp


@dp.message_handler()
async def send_data(msg: types.Message):
    if len(msg.text.split(':')) == 2:
        if get_data(msg.text):
            output = get_data(msg.text)
            output['surah_name'] = get_sura_name(msg.text)

            caption = f"<b>«{output['surah_name']}» súresi, {output['number_in_surah']}-ayat</b>"

            ans = output['text'] + '\n\n'
            ans += f"<a href='{output['image_url']}'> </a>\n"
            ans += f"«{output['surah_name']}» súresi, {output['number_in_surah']}-ayat." + "\n\n"

            if output['footnotes'] != '':
                ans += output['footnotes'] + "\n\n"

            ans += "<b>— Alauddin Mansur</b>"

            await msg.answer_voice(output['audio'], caption)
            await msg.answer(ans)
        else:
            await msg.reply("<b>Maģlumat tabılmadı.</b>")
    else:
        try:
            try:

                if send_audio(int(msg.text)):
                    name = get_sura_name(f'{int(msg.text)}:1')
                    await msg.answer_audio(
                        send_audio(int(msg.text)),
                        caption=f"<b>«{name}» súresi</b> | <b>Mishary Alafasy</b>"
                    )
                else:
                    ans = (
                        "<b>Quranda 114 súre bar.</b>",
                        "Iltimas, 1 den 114 ge deyin bolģan san jazıń."
                    )
                    await msg.reply('\n\n'.join(ans))
            except exceptions.WrongFileIdentifier:
                ans = (
                    "<b>Botta qátelik júz berdi, bul Telegram sheklewleri sebepli júzege keldi.</b>"
                    "<a href='https://telegra.ph/file/895a32ea912dd1409e82f.png'> </a>",
                    "Telegram-da bot arqalı 50 MB kólrmnen kóp bolģan fayl jiberilse"
                    "<a href='https://core.telegram.org/bots/api#sendaudio'>бўлмас экан</a>. "
                    "Bazı súrelerdiń kólemi 50 MB-dan artıp ketedi, sol sebepli qátelik júz berip atır."
                    "<b>Qolaysız jaģday ushın keshirim soraymız ..)</b>"
                )
                await msg.answer('\n\n'.join(ans))
        except ValueError:
            text = ("<b>Bottan paydalanıwda qátege jol qoydıńız, iltimas tuwrı soraw jiberiń.</b>",
                    "Eger botti isletiwge túsinbegen bolsańız, /help ti basıń."
                    )
            await msg.reply("\n\n".join(text))


def send_audio(num):
    if num < 10:
        return f'http://server8.mp3quran.net/afs/00{num}.mp3'
    elif num < 100:
        return f'http://server8.mp3quran.net/afs/0{num}.mp3'
    elif num <= 114:
        return f'http://server8.mp3quran.net/afs/{num}.mp3'
    else:
        return False
