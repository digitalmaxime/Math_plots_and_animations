import cmath
import math

def exp(n):
    res = 1
    term = 1
    for i in range(10):
        res += n**term/math.factorial(term)
        term += 1
    return res
    #return sum([
    # n**p / math.factorial(p)
    # for p in range(0, 100)
    # ])


if __name__ == "__main__":
    print(cmath.sqrt(1j))
    print()
    print(exp(complex(1, 1)))