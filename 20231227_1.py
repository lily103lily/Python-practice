#TEST1 (if)

hungry = True
if hungry:
    print("im going to eat")

#TEST2 (if else)
rain = False
if rain:
    print("go to work by car")
else:
    print("go to work by walking")

#TEST3 (if elif else)
score = 40
if score == 100:
    print("give u 1000")
elif score >= 80:
    print("give u 500")
elif score >= 60:
    print("give u 100")
else:
    print("give me 300")

#TEST4 (if and)
scores = 40
rainy = False
if scores == 100 and rainy:
    print("give u 10")
else:
    print("u give me 100")

#TEST5
point = 80
sun = False
if point != 100 or sun:
    print("give me 50")
else:
    print("u give me 5")