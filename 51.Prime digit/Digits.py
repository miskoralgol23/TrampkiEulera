
max_number = 1e6

import math

primes = [2]
current_number = 3

while current_number < max_number:
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

print(len(primes))
print(primes[:10], primes[-10:])
