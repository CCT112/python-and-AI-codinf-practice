import random


answer = random.randint(1, 10)
guess = int(input("請猜一個 1 到 10 的數字："))

if guess == answer:
    print("答對了！")
else:
    print(f"正確答案是 {answer}")