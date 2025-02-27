"""
시나리오 : 1부터 20까지의 숫자중 홀수만 출력하는 프로그램을 작성하시오.
단 continue를 사용하시오
"""

cnt = 0
while cnt < 20:
    cnt += 1
    if not cnt % 2 == 0:
        print(f"{cnt}는 홀수입니다.")
    else:
        continue


print()
print("=" * 30)

""" 시나리오: 구구단 출력"""
dan = 2
while dan <= 9:
    su = 1
    while su <= 9:
        print(f"{dan} * {su} = {dan*su}")
        su += 1
    dan += 1
for i in range(2, 10):

    for ii in range(1, 10):
        print(f"{i} * {ii} =  ", i * ii)
print()
print("=" * 30)

dan = 2
while dan <= 9:
    if dan % 2 == 1:
        dan += 1
        continue
    else:

        su = 1
        while su <= 9:
            print(f"{dan} * {su} = {dan*su}")
            su += 1
    dan += 1
    print()
print()
