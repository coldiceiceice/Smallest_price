# The program reads the current price of the XRP/USDT futures on the Binance exchange.
# If the price has fallen by 1% from the maximum price in the last hour since the start
# of work, the program displays the message
# To the console. At the same time, the program continues to work further, constantly
# reading the current price.

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
