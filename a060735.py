from functools import cache
from sympy import primefactors, prod
@cache
def a(n): return 1 if n == 0 else a(n-1) + prod(primefactors(a(n-1)))
print([a(n) for n in range(42)])

#if __name__ == "__main__":
#    assert [a(n) for n in range(1,13)] == [1,2,4,6,12,18,24,30,60,90,120,150]
#    for i in range(1, 20_001):
#        print(f"{i} {a(i)}")

