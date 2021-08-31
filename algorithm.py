def solution(s):
    # 1. init
    cnt = 0
    removed_cnt = 0
    
    # 2. len_to_binary
    def len_to_binary(n):
        res = ""
        
        while n > 0:
            res += str(n % 2)
            n //= 2
        
        return res[::-1]
    
    # 3. loop
    while s != "1":
        # 1) remove zero
        zero_removed = s.replace("0", "")
        removed_cnt += len(s) - len(zero_removed)
        
        # 2) length to binary
        s = len_to_binary(len(zero_removed))
        
        # 3) update
        cnt += 1

    return [cnt, removed_cnt]
