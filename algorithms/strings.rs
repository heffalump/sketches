


// KMP

fn kmp(s: &str) -> Vec<usize> {
    let n = s.len();
    let s_: Vec<_>  = s.chars().collect();
    let mut pi = vec![0; n];
    for i in 1..n {
        let mut j = pi[i - 1];
        while j > 0 && s_[i] != s_[j] {
            j = pi[j - 1];
        }
        if s_[i] == s_[j] {
            j += 1;
        }
        pi[i] = j;
    }
    return pi;
}




// Z-function

use std::cmp

fn z_function(s: &str) -> Vec<usize> {
    let n = s.len();
    let s_: Vec<_>  = s.chars().collect();
    let mut z = vec![0; n];
    let mut l = 0;
    let mut r = 1;
    for i in 1..n {
        if i <= r {
            z[i] = cmp::min(z[i - l], r - i + 1);
        }
        while i + z[i] < n && s_[i + z[i]] == s_[z[i]] {
            z[i] += 1;
        }
        if i + z[i] >= r {
            l = i;
            r = z[i] + i - 1;
        }
    }
    return z;
}


