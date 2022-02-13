import requests
from bs4 import BeautifulSoup
import re

URL = 'https://kwork.ru/projects?c=15'
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         "Chrome/83.0.4103.106 Safari/537.36", "accept": "*/*"}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_categories(html):
    bs = BeautifulSoup(html, 'html.parser')
    c_items = bs.find_all('div', class_='js-sub-category-wrap ')
    categories = []

    for item in c_items:
        a = item.find('div', class_='').get_text()
        print(a)
        categories.append(a)

    return categories


def get_content(html):
    bs = BeautifulSoup(html, 'html.parser')
    r_items = bs.find_all('div', class_='card__content pb5')
    exclude = r'[^А-Яа-яA-Za-z0-9іІєЄёЁїЇ\'"!?@<>#:;`~@№$%^&*()\/.,\-+_=]'
    results = []

    for item in r_items:
        title = item.find('div', class_='wants-card__header-title first-letter breakwords').find_next('a').get_text()
        title = re.sub(exclude, ' ', title)

        descrip = item.find('div', class_='breakwords first-letter js-want-block-toggle'
                                              ' js-want-block-toggle-full hidden')
        if descrip:
            descrip = descrip.get_text()[:-6]
        else:
            descrip = item.find('div', class_='wants-card__description-text br-with-lh').get_text()
        descrip = re.sub(exclude, ' ', descrip)

        status = item.find('div', class_='query-item__info mb10 ta-left').get_text()
        status = re.sub(exclude, ' ', status).replace('  ', '\n')

        price = item.find('div', class_='wants-card__header-price wants-card__price m-hidden').get_text()
        price = re.sub(r'\D', '', price) + ' руб.'
        results.append({
            'title': title,
            'description': descrip,
            'price': price,
            'status': status,
            'link': item.find('div', class_='wants-card__header-title '
                                            'first-letter breakwords').find_next('a').get('href')
        })
    return results


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        results = []
        html = get_html(URL)
        categories = get_categories(html.text)
        pages_count = 1
        for page in range(1, pages_count + 1):
            print(f"{page}/{pages_count} pages is processed...")
            html = get_html(URL, params={"page": page})
            results.extend(get_content(html.text))
    else:
        print("Error. Status code: ", html.status_code)

    print(categories)
    for i in results:
        print(i)
        print('-----------------------------------------------------------')


parse()
