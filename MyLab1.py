import numpy as np

fname = 'mat.csv'

#MyMatrix = np.random.randint(100, size=(10,10))
#np.savetxt(delimiter=',', fname=fname,fmt='%1.1i', X=MyMatrix)

mat = np. loadtxt(delimiter=',', fname=fname)
print(mat)

#определяем максимум и минимум
min_mat, max_mat = np.min(mat), np.max(mat)

#определяем их координаты
min_coord,max_coord = np.where(mat==min_mat), np.where(mat==max_mat)

#меняем их местами
mat[max_coord],mat[min_coord] = min_mat, max_mat

print('result:\n', mat)