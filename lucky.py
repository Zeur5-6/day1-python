import random
from datetime import datetime
import math
import sys, os

today = datetime.now().date()
while True:
    raw = input("1~99の任意の数字を入力▶")
    try:
        lucky_num = int(raw)
        if not 1 <= lucky_num <= 99:
            raise ValueError
        break
    except ValueError:
        print("ちゃんとやれ")
        sys.exit(1)

# ついでに math を使って“余興”を足す
digit_sum = sum(int(d) for d in str(lucky_num))
root      = round(math.sqrt(lucky_num), 2)

print(f"📅 {today} のラッキーナンバーは {lucky_num}!")
print(f"  ‣ 各桁の合計   : {digit_sum}")
print(f"  ‣ √{lucky_num} ≒ {root}")


with open("log.txt", "a", encoding="utf-8")as f:
    f.write(f"{today},{lucky_num}\n")

if os.path.exists("log.txt"):
    with open("log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()[-5:]      # 後ろから5行スライス
    print("\n🗒 直近の履歴")
    for line in lines:
        print("・" + line.strip())