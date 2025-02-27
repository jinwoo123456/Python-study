# 람다식과 amp, filter, reduce 함수 활용
print(f"{'람다식과 map함수1':-^30}")
# 인자에 2를 곱한 결과를 반환하는 람다식
multiLambda = lambda x: x * 2
list_data = [1, 2, 3, 4, -1, -2, -5, -10]
# 리스트의 인자 갯수만큼 람다식을 호출하여 얻어진 결과를 리스트로 반환한다.
result = list(map(multiLambda, list_data))
# 리스트의 전체 인자를 2로 곱한 결과값이 출력된다.
print("결과1", result)

"""
람다식에서 조건부 표현식(삼항 연산자) 사용하기
형식 : 식1 if 조건식 else 식2
     -조건식이 참일때 식1 거짓일때 식2
     -if를 사용했다면 반드시 else를 사용해야함.
     -elif는 사용 불가
     -2개 이상의 조건이 필요하면 if를 연속으로 사용해야한다.(이정도 길이면 조건식 쓰는게 낫다)
"""
print(f"{'람다식과 map함수2':-^30}")
list_data2 = [x for x in range(1, 11)]
strNumLambda = lambda x: "3X" if x % 3 == 0 else x  # 3의 배수인 경우 3X로 출력
result = list(map(strNumLambda, list_data2))
print("결과2", result)
# 출력 결과 : 3의 배수는 3X로 출력.나머지는 숫자로 출력
# [1, 2, '3X', 4, 5, '3X', 7, 8, '3X', 10]
print(f"{'람다식과 filter함수':-^30}")
list_data3 = [1, 4, 9, 16, 25, 47, 64, 81, 100]
result = list(filter(lambda z: z > 5 and z < 80, list_data3))
print("결과3", result)
# 출력 결과 : 5보다 크고 80보다 작은 수만 출력
# [9, 16, 25, 47, 64]
print(f"{'람다식과 reduce함수':-^30}")
import functools, operator

sum1 = functools.reduce(lambda i, j: i + j, range(1, 11))
print("결과4-1 :", sum1)

sum2 = functools.reduce(operator.add, range(1, 11))
print("결과4-2 :", sum2)
