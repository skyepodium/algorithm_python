# numpy를 불러옵니다.
import numpy as np

# 학습 시킬 train 데이터
# 1일때 1, 2일때 2, 3일때 3을 내놓도록 만들었습니다.
train_x = np.array([1, 2, 3])
train_y = np.array([1, 2, 3])

# 검증에 사용할 데이터
# 마찬가지로 1일때 1, 2일때 2, 3일때 3을 내놓도록 만들었습니다.
valid_x = np.array([3, 2, 1])
valid_y = np.array([3, 2, 1])

# 사이킷런의 RandomForestClassifier를 가져옵니다.
from sklearn.ensemble import RandomForestClassifier

# 모델 생성
rf = RandomForestClassifier()

# 학습
rf.fit(train_x.reshape(-1, 1), train_y)

# predict_proba로 확률 예측
proba_result = rf.predict_proba(valid_x.reshape(-1, 1))
print("proba_result", proba_result)

# 확률에 대해 가장 큰값 가져오기
res_list = []
for arr in proba_result:
    res_class = np.argmax(arr) + 1
    res_list.append(res_class)

print("res_list", res_list)

# class 예측
predict_result = rf.predict(valid_x.reshape(-1, 1))
print("predict_result", predict_result)