import itertools
from heapq import merge

def nth_hamming_number(n):
    def num_recur():
        last = 1
        yield last
        x, y, z = itertools.tee(num_recur(), 3)
        for n in merge((2 * i for i in x), (3 * i for i in y), (5 * i for i in z)):
            if n != last:
                yield n
                last = n
    result =  itertools.islice(num_recur(), n)
    return list(result)[-1]

print(nth_hamming_number(8))
print(nth_hamming_number(14))
print(nth_hamming_number(17))