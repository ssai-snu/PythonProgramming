def insertion_sort(l):
    n = len(l)
    print("input: " + str(l))
    print("   sorted: " + str(l[0:1]) + ", unsorted: " + str(l[1:]))
    for j in range(1, n):
        print("After inserting " + str(l[j]) + " into " + str(l[0:j]) + ", ")
        key = l[j]
        i = j - 1
        while ((i >= 0) and (key < l[i])):
            l[i+1] = l[i]
            i -= 1
        l[i+1] = key
        print("    " + str(l[0:j+1]) + str(l[j+1:]))
    return l
