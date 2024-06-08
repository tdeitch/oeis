from sympy import primefactors, prod
def a(n): return 1 if n == 1 else a(n-1) + prod(primefactors(a(n-1)))

from functools import cache

@cache
def a060735(n):
    if n == 1: return 1
    return a060735(n-1) + prod(primefactors(a060735(n-1)))

if __name__ == "__main__":
    assert [a(n) for n in range(1,13)] == [1,2,4,6,12,18,24,30,60,90,120,150]
    assert [a060735(n) for n in range(1,13)] == [1,2,4,6,12,18,24,30,60,90,120,150]

    for i in range(1, 10_001):
        print(f"{i} {a060735(i)}")

