#函式 FUNCTION
#程式由上往下執行
#遇到return會停止

#def：定義
def hello(name, age):
    print("hello!" + name + "你今年" + age + "歲")

hello("LILY", "20")


#TEST1
def add(no1, no2):
    print(no1 + no2)

add(1,2)  #=3

#TEST2
def add1(no3, no4):
    return no3 + no4

print(add1(3,4))  #=7

#TEST3
def add2(no5, no6):
    print(no5 + no6)
    return 10

value = add2(5,6)  #=11
print(value)  #=10

#TEST4
def add3(no7, no8):
    print(no7 + no8)

value = add3(7,8)  #15
print(value)  #none