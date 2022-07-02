import requests

symbol = ''
while symbol != 'q':
    print('Type "q" to quit' + '\n')
    symbol = input("Enter a ticker: ").upper()
    symbol2 = input("Enter a second ticker: ").upper()
    print()
    for x in range(20):
        binance = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}{symbol2}')
        ftx = requests.get(f'https://ftx.com/api/markets/{symbol}/{symbol2}')
        if binance.status_code and ftx.status_code == 200:
            bprice = float(binance.json()['price'])
            ftxprice = float(ftx.json()['result']['price'])
            print(f'Binance {symbol}/{symbol2}:', bprice)
            print(f'FTX {symbol}/{symbol2}:', ftxprice)
            prices = [bprice, ftxprice]
            prices.sort()
            print('Price difference: ' + str(round(prices[1] / prices[0] * 100 - 100, 10)) + '%')
            print()
        elif ftx.status_code != 200:
            print(f'FTX doesnt have the ticker {symbol}')
            break
        elif binance.status_code != 200:
            print(f'Binance doesnt have the ticker {symbol}')
            break
