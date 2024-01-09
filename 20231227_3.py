#if 建立一個計算機

no1 = float(input("請輸入第一個數字："))
op = input("請輸入運算符號：")
no2 = float(input("請輸入第二個數字："))


if op == "+":
    print(no1+no2)
elif op == "-":
    print(no1-no2)
elif op == "*":
    print(no1*no2)
elif op == "/":
    print(no1/no2)
else:
    print("不支援的運算")