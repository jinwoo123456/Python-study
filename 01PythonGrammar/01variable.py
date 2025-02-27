a = "Hello Python"

print(a, id(a))  # 메모리 주소값을 출력

a = 100
print(a, id(a))  # 메모리 주소값을 출력
print("한줄에.")
print("여러개 명령어를 쓰려면")
print("세미콜론(;)을 사용하면 됩니다.")


# 정수형

i = 200
print(i, type(i))  # type() 함수를 사용하여 변수의 타입을 확인할 수 있다.

# 실수형
i = 3.14

print(i, type(i))

# bool형
i = True
print(i, type(i))

# 문자형

i = "안녕"


# 변수와 할당을 여러개 할때는 콤마(,)를 사용한다.
r, g, b = "Red", "Green", "Blue"

print(r, g, b)
print(i, type(i))

if __name__ == "__main__":

    pass
