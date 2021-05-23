# numpy를 불러옵니다.
import numpy as np

# 직접 logloss를 계산할 함수를 생성합니다.
# answer_array는 정답 array
# proba_array는 확률 array
def my_logloss(answer_array, proba_array):

    # 0이면 무한대 값이 나오기 때문에 0에 가까운 값으로 치환해줍니다.
    MIN_VALUE = 1e-15

    # array의 크기를 가져옵니다.
    size = answer_array.shape[0]

    # 반복문을 사용해서 logloss의 합을 계산합니다.
    logloss_sum = 0
    # zip함수로 묶으면 함께 순회할 수 있습니다.
    for answer, arr in zip(answer_array, proba_array):
        proba = arr[answer - 1]

        # 0이면 무한대 값이 나오기 때문에 0에 가까운 값으로 치환해줍니다.
        if proba <= MIN_VALUE:
            proba = MIN_VALUE

        # 음의 로그함수에 넣어서 logloss 계산
        logloss_sum += -np.log(proba)

    # logloss의 평균 계산
    result = logloss_sum / size

    # 반환
    return result

# answer_array는 정답 array
# proba_array는 확률 array
answer_list = np.array([1, 3, 2])
proba_list = np.array([[0.99, 0, 0.01], [0, 0.5, 0.5], [0.9, 0.1, 0]])

# my_logloss 결과 출력
my_logloss_result = my_logloss(answer_list, proba_list)
print('my_logloss', my_logloss_result)


# 비교를 위해 사이킷런의 log_loss 함수를 불러옵니다.
from sklearn.metrics import log_loss

# 사이킷런 결과 확인
sklearn_reslt = log_loss(answer_list, proba_list)
print("sklearn_reslt", sklearn_reslt)

"""
my_logloss 1.0019275364691642
sklearn_reslt 1.001927536469165
"""