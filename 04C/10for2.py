"""
시나리오 : 1~100사이의 정수 중 3의 배수의 합을 구하시오.
"""

total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
        print(i, end="+")
print("\b", "=", total)

print()
print("=" * 30)

"""리스트 컴프리헨션
"""

#
list = [n**2 for n in range(10) if n % 3 == 0]
print(list)

print()
print("=" * 30)


