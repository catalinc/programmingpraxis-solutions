# Solution to http://programmingpraxis.com/2014/08/22/patience-sorting/


def patience_sort(items):
    piles = []
    while items:
        x = items.pop(0)
        added = False
        for p in piles:
            if p[0] > x:
                p.insert(0, x)
                added = True
                break
        if not added:
            p = [x]
            piles.append(p)
    sorted_items = []
    while piles:
        min_pile, min_item = None, None
        for p in piles:
            if not min_pile or p[0] < min_item:
                min_pile = p
                min_item = p[0]
        sorted_items.append(min_item)
        min_pile.pop(0)
        if not min_pile:
            piles.remove(min_pile)
    return sorted_items

if __name__ == '__main__':
    print(patience_sort([4, 3, 9, 1, 5, 2, 7, 8, 6]))