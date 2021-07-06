def binary_search(l, e):
    def bs(l, low, high, e):
        if (low > high):
            return -1
        i = int((low + high)/2)
        if (l[i] == e):
            return i
        elif (l[i] < e):
            i = bs(l, i+1, high, e)
        else:
            i = bs(l, low, i-1, e)
        return i
    return bs(l, 0, len(l)-1, e)


def binary_search_iter(l, e):
    low = 0
    high = len(l) -1
    while (low < high):
        i = int((high + low)/2)
        if (l[i] == e):
            return i
        elif (l[i] < e):
            low = i + 1
        else:
            high = i -1
    return -1

