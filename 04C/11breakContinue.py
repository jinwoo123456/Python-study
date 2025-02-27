repeat = 0

while True:
    repeat += 1
    num = int(input("2의 배수가 아니고 7의 배수인 정수찾기 : \n 정수를 입력하세요:"))
    if num % 2 == 0:
        print(f"입력한 {num}은 2의 배수이므로 계속합니다. ")
        continue
    elif num % 7 == 0:
        print(f"입력한 {num}은 7의 배수이므로 종료합니다.")
        break
    else:
        print("2와 7의 배수가 아니면 계속합니다.")
print(f"전체반복횟수 : {repeat}회")


n = 4
for i in range(1, 5):
    for j in range(1, 5):

        if i + j == 5:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
print("=" * 30)
