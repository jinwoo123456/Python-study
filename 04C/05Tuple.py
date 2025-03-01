tu1 = tuple()
tu2 = (1, 2, 3, 4, 5)

# 1개의 항목을 갖는 튜플 생성
tu3 = (1,)
tu4 = (98, 99, 100)
print(tu1, tu2, tu3)

# 인덱싱,슬라이싱

print(f"{'인덱싱/슬라이싱':-^30}")
print("tu2[0]:", tu2[0])
print("tu2[-1]:", tu2[-1])
print("tu2[1:3]:", tu2[1:3])

print(f"{'포함여부확인':-^30}")
print("4 in tu2:", 4 in tu2)
print("99 not in tu2:", 99 not in tu2)

print(f"{'반복출력':-^30}")
print("tu2*3:", tu2 * 3)

print(f"{'병합':-^30}")
new_tu = tu2 + tu4
print("new_tu:", new_tu)
print(f"{'튜플과 리스트 변환':-^30}")
my_list = [1, 2, 3]
my_tuple = ("x", "y", "z")
print(tuple(my_list))
print(list(my_tuple))
