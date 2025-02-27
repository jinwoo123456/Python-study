print(f"{'if문 첫번째 형식':-^30}")
a, b, c, str = 10, 20, 30, "Python"


# != 같지 않다
if a != b:
    print("a는 b와 다르다.")

# <= 같다
if a <= c:
    print("a는 c보다 작거나 같다.")
# 문자열 자체를 조건으로 사용하면 True가 된다. 단 빈 문자열은 False
# 자바는 문자열은 ture가 아니다.
if str:
    print("문자열은 True를 한다.")

# if a str:  # 에러 발생
# print("문자열과 정수는 비교의 대상이 될 수 없다.")

print(f"{'if문 두번째 형식':-^30}")  # -^30은 30개의 -로 중앙정렬

if not a > b:  # not은 False를 True로, True를 False로 바꾼다.
    print("a는 b보다 크지 않습니다.")
else:
    print("a는 b보다 큽니다.")

if a and b != c:  # and는 모든 조건이 True일때 True
    print("모든 조건을 만족합니다.")
else:
    print("조건 중 False가 있습니다.")

if a or b < c:  # or은 하나의 조건이 True일때 True
    print("조건 중 True가 있습니다.")
else:
    print("모든 조건에 만족하지 않습니다.")

print(f"{'if문 세번째 형식':-^30}")

age = 33
print(age, "실은 ", end="")


"""
    자바에서는 else- if
    파이썬에서 elif
    """
if age >= 35:
    print("중년입니다.")
elif age >= 30:
    print("중년의 시작입니다.")
else:
    print("청년입니다.")
