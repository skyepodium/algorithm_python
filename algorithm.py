def solution(arr1, arr2):
    # 1. init
    n = len(arr1)
    m = len(arr1[0])
    
    # 2. loop
    for i in range(n):
        for j in range(m):
            arr1[i][j] += arr2[i][j]
            
    return arr1
