def main():
    x = int(input())
    person = list(map(int, input().split()))

    count = 1
    min_dif = 9999999999999

    for h in range(max(person)+1):
        dif = 0
        for p in person:
            dif += abs(p-h)
        if dif < min_dif:
            min_dif = dif
        elif dif == min_dif:
            count += 1

    print(count)

if __name__=="__main__":
    main()