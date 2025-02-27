"""

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1

"""

totcnt = 4
cnt = 4
for x in range(1, 5):
    cnt -= 1
    for y in range(1, 5):
        if x == y:
            print(" 0 " * cnt, "1", end=" ")
            if not totcnt == cnt:
                print(" 0 " * (totcnt - cnt - 1), end="")

    print()


n = 4
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
print("=" * 30)
