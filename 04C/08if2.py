print(f"{'중첩된 fi문':-^30}")
num1 = int(input("숫자 하나를 입력하세요:"))

if num1 % 2 == 0:
    if num1 % 3 == 0:
        print("2와 3으로 나누어 떨어집니다.")
    else:
        print("2는 가능, 3은 불가능")
else:
    if num1 % 3 == 0:
        print("2는 불가능, 3은 가능")
    else:
        print("2와 3 모두 불가능")

print(f"{'삼항연산자':-^30}")

# 삼항연산자
number = 99
result = "100보다 크다 " if number > 100 else "100보다 작다"
print(result)

print("3의 배수") if number % 3 == 0 else print("3의 배수가 아니다")

print(f"{'if~in문':-^30}")
countryList = ["한국", "미국", "일본", "중국", "영국", "보라카이", "필리핀"]
journey = input("여행을 가고 싶은 나라를 입력하세요:")
if journey in countryList:
    print(print("{}은 여행지 목록에 있습니다.".format(journey)))
else:
    print("{}은 여행지 목록에 없습니다.".format(journey))
