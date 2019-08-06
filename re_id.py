"""
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been
lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked
you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme.

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number
from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next
five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's
string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the
value of n will always be between 0 and 10000.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(0)
Output:
    23571

Input:
Solution.solution(3)
Output:
    71113

-- Python cases --
Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113
"""


def eratosthenes():
    """
        Modification of Sieve of Eratosthenes by David Eppstein, UC Irvine, 28 Feb 2002 from
        http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
    """
    composite2prime = {}
    q = 2
    while True:
        p = composite2prime.pop(q, None)
        if p is not None:
            x = p + q
            while x in composite2prime:
                x += p
            composite2prime[x] = p
        else:
            composite2prime[q*q] = q
            yield q
        q += 1


def solution(n):
    sieve = eratosthenes()
    prime_str = ""
    while len(prime_str) < n + 5:
        prime_str += str(next(sieve))
    return prime_str[n:n+5]


if __name__ == "__main__":
    assert solution(0) == "23571"
    assert solution(3) == "71113"
