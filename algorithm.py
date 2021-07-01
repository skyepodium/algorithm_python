def solution(lottos, win_nums):
    best_rank = 1
    worst_rank = 6

    zero_cnt = 0
    match_cnt = 0
    for num in lottos:
        if num == 0:
            zero_cnt += 1

        for win_num in win_nums:
            if num == win_num:
                match_cnt += 1

    worst_rank = 7 - match_cnt
    if worst_rank == 7:
        worst_rank = 6

    best_rank = 7 - (match_cnt + zero_cnt)
    if best_rank == 7:
        best_rank = 6

    return [best_rank, worst_rank]