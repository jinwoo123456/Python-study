"""
퀴즈1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
"""

kor = int(input("국어 점수를 입력하세요:"))
eng = int(input("영어 점수를 입력하세요:"))
math = int(input("수학 점수를 입력하세요:"))

avg = (kor + eng + math) / 3

if avg >= 90:
    print("A학점")
elif avg >= 80 and 90 > avg:
    print("B학점")
elif avg >= 70 and 80 > avg:
    print("C학점")
elif avg >= 60 and 70 > avg:
    print("D학점")
elif 60 < avg:
    print("F학점")
"""
퀴즈2] 아이디를 먼저 입력받은 후 user_info 리스트에
등록되었다면 패스워드를 입력받아 일치하는지 확인하는 
프로그램을 작성하시오. 여기서 패스워드는 1234로 가정합니다. 
"""

id = input("아이디를 입력하세요:")
password = input("패스워드를 입력하세요:")
user_info = [id, "1234"]

if user_info[1] == password:
    print("패스워드가 일치합니다.")
