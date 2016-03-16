# Solution to https://programmingpraxis.com/2016/03/08/string-prefixes/


def str_prefix(s1, s2):
    i = 0
    k = min(len(s1), len(s2))
    while i < k and s1[i] == s2[i]:
        i += 1
    return s1[0:i]


def seq_prefix(seq):
    p = None
    for s in seq:
        if p is None:
            p = s
        else:
            p = str_prefix(p, s)
    return p or ''

if __name__ == '__main__':
    print(seq_prefix(['I love cats', 'I love dogs', 'I love pasta']))
