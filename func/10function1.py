"""
함수
형식: 
def 함수명(매개변수1, 매개변수2):
    실행구문
    return 결과1, 결과2
return문은 경우에 따라 생략 가능.
"""

print(f"{'함수 정의 및 호출':-^30}")


def sumTen():
    sum = 0
    for i in range(1, 11):
        sum += i
    print("1~10까지의 합:", sum)


sumTen()

print(f"{'함수 정의 및 응용':-^30}")


def menu():
    print("메뉴 중 숫자를 선택하세요:")
    print("1.덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈")
    print("5. 종료")
    return input("번호 선택 : ")


def add(a, b):
    print(a, " + ", b, " = ", a + b)


def sub(a, b):
    print(a, " - ", b, " = ", a - b)


def mul(a, b):
    print(a, " * ", b, " = ", a * b)


def div(a, b):
    print(a, " / ", b, " = ", a / b)


choice = 0

while True:
    choice = int(menu())
    if choice == 1:
        add(int(input("덧셈 a = ")), int(input("b = ")))
    elif choice == 2:
        sub(int(input("뺄셈 a = ")), int(input("b = ")))
    elif choice == 3:
        mul(int(input("곱셈 a = ")), int(input("b = ")))
    elif choice == 4:
        div(int(input("나눗셈 a = ")), int(input("b = ")))
    elif choice == 5:
        break
print("연산 종료!")
