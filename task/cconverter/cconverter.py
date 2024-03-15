import requests
import json

# number_coin = float(input())
# exchange_rate = {'RUB': 2.98, 'ARS': 0.82, 'HLN': 0.17, 'AUD' : 1.9622, 'MAD': 0.208}
#
# print(f'I will get {round((exchange_rate["RUB"] * number_coin),2)} RUB from the sale of {number_coin} conicoins.')
# print(f'I will get {round((exchange_rate["ARS"] * number_coin),2)} ARS from the sale of {number_coin} conicoins.')
# print(f'I will get {round((exchange_rate["HLN"] * number_coin),2)} HNL from the sale of {number_coin} conicoins.')
# print(f'I will get {round((exchange_rate["AUD"] * number_coin),2)} AUD from the sale of {number_coin} conicoins.')
# print(f'I will get {round((exchange_rate["MAD"] * number_coin),2)} MAD from the sale of {number_coin} conicoins.')

# currency_code = input()
# adress = f'http://www.floatrates.com/daily/{currency_code.lower()}.json'
# r = requests.get(adress).json()
# print(r.get('usd'))
# print(r.get('eur'))

my_currency = input()
address = f'http://www.floatrates.com/daily/{my_currency.lower()}.json'
r = requests.get(address).json()
if my_currency.lower() != 'usd':
    usd_rate = r.get('usd')
    usd_rate = usd_rate.get('rate')
if my_currency.lower() != 'eur':
    eur_rate = r.get('eur')
    eur_rate = eur_rate.get('rate')

cache = ['usd', 'eur']
while True:

    wanted_currency = input().lower()
    if wanted_currency == '':
        break
    money_to_exchange = float(input())

    address1 = f'http://www.floatrates.com/daily/{my_currency}.json'
    r = requests.get(address1).json()
    rate = r.get(wanted_currency)
    rate1 = rate.get('rate')

    print("Checking the cache...")
    if wanted_currency not in cache:
        print('Sorry, but it is not in the cache!')
        print(f'You received {round((money_to_exchange * rate1),2)} {wanted_currency.upper()}.')

    else:
        print('Oh! It is in the cache!')
        print(f'You received {round((money_to_exchange * rate1), 2)} {wanted_currency.upper()}.')
    cache.append(wanted_currency)