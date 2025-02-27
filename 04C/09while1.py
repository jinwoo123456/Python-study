cnt = 0

while 11 > cnt:
    cnt += 1
    print(f"나무가 {cnt}번 찍혔습니다.")
    if cnt == 10:
        print("나무가 넘어갑니다.")
        break

print()
print("=" * 30)

str = "python"
# str이 공백이 될때까지 반복.공백이 아니라면 True
while str:
    # 출력문 끝에 공뱍을 추가하여 줄바꿈없이 출력
    print(str, end="  ")
    """문자열 슬라이싱
    인덱스 1부터 마지막까지 슬라이싱."""
    str = str[1:]


print()
print("=" * 30)


# 시나리오 : 1~10까지의 합을 구하시오,

sum = 0
i = 1
while i <= 10:
    sum += i
    if i < 10:
        print(i, end=" + ")
    else:
        # 반복의 마지막에는 =를 출력
        print(i, end=" = ")
    i += 1
else:
    print(sum)
print()
print("=" * 30)


"""
하루에 판매 가능한 커피 :10잔.
while 무한루프로 커피 전부 판매하면 반복문 탈출,
"""
coffee = 10
while True:
    print("커피 한잔을 판매합니다.")
    coffee -= 1
    print(f"남은 커피는 {coffee}잔 입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break

print()
print("=" * 30)

"""로또번호생성. 1~45까지의 숫자중 6개를 랜덤으로 생성"""

import random

lotto = set()

while True:
    rndNum = random.randint(1, 45)
    lotto.add(rndNum)

    if len(lotto) == 6:
        break
    
    
    
#오름차순으로 정렬

print("로또번호:", sorted(lotto))

# lotto = set(random.randint(1,45) x for x in range(1,7))
