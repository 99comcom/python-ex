#문자형 변수
a = "Hello, World."
print(a, type(a)) #정수형 변수
a=100
print(type(a)) #실수형 변수
b=200.5
print(type(b)) #불린 변수
a = True
print(a, type(a)) #사칙 연산
add = a + b
subtract = a - b
multiply = a * b
divide = a / b
quotient = a // b
remainder = a % b
#사칙 연산 결과 출력
print(a, "+", b, "=", add)
print(a, "-", b, "=", subtract)
print(a, "x", b, "=", multiply)
print(a, "/", b, "=", quotient)
print(a, "%", b, "=", remainder)
print(type(divide)) #관계 연산자
a = 10
b = 20
c = a < b
#관계 연산 결과 출력
print(c, type(c))
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b) #논리 연산자
a = True
b = False #논리 연산 결과 출력
print(a & b)
print(a | b)
print(not a)
print(not b)
