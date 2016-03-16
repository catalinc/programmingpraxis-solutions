# Solution to https://programmingpraxis.com/2016/03/04/wave-sorting/


def wave_sort_set(l):
    ns = set(l)
    r = []
    while ns:
        max_n = max(ns)
        ns.remove(max_n)
        r.append(max_n)
        if ns:
            min_n = min(ns)
            ns.remove(min_n)
            r.append(min_n)
    return r


def wave_sort_bubble(l):
    i = 0
    while i < len(l) - 1:
        swap = False
        if i % 2 == 0:
            if l[i] < l[i + 1]:
                swap = True
        elif l[i] > l[i + 1]:
            swap = True
        if swap:
            l[i], l[i + 1] = l[i + 1], l[i]
        i += 1
    return l


if __name__ == '__main__':
    test_data = [[4, 1, 7, 5, 6, 2, 3], [8, 3, 10, 0, 7, 4, 13, 9, 11, 2]]
    for l in test_data:
        print(wave_sort_set(l))
        print(wave_sort_bubble(l))
        print('-' * 50)
