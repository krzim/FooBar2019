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
