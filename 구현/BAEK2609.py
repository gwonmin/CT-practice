num1, num2 = map(int, input().split())

def gcd(num1, num2):
    first_num = max(num1,num2)
    second_num = min(num1,num2)

    while True:
        mod = first_num % second_num
        if mod == 0:
            break
        first_num = second_num
        second_num = mod

    return second_num

def lcm(num1,num2):
    num1_set = set()
    num2_set = set()
    i = 0
    while True:
        i += 1
        num1_set.add(num1*i)
        num2_set.add(num2*i)
        inter_set = num1_set.intersection(num2_set)
        if len(inter_set) != 0:
            return min(inter_set)

print(gcd(num1,num2))
print(lcm(num1,num2))