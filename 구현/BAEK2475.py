num_lst = list(map(int, input().split()))
sqrt_sum = sum(list(map(lambda x: x**2,num_lst)))
result = sqrt_sum%10

print(result)

