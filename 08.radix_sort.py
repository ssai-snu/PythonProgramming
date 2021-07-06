def radix_sort(l, d):
    for r in range(0, d):
        c = [0] * 10
        m = d - r - 1
        for i in l:
            key = int(str(i)[m])
            c[key] += 1
        for j in range(1, 10):
            c[j] = c[j-1] + c[j]
        
        n = len(l)
        t = [0] * n
        for i in range(n-1, -1, -1):
            key = int(str(l[i])[m])
            t[c[key] - 1] = l[i]
            c[key] = c[key] -1
        for j in range(0, n):
            l[j] = t[j]
    return l