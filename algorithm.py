# and gate
def and_gate(x1, x2):
    # 입력값 x1에 대한 가중치 w1, x2에 대한 가중치 w2
    w1, w2 = 0.6, 0.6

    # bias 편향값
    b = -0.7

    # 연산 결과
    result = x1*w1 + x2*w2 + b

    # 결과가 0보다 작거나 같으면 0, 0보다 크면 1을 반환합니다.
    return 0 if result <= 0 else 1


# or gate
def or_gate(x1, x2):
    # 입력값 x1에 대한 가중치 w1, x2에 대한 가중치 w2
    w1, w2 = 0.6, 0.6

    # bias 편향값
    b = -0.5

    # 연산 결과
    result = x1*w1 + x2*w2 + b

    # 결과가 0보다 작거나 같으면 0, 0보다 크면 1을 반환합니다.
    return 0 if result <= 0 else 1


def nand_gate(x1, x2):
    # 입력값 x1에 대한 가중치 w1, x2에 대한 가중치 w2
    w1, w2 = 0.6, 0.6

    # bias 편향값
    b = -0.7
    # 연산 결과
    result = x1*w1 + x2*w2 + b

    # 결과가 0보다 작거나 같으면 1, 0보다 크면 0을 반환합니다.
    return 1 if result <= 0 else 0


# 입력값 목록을 튜플 리스트로 만듭니다.
input_list = [(0, 0), (0, 1), (1, 0), (1, 1)]


# 반복문을 순회하면서 입력값을 가져옵니다.
for x1, x2 in input_list:
    # or gate의 결과를 저장하고s
    or_result = or_gate(x1, x2)

    # nand gate의 결과를 저장하고
    nand_result = nand_gate(x1, x2)

    xor_result = and_gate(or_result, nand_result)

    # 출력합니다.
    print(f"입력값: {x1} {x2} / 결과: {xor_result}")