from dataclasses import replace
import sys

I = sys.stdin.readline()
P = sys.stdout.write

N = int(I)

star = "*"
result = ""
def Solution(star,N):
    if N == 3:
        result = f'{star}{star}{star}\n{star} {star}\n{star}{star}{star}'
        return
    
Solution(star,N)

P(result)
