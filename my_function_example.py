from math import sqrt
from itertools import count, islice
def is_prime(n):
    for number in islice(count(2), int(sqrt(n)-1)):
            if not n%number:
                return False
    return True

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
