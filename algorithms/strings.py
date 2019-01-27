


### KMP

def prefix_function(s):
    '''Creates the prefix function array for the given string s, to be used in KMP or similar'''
    pi = [0]
    n = len(s)
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi.append(j)
    return pi



### Needs testing


def z_function(s):
    '''Creates the Z-function array for the given string s'''
    z = [0]
    n = len(s)
    l = 0
    r = 1
    for i in range(1, n):
        z.append(0)
        if i < r:
            z[i] = min(z[i - l], r - i)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] >= r:
            l = i
            r = z[i]
    return z


### Suffix Arrays

def make_suffix_array(s):
    '''Creates a suffix array for the given string s in n(log(n))^2 time, because I'm lazy'''
    n = len(s)
    ranges = [n] + sorted([i for i in range(n)], key = lambda x: s[x])
    order = [0] * (n + 1)
    l = 1  ## interval length
    while (l < 2 * n):
        for (ord, ind) in enumerate(ranges):
            order[ind] = ord
        ranges = sorted([i for i in range(n + 1)],
                        key = lambda x: (order[x], order[(x + l) % (n + 1)]))
        l *= 2
    return [i - 1 for i in order[0:n]]



