def solution(enroll, referral, seller, amount):

    size = len(enroll)
    answer = [0 for _ in range(size)]
    v = [0 for _ in range(size + 1)]

    # 1. name_dict
    name_dict = {'-': 0}
    idx_dict = {0: '-'}
    idx = 1
    for en_name in enroll:
        name_dict[en_name] = idx
        idx_dict[idx] = en_name
        idx += 1

    for num in range(size):
        c = enroll[num]
        p = referral[num]
        v[name_dict[c]] = name_dict[p]

    sell_size = len(seller)
    for num in range(sell_size):
        node = name_dict[seller[num]]
        price = amount[num] * 100
        while node != 0:
            remain_price = int(price * 0.1)
            get_price = price - remain_price

            if remain_price < 1:
                get_price = price
            answer[node-1] += get_price
            if get_price == price:
                break

            price = remain_price
            node = v[node]
    return answer





enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

res = solution(enroll, referral, seller, amount)

print('res', res)