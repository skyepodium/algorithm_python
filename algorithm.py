from tensorflow import keras
from keras.layers import SimpleRNN, Dense, Input
from keras.models import Model


# 모델 생성
Inputs = Input(shape=(28, 28))
x1 = SimpleRNN(64, activation="tanh")(Inputs)
x2 = Dense(10, activation="softmax")(x1)
model = Model(Inputs, x2)

# 모델 저장 경로
SAVE_PATH = "./params.h5"

# 모델 저장
# model.save(SAVE_PATH)
model.save_weights(SAVE_PATH)

# 모델 불러오기
# new_model = keras.models.load_model(SAVE_PATH)
#
# # 모델 요약 정보 확인
# new_model.summary()