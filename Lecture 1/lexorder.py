def rank(A:set, n:int) -> int:
    """
    the rank of A in lexicographic order
    """
    """
    require:
        A in 2^[0,n)
    """
    r = 0

    for i in range(n):

        r = r + (2**i) * (i in A)

    return r
    """
    ensure: r = int(X(A))
    """

def unrank(r: int, n: int) -> set:
    """
    an inplementation of the unrank algorithm
    """
    """
    pre: r: [0:2^n]
    """
    A = set()

    for a in range(n):
        
        if r % 2 == 1:
            A = A | {a}  # This is an union operation

        r //= 2          # r = r // 2
    
    return A
    """
    post: int(X(A)) = r
    """

def successor(A: set, n: int) -> set:
    """
    an implementation of the successor algorithm
    """
    """
    pre: A: 2^[0:n)
    """
    B, a = A, 0

    while(a in B):

        B, a = B-{a}, a+1   # This is an minus operation
         
    if a < n:

        B = B | {a}

    return B
    """
    post: X(B) = X(A) + 1
    """

import math

def fac2dec(f: int, n: int) -> int:
    """
    the decimal value of a factorial number
    """
    # require f is a factorial number

    d = 0
    q = f // 10       # quotient
    r = 0       # remainder
    m = 1       # multiplier

    for i in range(n - 1):
            
            m = m * (i + 1)
            r = q % 10
            q = q // 10

            d = d + r * m
    
    return d


def dec2fac(d: int, n: int) -> int:
    """
    the factorial representation of a decimal number
    """
    # require d is a decimal number

    f = 0      # list of digits

    q = d       # quotient

    for i in range(n):
        
        r = q % (i + 1)

        f = r * (10**i) + f

        q = q // (i + 1)

    return f

def encode(pi: list[int], n: int) -> list[int]:
    """
    the Lehmer code of pi
    """
    # require: pi in Pi^n

    rho = [0]*n
    
    for i in range(n):

        rho[i] 