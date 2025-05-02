import random
from datetime import datetime
import math

today = datetime.now().date()
lucky_num = random.randint(1, 99)

# ついでに math を使って“余興”を足す
digit_sum = sum(int(d) for d in str(lucky_num))
root      = round(math.sqrt(lucky_num), 2)

print(f"📅 {today} のラッキーナンバーは {lucky_num}!")
print(f"  ‣ 各桁の合計   : {digit_sum}")
print(f"  ‣ √{lucky_num} ≒ {root}")