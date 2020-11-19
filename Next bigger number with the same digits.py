def next_bigger(n):
    n_str = str(n)
    for i in range(len(n_str) - 1, 0, -1):
        if n_str[i] > n_str[i - 1]:
            min_number = min(d for d in n_str[i:] if d > n_str[i-1])
            following_digits = ''.join(sorted(n_str[i-1] + n_str[i:]))
            n_str = n_str[:i-1] + min_number + following_digits.replace(min_number, '', 1)
            return int(n_str)
    return -1

print(next_bigger(9922))
