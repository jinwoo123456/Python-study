"""
클래스 변수와 정적 메서드
: class를 통해 생성되는 인스턴스에는 멤버변수와 멤버메서드가 포함된다.
하지만 클래스변수와 정적메서드는 인스턴스 내부에 존재하지 않고 별도의
메모리에 독립적으로 생성된다. 따라서 2개 이상의 인스턴스를 생성하더라도
딱 하나만 생성되어 모든 인스턴스가 공유하게된다
java에서 static과 동일한 개념이다.
"""


class MyCalculator:
    # 클래스 변수: 클래스 전체에서 공유됨. 딱 하나만 생성됨.
    calCount = 0

    def __init__(self, first, second):
        # 인스턴스 변수: 생성된 인스턴스마다 존재함
        self.first = first
        self.second = second

    # 인스턴스 메서드(멤버 메서드)
    def calculate(self, symbol):
        # 클래스 변수 사용: 연산 횟수 증가
        # 클래스 명을 통해 정적변수에 접근하여 1 증가.
        MyCalculator.calCount += 1

        if symbol == "+":
            result = self.first + self.second
        elif symbol == "-":
            result = self.first - self.second
        elif symbol == "*":
            result = self.first * self.second
        elif symbol == "/":
            result = self.first / self.second
        else:
            result = "잘못된 연산 기호입니다."
        return result

    def __str__(self):
        # 클래스 정보 문자열로 반환
        result = f"계산기 클래스입니다.\nfirst={self.first}, second={self.second}"
        return result

    @staticmethod
    def otherNumMulti(refCls, otherNum):
        """
        해당 함수는 정적함수로 정의되었으므로 인스턴스 외부에 독립적으로 생성된다.
        따라서 특정 인스턴스의 멤버변수에 접근하기 위해 인스턴스의 참조값을
        매개변수로 받은 후 사용해야 한다.
        """
        # 주어진 두 숫자 곱하고 다른 숫자와 곱하기
        result = (refCls.first * refCls.second) * otherNum
        MyCalculator.calCount += 1
        print("결과:", result)
        print("연산횟수:", MyCalculator.calCount)


# MyCalculator 객체 생성
cal1 = MyCalculator(5, 9)
cal2 = MyCalculator(3, 4)

# 계산 수행 및 결과 출력
print("덧셈(cal1):", cal1.calculate("+"))
print("곱셈(cal1):", cal1.calculate("*"))
print("뺄셈(cal2):", cal2.calculate("-"))
print("나눗셈(cal2):", cal2.calculate("/"))

# 전체 연산 횟수 출력
print("계산횟수:", MyCalculator.calCount)

"""
정적 함수는 참조변수가 아니라 클래스명으로 직접 호출한다. 즉 함수 호출을
위해 인스턴스를 생성할 필요가 없다.
"""
# 클래스의 정적 메서드 호출
MyCalculator.otherNumMulti(cal1, 10)
MyCalculator.otherNumMulti(cal2, 10)
