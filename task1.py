def binary_bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if int(arr[j], 0) > int(arr[j+1], 0):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

a = ['0b1100100', '0b100101', '0b100']
print(binary_bubble_sort(a))