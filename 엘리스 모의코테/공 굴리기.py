def main():
    n, m = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(n)]
    ball = list(map(int, input().split()))
    ball = [ball[0] - 1, ball[1] - 1]
    visited = [ball]

    dx = [0,-1, 0, 0, 1]
    dy = [0,0, -1, 1, 0]


    while True:
        temp = ball
        d = M[temp[0]][temp[1]]
        temp[0] += dx[d]
        temp[1] += dy[d]
        visited.append(temp)
        if temp[0] < 0 or temp[0] >= m or temp[1] < 0 or temp[1] >= n:
            print(-1)
            break

    print(visited)

if __name__ == "__main__":
    main()