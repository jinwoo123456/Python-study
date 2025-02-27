"""
서식문자로 문자열, 정수 ,실수 표현
형식 :
    문자열 : %s
    정수 : %d
    실수 : %f
    변수가 2개 이상일 때 : % (변수1, 변수2, ...)
    자리수 지정 시 : %자리수d, %자리.수f
"""

# 문자열 사용
str = "내 이름은 %s 입니다." % "칸"
print("str=", str)

# 리스트 사용
names = ["유비", "관우", "장비"]
for n in names:
    print("리스트 이름 : %s" % n)


# 정수 사용
money = 10000
str = "마우스 가격은 %d원 입니다." % money
print("str=", str)

# 실수 사용
pi = 3.141592
print("원주율은 %f 입니다." % pi)
print("원주율은 %5.3f 입니다." % pi)

# 변수가 2개 이상일 때
str = "이름 : %s, 나이 : %d" % ("홍길동", 99)
print("str=", str)

# 변수 여러개 초기화
phone, age, height = "010-1234-5678", 20, 180.5
# 여러개를 출력할때는 콤마로 구분하고 괄호로 묶어준다.
str2 = "전화번호:%s, 나이:%d, 키:%.2f" % (phone, age, height)
print("str2=", str2)
