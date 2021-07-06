def selection_sort(l):
    def swap(i, j):
        print(str(l) + " === after swapping " +
              str(l[i]) + " and " + str(l[j]) + "===> ", end='')
        t = l[i]
        l[i] = l[j]
        l[j] = t
        print(l)
        return
    print("Input: " + str(l))
    n = len(l)
    for i in range(0, n-1):
        s = i
        print("Iter. " + str(i) +
              "   -----------------------------------------------------")
        print("  comparing " + str(l[s]) +
              " with the elements in " + str(l[s+1:]))
        swap_flag = False
        for j in range(i+1, n):
            if(l[s] >= l[j]):
                s = j
                swap_flag = True
        swap(i, s) if swap_flag else None
        print(str(l[0:i+1]) + str(l[i+1:]))
    return l
