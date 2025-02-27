
'''
format() 함수를 사용한 문자열 포맷팅
: 문자열 포멧팅은 문자열 내에 특정한 값을 삽입하는 방법을 말한다.
서식 문자보다 더 간단히 문자를 표현할 수 있다.
{}(중괄호)안에 포메팅을 지정하고 format() 함수를 사용하여 값을 삽입한다.
형식:
 '{인덱스}'.format(값 혹은 변수)
'''
str1 = "name : {0}".format("홍길동")
print(str1)

age = 55
str2 = "age : {0}".format(age)
print(str2)

str3 = "name : {name}, age : {age}".format(name="홍길동", age=33)
print(str3)

str4 = " 이름 : {}, 나이 : {}".format("이순식", 44)
print(str4)

str5 = "나이 : {1}, 이름 : {0}".format("이성계", 55)
print(str5)

str6 = "항목1 : {0}, 항목2 : {1}, 항목3 : {2}".format("사과", "바나나", "포도")
print(str6)

str7 = "정수3자리 : {0:03d}, {1:03d}".format(12345, 12)
print(str7)

str8 = "소수점 아래 2자리 : {0:0.2f},소수점 아래 5자리 : {1:0.5f}".format(
    3234.141592, 3.141592
)
print(str8)

str9 = "{{{0}}}".format("python 중괄호 표현")
print("str9=", str9)

str10 = 1592000
print(format(str10, ","))
