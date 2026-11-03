import sys
import lexorder

if len(sys.argv) < 2:
    print("usage: test-subsets.py <n>")
else:
    n = int(sys.argv[1])

    for i in range(2**n):
        A = lexorder.unrank(i, n)
        B = lexorder.successor(A, n)
        print(f'{lexorder.rank(A, n)} successor({A}) = {B}')