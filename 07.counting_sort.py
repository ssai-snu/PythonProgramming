def counting_sort(l, m):
    c = [0] * (m + 1)
    for i in l:
        c[i] += 1
    print(c)
    
    for j in range(1, m+1):
        c[j] = c[j-1] + c[j]
    print(c)
    
    n = len(l)
    t = [0] * n
    for i in range(n-1, -1, -1):
        j = l[i]
        t[c[j] - 1] = j
        c[j] = c[j] -1
    for i in range(0, n):
        l[i] = t[i]
    return l