import requests


def get_data(inp):
    sp = inp.split(":")
    url = f"https://quranenc.com/api/v1/translation/aya/uzbek_mansour/{sp[0]}/{sp[1]}"
    r = requests.get(url)
    res = r.json()
    if r.status_code == 404:
        return False
    else:
        output = {}
        number = res['result']['id']
        output['text'] = res['result']['arabic_text']
        output['number_in_surah'] = res['result']['aya']
        output['footnotes'] = res['result']['footnotes']
        output['image_url'] = f"https://cdn.islamic.network/quran/images/{sp[0]}_{sp[1]}.png"
        output['audio'] = f"https://cdn.islamic.network/quran/audio/128/ar.alafasy/{number}.mp3"
        return output
