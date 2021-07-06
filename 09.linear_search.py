def linear_search(l, e):
    found = False
    for i in l:
        if(i == e):
            found = True
    return found

def linear_search_idx(l, e):
    n = len(l)
    idx = -1
    for i in range(n):
        if(l[i] == e):
            idx = i
    return idx


def linear_search_sorted(l, e):
    found = False
    for i in l:
        if(i == e):
            found = True
            break
        if (i > e):
            found = False
            break
    return found