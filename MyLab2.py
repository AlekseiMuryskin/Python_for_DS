import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

#входные параметры
b = -0.4
a = 0.2
MyAngle=10 # угол для которого будет выведена матрица
sigma = lambda x: (x > 1).astype(int)
dig_img = np.dot(plt.imread('dig_img.png')[...,:3],[1,1,1]) # вход, изображение

#вектор обучения
D = []
for i in range(8):
    a = i * 48
    x=  (dig_img[5:104,0+a:48+a] > 1).astype(int).flatten()
    y = (np.array(list(bin(i)[2:].zfill(3))) == '1').astype(int)
    D += [[x,y]]

#матрица весов
w = np.zeros((D[0][0].shape[0],D[0][1].shape[0]))

#функции распознавания и тренировочная
def f(x):
    s = b + x @ w
    return sigma(s)

def train():
    global w
    _w = w.copy()
    for x, y in D:
        i = np.where(x>0)
        w[i] += a * (y - f(x))
    return (w != _w).any()

#тренировка
while train():
    print(w)

print('Распознавание при повороте')
print('Угол \t Доля совпадений')

for angle in np.arange(0,100,20):
    D_rot=[]
    pos = 0
    for dig in range(8):
        a = dig * 48
        rot=ndimage.rotate(dig_img[5:104,0+a:48+a], angle, reshape=0)
        x = (rot > 1).astype(int).flatten()
        D_rot += [[x]]
        if np.array_equal(f(D[dig][0]),f(D_rot[dig][0])):
            pos+=1
    print(angle,'\t',str(pos/8))

#матрица
print('\n')
print(('матрица результатов для угла {} градусов').format(MyAngle))
for i in range(8):
    print('\t'+str(i),end='')

print('\n',end='')

for i in range(8):
    D_rot = []
    print(i, end='\t')
    for j in range(8):
        a = j * 48
        rot = ndimage.rotate(dig_img[5:104, 0 + a:48 + a], MyAngle, reshape=0)
        x = (rot > 1).astype(int).flatten()
        if np.array_equal(f(D[i][0]),f(x)):
            print('1\t',end='')
        else:
            print('0\t',end='')

    print('\n',end='')
