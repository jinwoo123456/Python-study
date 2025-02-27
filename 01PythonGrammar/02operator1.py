# 산술 연산자
x = 2
y = 4
z = 8
txt = "50"
print("x =", x, "y = ", y)  # x = 2 y = 4
print("x + y ", x + y)  # x + y  6
print("x - y ", x - y)  # x - y  -2
# 나누기 연산 결과는 실수(float)로 반환된다.
print("x * y ", x * y)  # x * y  8
# 몫을 구하기 위한 나누기 연산
print("x / y ", x / y)  # x / y  0.5
print("x % y ", x % y)  # x % y  2
print("x // y ", x // y)  # x // y  0
# 거듭제곱. 즉 x의 y승을 구한다.
print("x ** y ", x**y)  # x ** y  16
# pow() : 파이썬에서 제공하는 기본 함수. 거듭제곱의 결과 반환
print("pow(x , y) ", pow(x, y))  # pow(x , y)  16
# x의 y승의 z로 나눈 나머지를 반환
print(" pow(x , y , z)", pow(x, y, z))  # pow(x , y , z)  16

# x를 y로 나눈 몫과 나머지를 튜플로 반환
print("divmod(x, y)", divmod(x, y))  # divmod(x, y) (0, 2)

"""
수학 관련 여러가지 함수를 가지고 있는 math 모듈을 현재 문서에
import 한 후 팩토리얼 함수를 호출 
"""
import math

# math.factorial() : 팩토리얼 함수
# 팩토리얼 : 1부터 n까지의 정수를 모두 곱한 것
print("math.factorial(5)", math.factorial(5))  # math.factorial(5) 120
