import requests


def get_sura_name(inp):
    url = f"https://api.alquran.cloud/v1/ayah/{inp}/editions/quran-uthmani,uz.sodik"
    r = requests.get(url)
    res = r.json()
    return res['data'][1]['surah']['englishName']
