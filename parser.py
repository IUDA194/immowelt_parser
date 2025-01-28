import requests
from bs4 import BeautifulSoup


def parse_flats(url):
    # Получение HTML через requests
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Найти все div с data-testid="cardmfe-description-box-address"
    matching_divs = soup.find_all('div', {'data-testid': 'cardmfe-description-box-address'})

    flats = []

    # Извлечение текста, ссылки и дополнительных данных про каждый адрес
    for idx, div in enumerate(matching_divs, start=1):
        address = div.get_text(strip=True)
        link = div.find_previous('a', href=True)
        link_url = link['href'] if link else 'Ссылка не найдена'

        # Найти родительский элемент для извлечения дополнительных данных
        parent = div.find_parent('div', {'data-testid': 'serp-core-classified-card-testid'})
        price = parent.find('div', {'data-testid': 'cardmfe-price-testid'}).get_text(strip=True) if parent and parent.find('div', {'data-testid': 'cardmfe-price-testid'}) else 'Цена не найдена'
        details = parent.find('div', {'data-testid': 'cardmfe-keyfacts-testid'}).get_text(separator=', ', strip=True) if parent and parent.find('div', {'data-testid': 'cardmfe-keyfacts-testid'}) else 'Детали не найдены'

        # Найти ссылку на первую картинку
        first_image = parent.find('img')
        image_url = first_image['src'] if first_image else 'Ссылка на изображение не найдена'

        flats.append({
            "address": address,
            "link": link_url,
            "price": price,
            "details": details,
            "image_url": image_url
        })

    return flats


