import sys

I = sys.stdin.readline
P = sys.stdout.write

N = int(I())
num_list = []

for _ in range(N):
    num_list.append(int(I()))

num_list.sort()
P('\n'.join(map(str,num_list)))



#힙 활용
# import heapq

# N = int(sys.stdin.readline())
# num_list = [int(sys.stdin.readline()) for _ in range(N)]
# heap = []

# for i in num_list:
#     heapq.heappush(heap,i)

# for i in range(len(heap)):
#     result = heapq.heappop(heap)
#     print(result)
    
    