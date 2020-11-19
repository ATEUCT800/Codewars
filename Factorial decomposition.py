def get_divisible(number, factor, count = 0):
    if number % factor == 0:
        count += get_divisible(number // factor, factor) + 1
    return count

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def decomp(n):
    decompos = {}
    result = ''

    prime_factors = [i for i in range(n, 1, -1) if isPrime(i)]

    for i in range(2, n + 1):
        for j in prime_factors:
            if i % j == 0:
                if not j in decompos.keys(): decompos[j] = get_divisible(i, j)
                else: decompos[j] += get_divisible(i, j)

    for factor, count in sorted(decompos.items()):
        if count != 1: result += f'{factor}^{count} * '
        else: result += f'{factor} * '
    return result[:-3]

print(decomp(12))