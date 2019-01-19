


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

    min_character = '$'  ## alter this if needed for an artifical minimum

    ## Make intervals for single character strings, sort by those letters

    ## Conert the order of those intervals into a map from interval -> position

    ## REpeatedly: create intervals of double the length.  sort them by using as a key
    ## the ordered pair of the first half of the intervals position, second half of the
    ## intervals position

    ## once we have intervals for length > length of s, their positions are the suffix array
    ## using the left bound of the interval 


    return
