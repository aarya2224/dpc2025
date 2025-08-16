def missing_num(arr):
    n = len(arr) + 1  
    exp_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return exp_sum - actual_sum

arr = [1, 2, 4, 5]
print("Missing number:", missing_num(arr))
