from tempfile import _candidate_tempdir_list

max_number = 1e5

import math

def primes(n):
    primes = [2]
    current_number = 3

    while current_number < n:
        upper_limit = math.sqrt(current_number)
        non_div = True
        for p in primes:
            if current_number % p == 0:
                non_div = False
                break
            if p > upper_limit:
                break
        if non_div:
            primes.append(current_number)
        current_number += 2
    return primes

p = primes(1e7)
print("The number of primes:",len(p))

def is_candidate(prime):
    from collections import Counter
    c = Counter(str(prime)[:-1])
    return 3 in c.values()

candidates = filter(is_candidate,p)
print("The number of candidates", len(candidates))


def remove_repeated(prime):
    string_rep = str(prime)[:-1]
    from collections import Counter
    c = Counter(string_rep)
    g = filter(lambda x: (c[x]==3),list(c.iterkeys()))
    counter = 0
    for digit in g:
        counter += 1
        string_rep = string_rep.replace(digit, "X"+str(counter))
    return string_rep + str(prime)[-1:]

candidates_mapped = map(remove_repeated,candidates)
from collections import Counter
print(Counter(candidates_mapped))

#'X2X2X2X1X1X17': 8, 'X1X2X1X2X1X21': 8, 'X2X2X1X1X2X11': 8

for x1 in range(9):
    for x2 in range(9):
        can = int('X2X2X2X1X1X17'.replace("X2",str(x2)).replace("X1",str(x1)))
        if can in p:
            print(can)