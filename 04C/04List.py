import random

rndNum = random.randint(6, 10)  # 6~10사이의 랜덤값

list6 = [x for x in range(1, 5)]
list6.append(rndNum)
print("list6:", list6)
list1 = [1, 2, 3, 4, rndNum]
list2 = [
    "java",
    "python",
    "c",
    "c++",
    "c#",
    "ruby",
    "kotlin",
    "swift",
    "scala",
    "groovy",
]
list3 = [10, 20, ["java", "python", "html"]]

# 출력
print("list1:", list1)
print("list2[2]:", list2[2])
print("list3[2]:", list3[2])

# 슬라이싱
print(f"{"슬라이싱":-^30}")
print("list1[1:4]", list1[1:4])
print("list1[:3]", list1[:3])
print(list1[1:], list1[1:])


print(f"{'리스트연결':-^30}")
all_list = [list1, list2]
print("all_list ", all_list)
print("all_list[0]", all_list[1][0])


# 리스트 관련 메소드
print(f"{'리스트 관련 메소드':-^30}")
rndNum = random.randint(11, 20)
list1.append(rndNum)
print(f"append({rndNum})", list1)

list1.clear()
print("clear()", list1)

list1.extend([10, 20, 30, 40, 50])
print("extend()", list1)

list1.extend([10, 20, 30, 40, 50])
print("extend()", list1)
list1.insert(1, 99)
print("insert(1,99)", list1)

print(list1.pop())
print("pop()", list1)

list1.remove(99)
print("remove(99)", list1)

#리스트를 뒤집을때 사용
list1.reverse()
print("reverse()", list1)

del list1[0]
print("0번항목삭제", list1)
