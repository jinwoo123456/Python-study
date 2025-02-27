"""
문제 1: 숫자의 합 구하기
사용자로부터 양의 정수 2개를 입력받아 각 자릿수의 합을 계산하는 함수를 작성하세요.

"""


def sum(result, result2):

    list1 = []
    list2 = []
    list_sum = []
    for char in result:

        list1.append(int(char))

    for char2 in result2:

        list2.append(int(char2))

    while True:
        temp = []
        if list1 == temp:
            break
        if list2 == temp:
            break
        sum = list1[-1] + list2[-1]
        del list1[-1]
        del list2[-1]
        list_sum.append(sum)

    return list_sum


if __name__ == "__main__":
    result = input("값을 입력하세요 1 :")
    result2 = input("값을 입력하세요 2 :")
    abc = sum(result, result2)
    abc.reverse()
    print(abc)
