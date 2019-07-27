import requests
import misc_bot
from bs4 import BeautifulSoup

token = misc_bot.token  # name_bot = Aleksey_test_ORmedia_bot

URL = "https://api.telegram.org/bot" + token + "/"
global last_id
last_id = 0
code_id = {'AUD': 170, 'BGN': 191, 'UAH': 290, 'DKK': 291, 'USD': 145, 'EUR': 292, 'PLN': 293, 'IRR': 303,
           'ISK': 294, 'JPY': 295, 'CAD': 23, 'CNY': 304, 'KWD': 72, 'MDL': 296, 'NZD': 286, 'NOK': 297,
           'RUB': 298, 'XDR': 299, 'SGD': 119, 'KGS': 300, 'KZT': 301, 'TRY': 302, 'GBP': 143, 'CZK': 305,
           'SEK': 306, 'CHF': 130}


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_id
    if last_id != current_update_id:
        last_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {'chat_id': chat_id, 'text': message_text}

        return message

    return None


def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def kurs(pw_id):
    url = "http://www.nbrb.by/API/ExRates/Rates/" + str(pw_id)
    html = requests.get(url).json()
    money = "Сегодня 1 {} стоит {} BYN".format(str(html["Cur_Abbreviation"]), str(html['Cur_OfficialRate']))
    return money


def kurs_date(id, text):
    try:
        code_id = self.code_id
        abb = code_id[(text.split('_')[0])[1:4].upper()]  # /usd
        date = text.split('_')[1]  # 2016-5-5
        url = "http://www.nbrb.by/API/ExRates/Rates/" + str(abb) + "?onDate=" + str(date)
        html = requests.get(url).json()
        kurs_date = "{} числа 1 {} имел курс {} BYN".format(date, str(html["Cur_Abbreviation"]),
                                                            str(html['Cur_OfficialRate']))
        return kurs_date
    except:
        send_message(id, 'даты нет в базе')


def anekdot():
    url = "https://nekdo.ru/random/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    anek = soup.find('div', class_="text").text
    return anek


def pogoda():
    url = 'https://yandex.by/pogoda/minsk'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    pogoda = soup.find('div', class_="fact__temp-wrap").find('span', class_="temp__value").text
    return pogoda


def main():
    while True:
        answer = get_message()

        if answer != None:
            id = answer['chat_id']
            text = answer['text']
            if text == '/help':
                send_message(id, '/help - помощь\n/kurs - курс валют\n/kurs_date - курс валют на дату'
                                 '\n/anekdot - посмеемся Вместе\n/afisha - фильмы в прокате\n/pogoda - погода в минске')
            if text == '/kurs':
                send_message(id, '/aud  -  австралийский доллар\n/bgn  -  болгарский лев\n/uah  -  гривня\n'
                                 '/dkk  -  датские кроны\n/usd  -  доллар сша\n/eur  -  евро\n/pln  -  злоты\n'
                                 '/irr  -  иранские риалы\n/isk  -  исландские кроны\n/jpy  -  йен\n'
                                 '/cad  -  канадский доллар\n/cny  -  китайский юань\n/kwd  -  кувейтский динар\n'
                                 '/mdl  -  молдавский леев\n/nzd  -  новозеландский доллар\n/nok  -  норвежский крон\n'
                                 '/rub  -  российский рубль\n/xdr  -  сдр (специальные права заимствования)\n'
                                 '/sgd  -  сингапурcкий доллар\n/kgs  -  сом\n/kzt  -  тенге\n/try  -  турецкий лир\n'
                                 '/gbp  -  фунт стерлингов')
            if text[1:4].upper() in code_id and len(text) == 4:
                pw_id = code_id[text[1:4].upper()]
                send_message(id, kurs(pw_id))
            if text == '/kurs_date':
                send_message(id, 'Укажите дату формата: /валюта_год-месяц-день,\nнапример: "/usd_2016-5-21". '
                                 'Если дата указана неверно,\nвозвращает курс на текущий момент.')
            if (text.split('_')[0])[1:4].upper() in code_id and len(text) >= 13:
                send_message(money_on_date(id, text))
            if text == '/pogoda':
                send_message(pogoda(id))

            # else:
            #     send_message(id, 'Пожалуйста, Введите команду правильно.')
        else:
            continue


if __name__ == '__main__':
    main()
