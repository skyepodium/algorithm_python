from tensorflow import keras
import matplotlib.pyplot as plt

# 데이터를 불러오는 코드를 작성해주세요.
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 데이터의 크기를 shape 함수를 통해 출력해주세요.
print(f"train_images: {train_images.shape}")
print(f"train_labels.shape: {train_labels.shape}")

print(f"test_images.shape: {test_images.shape}")
print(f"test_labels.shape: {test_labels.shape}")

"""
train_images: (60000, 28, 28)
train_labels.shape: (60000,)
test_images.shape: (10000, 28, 28)
test_labels.shape: (10000,)
"""
#(BHW) - 1. batch, 2. height, 3. width
"""
이미지 데이터는 3가지의 속성을가집니다.
순서대로 1. batch, 2. height, 3. width
"""

# 28x28의 흑백 이미지를 plt를 이용하여 출력하는 코드를 작성해보세요.
plt.figure()
plt.imshow(train_images[1])
plt.colorbar()
plt.grid(True)
plt.show()
print(train_labels[1])