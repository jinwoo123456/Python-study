print(f"{'기본 내장 함수':-^30}")
data1 = list(range(1, 11))
print(data1)
print("len=", len(data1))
print("sum=", sum(data1))
print("max=", max(data1))
print("min=", min(data1))

"""
built-in function 내장함수
:내장 함수는 외부 모듈과 달리 import가 필요하지 않기 떄문에
아무런 설정 없이 바로 사용할 수 있다.
int(), float(), str(), list(), tuple(), dict() 등이 있다.

"""
print(f"{'enumerate()':-^30}")
for i, v in enumerate(data1):
    print(i, v)
print()

data2 = dict(birth=1970, name="홍길동", size="100cm")
for i, v in enumerate(data2):
    print(i, v, data2[v], end=", ")
print()

print(f"{'eval()':-^30}")
print(eval("1+2"))
print(eval("'hi'+'a'"))

print(f"{'sorted()':-^30}")
numbers = (8, 9, 56, 4, 64, 5, 4325, 3, 2, 3, 4, 56, 2)
print(sorted(numbers))

"""
iter() : 반복을 끝낼 값(Sentinel1)을 지정하면 특정 값이 나올때 반복을
    종료하는 함수
    형식: iter(반복가능한 객체, 반복을 끝낼 값)
"""
print(f"{'이터레이터(Iterator)':-^30}")
it = iter([1, 2, 3, 4, 5, 99])
while it:
    row = next(it)
    # 99가 되면 break를 통해 반복문 탈출
    if row == 99:
        break
    print(row, end=", ")
"""위 문장은 더이상 출력할 항목이 없을 경우 next()에서 예외가 발생되면서
실행이 중지됨. 이 부분은 예외처리에서 학습할 예정"""
print("=" * 30)

# 랜덤한 난수 생성 모듈 임포트
import random

count = 0
"""iter()함수를 통해 반복한다. 2가 나올때 까지 계속 반복된다."""
for i in iter(lambda: random.randint(0, 10), 2):
    # 0~10까지의 난수를 출력.
    print(i, end=", ")
    count += 1
else:
    print("\n난수가 2가 생성되어 종료")
print(f"반복 횟수:{count}")
