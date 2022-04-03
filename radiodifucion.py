from mxnet import np,npx

a = np.arange(3)
print("----")
a = a.reshape(3,1)
print(a)
print("-----")
b = np.arange(2)
print("-----")
b = b.reshape(1,2)
print(b)
print("-----")
print(a+b)