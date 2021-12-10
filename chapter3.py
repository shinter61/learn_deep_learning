import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    y = x > 0
    return y.astype(int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
# y = sigmoid(x)
y = relu(x)

plt.plot(x, y)
plt.ylim(-0.1, 5.1)
# plt.show()

A = np.array([1,2,3,4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))
print(B.shape)

C = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(C.shape)
print(B.shape)
print(np.dot(C, B))

A = np.array([[1,2],[3,4],[5,6]])
B = np.array([7,8])
print(A.shape)
print(B.shape)
print(np.dot(A,B))

print("-------------")
X = np.array([1,2])
print(X.shape)

W = np.array([[1,3,5],[2,4,6]])
print(W)
print(W.shape)

Y = np.dot(X,W)
print(Y)
