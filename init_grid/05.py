# 선물 현재가 조회
import ccxt

# API 정보 파일 열기
f = open("../binance.key")
lines = f.readlines()
api_key = lines[0].strip()
secret = lines[1].strip()
f.close()

exchange = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

# XRP/USDT Perpetual Last Price
SYMBOL = "XRP/USDT"
xrp = exchange.fetch_ticker(symbol=SYMBOL)
curr_price = float(xrp['last'])
print(curr_price, type(curr_price))

# limit order
GRID_SPACING = 0.04
AMOUNT = 20

# buy
buy_price = curr_price - GRID_SPACING
exchange.create_limit_buy_order(
    symbol=SYMBOL,
    amount=AMOUNT,
    price=buy_price
)

# sell
sell_price = curr_price - GRID_SPACING
exchange.create_limit_sell_order(
    symbol=SYMBOL,
    amount=AMOUNT,
    price=sell_price
)