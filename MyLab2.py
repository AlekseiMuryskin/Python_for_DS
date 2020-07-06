import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import ndimage

pth='c:\\Users\\aleksey\\Desktop\\ABC\\'

a=0.2
b=-0.4
c = lambda x: 1 if x > 0 else 0

w = np.zeros(10000)  #веса
D = None
Y0 = np.array([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], dtype=float)  #у для обучающей выборки

def f(x):
    s = b + np.sum(x @ w)
    return c(s)

def train():
    global w
    _w = w.copy()
    for x, y in zip(D, Y0):
        w += a * (y - f(x)) * x
    return (w != _w).any()

print(w)
for name in os.listdir(pth):
    img = plt.imread('{}{}'.format(pth, name))
    #print(img)
    xs = np.dot(img[...,:3], [1, 1, 1]) .flatten()
    if D is None:
        D = xs
    else:
        D = np.vstack((D, xs))


#print(D)

while train():
    print(w)

for i in np.arange(0,90,10):
    j=0

    for name in os.listdir(pth):
        pos = 0
        neg = 0
        img = plt.imread('{}{}'.format(pth, name))
        rotated = ndimage.rotate(img, i, reshape=0)
        ac = np.binary_repr(ord(name.split('.')[0]))[2:]
        #print("Бинарный код тестовой буквы 10",ac)
        xs = np.dot(img[..., :3], [1, 1, 1]) .flatten()  #Привели к ч/б умножив срез на [1, 1, 1]+ превращаем матрицу в вектор
        result = f(xs)
        ac=Y0[j]
        j+=1

        if result == ac:
            pos += 1
        else:
            neg += 1

    print("Угол поворота", i)
    print("Корректно распознал", pos / (pos + neg) * 100)
    print("Ошибочно распознал", neg / (pos + neg) * 100)