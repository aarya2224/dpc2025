def 
zerosum_subarrays(arr):
    prefix_sum = 0
    seen = {0: [-1]}   
    res= []

    for i, num in enumerate(arr):
        prefix_sum += num

        
        if prefix_sum in seen:
            for start in seen[prefix_sum]:
                res.append((start + 1, i))

      
        seen.setdefault(prefix_sum, []).append(i)

    return res



arr = [1, 2, -3, 3, -1, 2]
print(zerosum_subarrays(arr))
