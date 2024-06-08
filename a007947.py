from sympy import primefactors, prod
def a(n): return  prod(primefactors(n))

if __name__ == "__main__":
    assert [a(i) for i in range(1,13)] == [1,2,3,2,5,6,7,2,3,10,11,6]
    for i in range(1, 10_001):
        print(f"{i} {a(i)}")

