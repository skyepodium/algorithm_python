def solution(n):
    # 1. init
    max_int = 1000001
    one_cnt = 0
    
    # 2. to_binary
    def to_binary(n):
        res = ""
        while n > 0:
            res += str(n%2);
            n //= 2
        return res[::-1]
    
    # 3. update_one_cnt
    one_cnt = to_binary(n).count("1")
    
    # 4. loop
    for i in range(n+1, max_int):
        if one_cnt == to_binary(i).count("1"):
            return i
    
    return -1
