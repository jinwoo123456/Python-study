print(f"{'2개 이상의 반환값을 가진 함수':-^30}")


def min_max(num):
    sum = 0
    for val in num:
        sum += val
    return sum, min(num), max(num)


numbers = (8, 7, 6, 8, 5, 4, 9, 5)
sumval, minval, maxval = min_max(numbers)

print("튜플의합,최댓값,최소값: ", sumval, minval, maxval)

print(f"{'지역변수와 전역변수':-^30}")
total = 0


def sum(arg1, arg2):
    # 함수의 지역변수로 정의
    total = arg1 + arg2
    # 전역변수와 지역변수가 충돌되면 지역변수가 항상 우선순위가 높다.
    print("지역변수 total= ", total)
    # 이 변수는 함수를 벗어나면 메모리에서 소멸됨.
    return total


# 초기값 0이 그대로 출력됨
print("전역변수 total= ", total)
# 함수 ㅎ출 후 반환값은 30 출력됨.
print("sum(10,20)호출 후 반환값= ", sum(10, 20))

print(f"{'내부함수':-^30}")


# 외부함수로 정의
def person(name, age):
    # 내부함수로 정의
    def myName(n):
        print("이름:%s" % n)

    def myAge(a):
        return "나이:%s" % a

    # 내부함수 호출
    myName(name)
    print(myAge(age))


# 외부함수를 호출하면 전달된 인수는 내부함수로 전달되어 결과 출력됨.
person("성유겸", 13)
print(f"{'매개변수1 : 순서 매개변수':-^30}")


# 함수에서 사용하는 가장 일반적인 매개변수로 작성 순서대로 적용됨.
def paramFunc1(str1, str2):
    print(str1, str2)
    return


cont = "은 매우 좋은 프로그램입니다."
paramFunc1("Python", cont)

print(f"{'매개변수2 : 키워드 매개변수':-^30}")


# 매개변수명을 그대로 사용하여 값을 전달. 따라서 순서를 변경할 수 있음.
def paramFunc2(name, age):
    print("이름:", name)
    print("나이:", age)
    return


paramFunc2(name="홍길동", age=33)


print(f"{'매개변수3 : 디폴트 매개변수':-^30}")


# 매개변수로 값이 전달되지 않는 경우 디폴트값을 지정하는 방식.
def paramFunc3(lan="Java"):
    print("내가 좋아하는 언어는", lan, "입니다.")
    return


paramFunc3()  # 인수가 없으므로 JAVA가 출력
paramFunc3("RUST")  # RUST 출력

print(f"{'매개변수4 : 가변 매개변수(튜플)':-^30}")


# *args는 튜플이 되어 여러 값(인수)을 저장하게 된다.
def paramFunc4(*args):
    print("*args=>", args)
    result = 1
    # 튜플이므로 반복 가능
    for a in args:
        # 누적해서 곱한 결과 반환.
        result *= a
    return result


print("결과=>", paramFunc4(1, 2, 3, 4, 5))

print(f"{'매개변수5 : 가변 매개변수(딕셔너리)':-^30}")


def paramFunc5(**man):
    # 딕셔너리 형태로 출력
    print("**man", man)
    # 딕셔너리이므로 Key와 Value를 출력
    for key in man:
        print(key, " => ", man[key])


paramFunc5(의인="홍길동", 장군="이순신", 임금="세종대왕", 대통령="박정희")
