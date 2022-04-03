from mxnet import np, npx

npx.set_np()

print("Hello world")
x=np.arange(12)
print(x)

print(f"longitd {x.shape}")

print("total de elementos del tensor")
print(x.size)

print("cambiar la forma de un tensor sin modificar sus valores y tamaño")
x = x.reshape(3,4)
print(x)


print("creacion de un tensor con valores en 0")
y = np.zeros((1,3,4));
print(y)

print("creacion de un tensor con valores en 1")
y = np.ones((1,3,4))
print(y)

print("muetras al azar en un tensor")
y=np.random.normal(0,1,size=(3,4))
print(y)

print("Espesificando valores exactos para cada elemento en el tensor")
y = np.array([[2,5,1],[1,2,3,]])
print(y)

#suma de matrices 
print("suma de matrizes")
m1 = np.array([1,2,3,4,10])
m2 = np.array([1,2,3,4,10])
print(m1+m2)
