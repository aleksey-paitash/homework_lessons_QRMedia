import requests
from bs4 import BeautifulSoup


# Получить список статей хабра за месяц.
# https://habr.com/top/monthly/

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h2 = soup.find('div', class_="posts_list").find_all('h2')
    for i in h2:
        x = i.text
        print(x)


def main():
    url = "https://habr.com/top/monthly/"
    html = get_html(url)
    get_data(html)
    # print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
