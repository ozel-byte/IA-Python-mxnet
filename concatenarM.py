from mxnet import np,npx

X = np.arange(12).reshape(3,4)


Y = np.array([[1,2,3,4],[4,6,8,7],[6,3,1,3]])

print(np.concatenate([X,Y],axis=0))

print("usando axios 1")
print(np.concatenate([X,Y],axis=1))

print(X==Y)


prueba1M = np.array([[2,5,4,1],[10,5,1,1]])
prueba2M = np.array([[5,5,5,5],[2,3,4,1]])
print("comparar matriz")
print(prueba1M==prueba2M)

print("suma de todos los elementos de prueba")

print("prueba de longitud")
print(prueba1M.shape)
t = np.arange(12)
print(t.shape)