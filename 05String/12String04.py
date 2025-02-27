"""
뮨저욜 바꾸기

    replace() : 문자열에서 특정 문자열을 다른 문자열로 바꾸기
    maketrans() : 문자열에서 특정 문자를 다른 문자로 바꾸기 위한 변환 테이블을 만듭니다.
"""

print(f"{'replace()':-^30}")
print("Hello, world!".replace("world", "Python"))

s = " Hello, world! "
s = s.replace("Hello", "안녕")
print(s)

"""문자바꾸기
: maketrans('바꿀문자', '새문자') -> 테이블 생성 후
 translate(테이블)로 적용한다.

"""

print(f"{'maketrans()/translate()':-^30}")
str1 = "apple"
table = str1.maketrans("aeiou", "12345")
print(str1.translate(table))

# 한아언이 XYZ로 각각 변경된다.
str2 = "한글은 아름다운 언어"
table = str2.maketrans("한아언", "123")
print(str2.translate(table))

"""문자열 연결
리스트로 주어진 요소들을 특정 구분자를 통해 연결한다.
"""
print(f"{'join()':-^30}")
print("-".join(["010", "1234", "5678"]))

"""공백삭제 혹은 특정 문자 삭제
: lstrip() : 왼쪽 공백 삭제
: rstrip() : 오른쪽 공백 삭제
: strip() : 양쪽 공백 삭제
"""
print(f"{'strip()':-^30}")
str = "#^%오늘은 @@ 파이썬 @@ 공부하는날 #^$%"
print(str.strip("#"))
print(str.strip("%"))
print(str.strip("%").lstrip("#").replace("@", ""))
"""열 위치 찾기
    find(왼쪽부터), rfind(오른쪽부터) : 문자열에서 특정 문자열의 위치를 찾는다.
    인덱스를 반환함.
"""
print(f"{'find()':-^30}")
print("apple pineapple".find("pl"))
print("apple pineapple".rfind("p1"))

"""문자열 상세검사
isalnum():문자열에서 숫자,알파벳,한글만 있는 경우 True,
그 외 문자가 포함되어 있다면 False를 반환.
"""
print(f"{'isalnum()':-^30}")
str = "python312좋아"
print(str.isalpha())
str = "python3.12좋아^^"
print(str.isalnum())

"""
시나리오 : 입력한 문자열에 영문대문자, 소문자 ,숫자만 포함되어 있다면 True, 
문자가 하나라도 ㅍ함되면 False를 출력하시오
"""
print(f"{'시나리오':-^30}")
s = input("문자열 입력 : ")
result = True
for char in s:
    #문자를 하나씩 검사한다.
    if not (char.isupper() or char.islower() or char.isdigit()):

        print("False")
        #대문자,소문자,숫자가 아닌 경우 False를 할당
        result = False

print(f"입력한 문자열 : {s}")
print(f"결과 : {result}")

"""문자열 분리"""
