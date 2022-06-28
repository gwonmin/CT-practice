n = int(input())

triangle = [[0]+list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(1,len(triangle[i-1])):
        triangle[i][j] = max(triangle[i-1][j]+triangle[i][j],triangle[i-1][j-1]+triangle[i][j])
    triangle[i][-1] += triangle[i-1][-1]
    triangle[i][0] += triangle[i-1][0]

print(*triangle,sep='\n')
print(max(triangle[-1]))

