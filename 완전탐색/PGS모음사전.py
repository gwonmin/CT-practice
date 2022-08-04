word = "AAAAE"

from itertools import product

def solution(word):
    alpha = ['A','E','I','O','U']
    products = []
    for i in range(1,6):
        for p in product(alpha,repeat=i):
            products.append(''.join(p))
    products.sort()
    answer = products.index(word)+1
    return answer

solution(word)