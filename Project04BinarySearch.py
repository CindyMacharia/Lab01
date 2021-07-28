def binary_search(list, n):
    lower_end = 0
    upper_end = len(list) - 1

    while lower_end <= upper_end: 
        mid = lower_end + (upper_end - lower_end) // 2
        mid_value = list[mid]
        if mid_value == n:
            return mid

        elif n < mid_value:
            upper_end = mid - 1

        else:
            lower_end = mid + 1

    return None

list = [22,24,26,28,30,32,34,36,38,40,42]
n = 34

print(binary_search(list, n))



    
            



    

