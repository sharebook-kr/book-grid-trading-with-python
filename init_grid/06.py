# 초기 그리드 설정
import ccxt
import time

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
GRID_SPACING = 0.02     # 그리드 간격
GRID_NUMBER = 3         # 그리드 수 (한쪽 방향 기준)
AMOUNT = 20

for i in range(GRID_NUMBER):
    # buy
    buy_price = curr_price - ((i+1) * GRID_SPACING)
    exchange.create_limit_buy_order(
        symbol=SYMBOL,
        amount=AMOUNT,
        price=buy_price
    )

    # sell
    sell_price = curr_price + ((i+1) * GRID_SPACING)
    exchange.create_limit_sell_order(
        symbol=SYMBOL,
        amount=AMOUNT,
        price=sell_price
    )

    # 지정가 주문 후 0.5초 대기
    time.sleep(0.5)