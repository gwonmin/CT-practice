while True:
    T = input()
    if T == "0":
        break

    num = len(T)//2
    if T[:num] == T[::-1][:num]:
        print("yes")
    else:
        print("no")