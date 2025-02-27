# 표준 입출력 장치

i, j, k = 7, 8, 9

# 출력값 사이에 스페이스 하나씩 추가. => 7 8 9
print(i, j, k)
# sep : 출력값 사이에 구분자를 추가. => 7-8-9
print(i, j, k, sep="-")
# 값을줄바꿈없이출력 => 7, 8, 9
print(i, end=", ")
print(j, end=", ")
print(k)

# format() 함수 => 원주율 =   3.142
print("원주율 =", format(3.14159, "8.3f"))
# => 맥주      5000
print("맥주", format(5000, "10d"))
# => 노트북 1,580,000
print("노트북", format(1580000, "3,d"))

# 서식문자 => 이름: 성유겸, 나이: 13, 가격: 123.46'
# 서식문자 : 문자열(%s), 정수(%d), 실수(%f)
name = "성유겸"
age = 13
price = 123.456
print("이름: %s, 나이: %d, 가격: %.2f" % (name, age, price))

menu1 = "치킨"
menu2 = "맥주"
# format()함수 => 오늘 저녁은 치킨과 맥주이다.
print("오늘 {str}은 {0}과 {1}이다.".format(menu1, menu2, str="저녁"))
# => 오늘은 치킨과 맥주로 아침을 시작하겠다.
print("오늘은 {}과 {}로 {str}을 시작하겠다.".format(menu1, menu2, str="아침"))

# 입력받기 : 키보드를 통해 입력받는 값은 항상 '문자형(str)'이 된다.
num = input("숫자를 입력하세요: ")
print("입력한 숫자는", num, "이고, 타입은", type(num), "이다.")

# 문자+숫자 => 에러발생
# result_error = num + 10
# 연산을 위해 정수형으로 변환 후 처리할 수 있다.
result1 = int(num) + 10
print("덧셈결과:", result1)

# 입력 및 정수변환 : 일반적으로 동시에 처리
result2 = int(input("숫자1 : ")) * int(input("숫자2 : "))
print("곱셈결과:", result2)

# 실수변환
result3 = float(input("원주율 : ")) * (float(input("반지름 : ")) ** 2)
print("원의넓이", result3)
