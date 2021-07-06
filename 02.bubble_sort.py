def bubble_sort(l):
    def swap(i, j):
        t = l[i]
        l[i] = l[j]
        l[j] = t
        print(" after swap(" + str(i) + ", " + str(j) + "):" + str(l))
        return
    
    n = len(l) - 1
    for i in range(n, 0, -1):
        print("Iterataion   " + str(i) + ": " + str(l))
        for j in range(i):
            if (l[j] >= l[j+1]):
                swap(j, j+1)
    return l