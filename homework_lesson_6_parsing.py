import requests

# Задание 1.
print('Задание 1. Курс валют.')
# Получить курс нескольких валют за текущую дату.

# "Cur_ID": 170,
# "Date": "2019-07-13T00:00:00",
# "Cur_Abbreviation": "AUD",
# "Cur_Scale": 1,
# "Cur_Name": "Австралийский доллар",
# "Cur_OfficialRate": 1.4217

def main():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    text = requests.get(url).json()
    for i in text:
        print(f" Курс валют: за 1 {i['Cur_Name']}  {i['Date'].split('T')[0]} числа, Вы заплатите {i['Cur_OfficialRate']} BYN")


if __name__ == '__main__':
    main()