#1~10까지의 수열의 합을 계산하여 출력하는 함수

def sum1To10():
    sum = 0
    for i in range(1, 11):
        sum += i
    print("1부터 10까지의 합 : ", sum)
