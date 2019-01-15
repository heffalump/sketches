


### KMP

def prefix_function(s):
    '''Creates the prefix function for the given string s, to be used in KMP or similar'''
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


            
