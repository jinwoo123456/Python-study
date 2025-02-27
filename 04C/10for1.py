# 0~4까지 반복됨
for i in range(5):
    print("i", i, end="")

print()
print("=" * 30)

# for문에 리스트를 사용
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in list1:
    sum += i
print("1부터 10까지의 합 =", sum)

print()
print("=" * 30)

# 문자열의 크기만큼 반복
str1 = "파이썬이좋아요"
for ch in str1:
    print(ch, end="")

print()
print("=" * 30)

# 구구단
for dan in range(2, 10):  # 단은 2~9까지 반복
    for su in range(1, 10):  # 수는 1~9까지 반복
        print("%2d * %2d = %2d" % (dan, su, dan * su), end="  ")
    print()

print()
print("=" * 30)

# 1~100까지의 합
