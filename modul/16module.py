# 방법1 : 모듈명만 임포트. 이경우 모듈명을 함께 기술해서 함수를 호출한다.
import mod1

print("모듈의 함수 호출1 : ", mod1.add(3, 4))
print("모듈의 함수 호출2 : ", mod1.sub(4, 2))

from mod1 import add

result = add(3, 4)
print(" 결과  : ", result)


from mod1 import *

result1 = add(3, 4)
print(" 결과 : ", result1)
result2 = sub(3, 4)
print(" 결과 : ", result2)

# __name__ 변수를 사용하여 작성된 모듈 임포트
import mod2

# 임포트하면 __name__에는 "mod2"가 저장됨.

result = mod2.mul(3, 4)
print(result)

import commons.mod3

commons.mod3.sum1To10()

from commons.mod3 import sum1To10

sum1To10()
