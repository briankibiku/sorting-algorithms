def quick_sort(s):
    if len(s) <= 1:
        return s
    else:
        pivot = s.pop()
    first_array = []
    last_array = []
    for item in s:
        if pivot > item:
            first_array.append(item)
        else:
            last_array.append(item)
    return quick_sort(first_array) + [pivot] + quick_sort(last_array)
    
    
print(quick_sort([0,3,2,9,8,7,50,33,2,9,8,7,50,3,2,9,8,7,55,35,35,64,735,754,421,84,8,3124,124,4,1,51,53,431,7,5,56,7,563,3,73,45,5456,46,436,436,643,364,436,46,346,]))