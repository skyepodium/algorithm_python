import pandas as pd
from sklearn.metrics import log_loss
from sklearn.ensemble import RandomForestClassifier

a = [1, 2, 3, 4, 1, 2]
b = [1, 2, 3, 4, 5, 5]

train_data = {
    'data': a,
    'target': b
}

train = pd.DataFrame(
            data=train_data
        )

a = [1, 2, 3, 4, 1, 2]
b = [1, 2, 3, 4, 5, 5]

test_data = {
    'data': a,
    'target': b
}

test = pd.DataFrame(
            data=test_data
        )


train_x = train.drop(columns=["target"])
train_y = train["target"]
test_x = train.drop(columns=["target"])
test_y = train["target"]


rf = RandomForestClassifier()
rf.fit(train_x.values.reshape(-1, 1), train_y)
preds_proba = rf.predict_proba(test_x.values.reshape(-1, 1))

print(test_y)
print(test_y.shape)
print(preds_proba)
print(preds_proba.shape)

log_loss_result = log_loss(test_y, preds_proba)

print(f"log_loss_result: {log_loss_result}")

import numpy as np
print(-1 * np.log(1))

result1 = -1 * np.log(0.99)
result2 = -1 * np.log(0.5)
result3 = -1 * np.log(0.1)

total_result = result1 + result2 + result3
print("total logloss", total_result / 3)

a = np.array([1, 3, 2])
print(a)
b = np.array([[0.99, 0, 0.01], [0, 0.5, 0.5], [0.9, 0.1, 0]])
print(b)

log_loss_result = log_loss(a, b)
print(f"log_loss_result: {log_loss_result}")

a = np.array([1, 2, 3])
print(a)
b = np.array([[0, 0, 1], [1, 0, 0], [1, 0, 0]])
print(b)

log_loss_result = log_loss(a, b)
print(f"log_loss_result: {log_loss_result}")

a = 1e-15
print(-np.log(a))

a = np.array([1, 3, 2])
print(a)
b = np.array([[0.99, 0, 0.01], [0, 0.5, 0.5], [0.9, 0.1, 0]])
print(b)

res = (-np.log(0.99) + -np.log(0.5) + -np.log(0.1)) / 3
print(res)