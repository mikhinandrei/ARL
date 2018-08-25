import requests
from lxml.html import fromstring
import pandas as pd


def get_data():
    URL = 'https://ru.wikipedia.org/wiki/Частоты_настройки_фортепиано'
    r = requests.get(URL)
    t = r.text.replace("br", "/").encode('utf-8')
    list_doc = fromstring(t)

    tbl = list_doc.cssselect('table')[1]
    notes = [x.text.strip() for x in tbl.cssselect('td')[2::4]]
    freqs = [float(x.text.strip().replace(',', '.')) for x in tbl.cssselect('td')[3::4]]
    pd.DataFrame({'notes': notes, 'freqs': freqs}).to_csv('../data/data.csv')


def load_data(path):
    df = pd.read_csv(path)
    return dict(zip(df.freqs, df.notes))