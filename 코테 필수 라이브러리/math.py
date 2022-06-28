# 1. factorial(x) => x의 팩토리얼 값 출력

# 2. sqrt(x) => x의 제곱근 출력

# 3. gcd(a,b) => a 와 b의 최대공약수 출력

# 4. 상수 pi , e => 파이와 자연상수 출력

# import math

# print(math.factorial(5))   # 120
# print(math.sqrt(7))        # 2.6457513110645907
# print(math.gcd(21,14))     # 7
# print(math.pi)             # 3.14159....93
# print(math.e)              # 2.71828......45

# math.round()
# 반올림

# math.ceil(x)
# 함수 설명 : 인자로 들어온 x의 올림 값을 반환합니다
# 반환한 값은 정수 타입(int)으로 반환이 됩니다.
# 당연하게도 음수의 올림도 가능합니다.

# import math
# math.ceil(1.0) # 1
# math.ceil(1.1) # 2
# math.ceil(1.5) # 2
# math.ceil(2.1) # 3
# math.ceil(-3.2) # -3

# math.floor(x)
# 함수 설명 : 인자로 들어온 x의 내림 값을 반환합니다
# 반환하는 결괏값은 정수 타입(int)으로 반환이 됩니다.
# 당연하게도 음수의 내림도 가능합니다.

# import math
# math.floor(1.0) # 1
# math.floor(1.1) # 1
# math.floor(1.5) # 1
# math.floor(2.1) # 2
# math.floor(-3.2) # -4