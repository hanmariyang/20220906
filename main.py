from calculator import *

print("숫자를 입력 합니다.")
a = int(input())
print("+, -, *, / 중 원하는 사칙연산을 입력 합니다.")
cal = str(input())
print("숫자를 입력 합니다.")
b = int(input())

if cal == "+" :
    c = plus(a, b)
elif cal == "-" :
    c = minus(a, b)
elif cal == "*" :
    c = multiplied(a, b)
elif cal == "/" :
    c = divided(a, b)

print(f"{a} {cal} {b} = {c}")