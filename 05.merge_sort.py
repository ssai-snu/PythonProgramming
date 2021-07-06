def merge(left, right):
    len_left, len_right = len(left), len(right)
    i_left, i_right = 0, 0
    l = []
    print(l, left[i_left:], right[i_right:])
    while((i_left < len_left) and (i_right < len_right)):
        if (left[i_left] < right[i_right]):
            l.append(left[i_left])
            i_left += 1
        else:
            l.append(right[i_right])
            i_right += 1
        print(l, left[i_left:],  right[i_right:])
    while (i_left < len_left):
        l.append(left[i_left])
        i_left += 1
        print(l, left[i_left:],  right[i_right:])
    while (i_right < len_right):
        l.append(right[i_right])
        i_right += 1
        print(l, left[i_left:],  right[i_right:])
    return l

def merge_sort(l, n):
    if((len(l) == 0) or (len(l) == 1)):
        return l
    mid = int(len(l) / 2)
    print("   " * n + "Dividing " + str(l) +
          " into " + str(l[0:mid]) + str(l[mid:]))

    left = merge_sort(l[0:mid], n+1)
    print("   " * n + "After sorting " + str(l[0:mid]) + ", " + str(left))

    right = merge_sort(l[mid:], n+1)
    print("   " * n + "After sorting " + str(l[mid:]) + ", " + str(right))

    r = merge(left, right)
    print("   " * n + "After merging " + str(left) + " and " + str(right) + ", " + str(r))
    return r
