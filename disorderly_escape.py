"""
Disorderly Escape
=================

Oh no! You've managed to free the bunny prisoners and escape Commander Lambdas exploding space station, but her team of
elite starfighters has flanked your ship. If you dont jump to hyperspace, and fast, youll be shot out of the sky!

Problem is, to avoid detection by galactic law enforcement, Commander Lambda planted her space station in the middle of
a quasar quantum flux field. In order to make the jump to hyperspace, you need to know the configuration of celestial
bodies in the quadrant you plan to jump through. In order to do *that*, you need to figure out how many configurations
each quadrant could possibly have, so that you can pick the optimal quadrant through which youll make your jump.

There's something important to note about quasar quantum flux fields' configurations: when drawn on a star grid,
configurations are considered equivalent by grouping rather than by order. That is, for a given set of configurations,
if you exchange the position of any two columns or any two rows some number of times, youll find that all of those
configurations are equivalent in that way - in grouping, rather than order.

Write a function answer(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations
that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states.
Equivalency is defined as above: any two star grids with each celestial body in the same state where the actual order of
the rows and columns do not matter (and can thus be freely swapped around). Star grid standardization means that the
width and height of the grid will always be between 1 and 12, inclusive. And while there are a variety of celestial
bodies in each grid, the number of states of those bodies is between 2 and 20, inclusive. The answer can be over 20
digits long, so return it as a decimal string.  The intermediate values can also be large, so you will likely need to
use at least 64-bit integers.

For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0
(for instance, silent) or state 1 (for instance, noisy).  We can examine which grids are equivalent by swapping rows and
columns.

00
00

In the above configuration, all celestial bodies are "silent" - that is, they have a state of 0 - so any swap of row or
column would keep it in the same state.

00 00 01 10
01 10 00 00

1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of the
4 positions.  All four of the above configurations are equivalent.

00 11
11 00

2 celestial bodies are emitting noise side-by-side.  Swapping columns leaves them unchanged, and swapping rows simply
moves them between the top and bottom.  In both, the *groupings* are the same: one row with two bodies in state 0, one
row with two bodies in state 1, and two columns with one of each state.

01 10
01 10

2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different because
there's no way to transpose the grid.

01 10
10 01

2 noisy celestial bodies diagonally.  Both have 2 rows and 2 columns that have one of each state, so they are equivalent
to each other.

01 10 11 11
11 11 01 10

3 noisy celestial bodies, similar to the case where only one of four is noisy.

11
11

4 noisy celestial bodies.

There are 7 distinct, non-equivalent grids in total, so answer(2, 2, 2) would return 7.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) w = 2
    (int) h = 2
    (int) s = 2
Output:
    (string) "7"

Inputs:
    (int) w = 2
    (int) h = 3
    (int) s = 4
Output:
    (string) "430"
"""


import fractions
from math import factorial


def make_change(goal, coins):
    wallets = [[coin] for coin in coins]
    new_wallets = []
    collected = [[(goal, 1)]]

    while wallets:
        for wallet in wallets:
            s = sum(wallet)
            for coin in coins:
                if coin >= wallet[-1]:
                    if s + coin < goal:
                        new_wallets.append(wallet + [coin])
                    elif s + coin == goal:
                        wallet += [coin]
                        vector = []
                        for c in set(wallet):
                            vector.append((c, wallet.count(c)))
                        collected.append(vector)
                    else:
                        break
        wallets = new_wallets
        new_wallets = []
    return collected


def lcm(a, b):
    return (a * b) / fractions.gcd(a, b)


def calc_coefs(poly):
    out = []
    for vars in poly:
        denominator = 1
        for k, j_k in vars:
            denominator *= factorial(j_k) * k ** j_k
        out.append((fractions.Fraction(1, denominator), vars))
    return out


def combine_vars(a, b):
    out = []
    for sub_a, super_a in a:
        for sub_b, super_b in b:
            lcm_ = lcm(sub_a, sub_b)
            out.append((lcm_, (super_a * super_b * sub_a * sub_b) / lcm_))
    return out


def mult_poly(p1, p2):
    prod = []
    for coef1, var1 in p1:
        for coef2, var2 in p2:
            new_coef = coef1 * coef2
            new_var = combine_vars(var1, var2)
            prod.append([new_coef, new_var])
    return prod


def calc_cycle_index(poly, s):
    tot = 0
    for coef, vars in poly:
        var_tot = 1
        for sub, super_ in vars:
            var_tot *= s ** super_
        tot += coef * var_tot
    return tot


def solution(w, h , s):
    poly_w = calc_coefs(make_change(w, range(1, w + 1)))
    poly_h = calc_coefs(make_change(h, range(1, h + 1)))
    poly_tot = mult_poly(poly_w, poly_h)
    cycle_index = calc_cycle_index(poly_tot, s)
    return str(cycle_index)


if __name__ == "__main__":
    assert solution(2, 3, 4) == "430"
    assert solution(2, 2, 2) == "7"
