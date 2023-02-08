
from keys import API_KEY, SECRET_KEY
from binance.um_futures import UMFutures
from time import sleep

client = UMFutures(key=API_KEY, secret=SECRET_KEY)  # Binance API
symbol = 'XRPUSDT'

last_price = float(client.ticker_price(symbol)["price"])  # We get the value of the latest futures since launch
max_price = last_price

while True:
    if ((max_price - last_price) / max_price * 100) >= 1:  # We find the difference in percentages
        print(f'The price decreased by  1%\nLast price 1 XRP : {last_price} $')
    sleep(60)  # updating data
    last_price = float(client.ticker_price(symbol)["price"])
