"""
    집합(set)
    : 중복되지 않는 요소들이 모인 것
    : 순서가 없다
    : {}를 사용해서 선언
    : 요소를 추가할 때는 add() 메서드를 사용
    : 여러 요소를 추가할 때는 update() 메서드를 사용
    : 요소를 삭제할 때는 remove() 메서드를 사용
    : 모든 요소를 삭제할 때는 clear() 메서드를 사용
    : 집합 연산을 할 때는 |, &, - 연산자를 사용
    :dict와 set의 차이점은 {}를 사용할 때, dict는 key:value
         형태로 사용하고 set은 요소(value)만 사용한다
"""

empty_set = set()
print(empty_set)

even_set = set([0, 2, 4, 6, 8])
print(even_set)

# 중복값 자동 제거
odd_set = {1, 3, 5, 7, 9, 7, 5, 3, 1}
print("중복제거:", odd_set)
print("크기:", len(odd_set))

# 새로운 Set 생성
myset = {1, 3, 5}

# 요소 추가
myset.add(7)
print("myset1:", myset)

# 여러개의 요소 추가
myset.update({4, 6, 8})
print("myset2:", myset)

# 삭제
myset.remove(1)
print("myset3:", myset)


# 모든 요소 삭제
myset.clear()
print("myset4:", myset)

# 집합연산

set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 5}
print("합집합:", set_a | set_b)  # {1,2,3,5,7,9}
print("교집합:", set_a & set_b)  # {1,5}
print("차집합:", set_a - set_b)  # {3,7,9}
