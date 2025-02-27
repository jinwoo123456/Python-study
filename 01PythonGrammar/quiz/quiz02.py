"""
result = int(input("소수를 구할 정수 한개 입력:"))
print(result)
result_list = [x for x in range(1, result + 1)]
cnt2 = 0
for i in result_list:
    cnt = 0
    for ii in result_list:
        if i % ii == 0:
            cnt += 1
    if cnt == 2:
        cnt2 += 1
        print(f"{i}(은/는) 소수이다.")

print(f"1~{result} 사이의 소수 개수={cnt2}")

"""


def pale(result):
    a = result[-1]
    print(a)
    b = result[0]
    print(b)
    true = ""
    false = ""
    if a == b:
        true = "펠릭스어쩌구문자입니다~"

    else:
        false = "펠릭어쩌꾸문자아닙니다~"
    return true if a == b else false


if __name__ == "__main__":
    result = input("문자열 입력")
    print(pale(result))
