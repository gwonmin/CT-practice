num_lst = list(map(int, input().split()))

temp = [i for i in range(1,9)]

if num_lst == temp:
    print("ascending")
elif num_lst == temp[::-1]:
    print("descending")
else:
    print("mixed")