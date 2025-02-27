# 논리연산자
num1 = float(input("첫번째 숫자를 입력하세요:"))  # input값은 문자열로 반환
num2 = float(
    input("두번째 숫자를 입력하세요:")
)  # 그러므로 float로 형변환해야함.# float() : 문자열을 실수로 변환


# 관계연산자
result1 = num1 == num2
print("같은지 비교", result1)

result2 = num1 != num2
print("다른지 비교", result2)

result3 = num1 >= num2
print("큰지 비교", result3)

result4 = num1 < num2
print("작은지 비교", result4)

result = not (num1 > num2)
print("관계식 판단의 부정", result)


logical1 = result1 and result2  # F and T ==> False
logical2 = result3 or result4  # F or T ==> True
logical3 = not (result3 or result4)  # not(Ture) ==> False

print("logical1", logical1)
print("logical2", logical2)
print("logical3", logical3)
