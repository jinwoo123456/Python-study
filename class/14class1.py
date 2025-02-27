class Person:
    # 생성자 메서드. 첫번째 매개변수로 클래스 자신을 가리키는 self를 기술.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"이름 : {self.name}")
        print(f"이름 : {self.age}")

    def justDoIt(self, act):
        print(f"{self.name} 님이 {act} 을(를) 합니다.")

    # java의 toString과 동일
    def __str__(self):
        return f"제 이름은 {self.name}({self.age}) 입니다."


# 인스턴스 생성. new를 붙이지 않는다.
person1 = Person("박찬호", 30)
person2 = Person("손흥민", 28)

person1.showInfo()
person1.justDoIt("야구")

print(person2)
person2.justDoIt("축구")

print(person1)
