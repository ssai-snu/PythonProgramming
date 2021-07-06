def partition(l, low, high):
    p = l[low]
    small = []
    large = []
    print("Input: [" + str(p) + "]", l[low+1:])
    for i in l[low+1:high+1]:
        if (i < p):
            small.append(i)
        else:
            large.append(i)
        print("[" + str(p) + "]", small, large)
    small.append(p)
    print(small, large)
    idx = low
    for i in small:
        l[idx] = i
        idx += 1
    for i in large:
        l[idx] = i
        idx += 1
    print(l)
    return (low + len(small)-1)

def partition_swap(l,low, high):
    def swap(i, j):
        t = l[i]
        l[i] = l[j]
        l[j] = t
        return
    p = l[low]
    m = low
    for j in range(low+1, high+1):
        if (l[j] < p):
            m += 1
            swap(j, m)
    swap(low, m)
    return m

def quik_sort(l):
    def qs(l, low, high, n):
        print("===" * n + " Sorting " + str(l[low:high+1]))
        if(low<high):
            pivot_idx = partition_swap(l, low, high)
            print("===" * n + " After partitioning: " + str(l[low:pivot_idx])
                  + "[" + str(l[pivot_idx]) + "]" + str(l[pivot_idx+1:high+1]))

            qs(l, low, pivot_idx - 1, n + 1)
            qs(l, pivot_idx+1, high,  n + 1)
            print("===" * n + " After Sorting: " + str(l[low:pivot_idx])
                  + "[" + str(l[pivot_idx]) + "]" + str(l[pivot_idx+1:high+1]))
        return l
    qs(l, 0, len(l)-1, 0)
    return l