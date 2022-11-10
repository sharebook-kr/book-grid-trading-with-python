# API 정보 파일 열기
f = open("../binance.key")
lines = f.readlines()
f.close()

print(lines)