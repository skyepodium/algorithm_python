import numpy as np


class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=5000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.w = 0.0
        self.b = 0.0

    def fit(self, x_train, y_train):
        w = self.w
        b = self.b
        learning_rate = self.learning_rate
        epochs = self.epochs

        n_data = len(x_train)

        for i in range(epochs):
            hypothesis = x_train * w + b
            cost = np.sum((hypothesis - y_train) ** 2) / n_data
            gradient_w = np.sum((w * x_train - y_train + b) * 2 * x_train) / n_data
            gradient_b = np.sum((w * x_train - y_train + b) * 2) / n_data

            w -= learning_rate * gradient_w
            b -= learning_rate * gradient_b

            if i % 100 == 0:
                print('Epoch ({:10d}/{:10d}) cost: {:10f}, W: {:10f}, b:{:10f}'.format(i, epochs, cost, w, b))

        self.w = w
        self.b = b

    def predict(self, test_x):
        w = self.w
        b = self.b

        y_pred = test_x * w + b
        return y_pred


lr = LinearRegression()

train_x = np.array([1., 2., 3., 4., 5., 6.])
train_y = np.array([9., 16., 23., 30., 37., 44.])
test_x = np.array([2, 3, 4, 5, 6, 7])
print(lr)
lr.fit(train_x, train_y)

result = lr.predict(test_x)
print('result', result)
from sklearn.linear_model import LinearRegression as real
lo = real()
lo.fit(train_x.reshape(-1, 1), train_y)
real_pred = lo.predict(test_x.reshape(-1, 1))
print("real_pred", real_pred)