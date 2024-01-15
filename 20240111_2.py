#猜數字遊戲

no = 77
guess = None

while no != guess:
    guess = int(input("請輸入數字"))

    if guess > no:
        print("小一點")
    elif guess < no:
        print("大一點")

        print("恭喜答對!")