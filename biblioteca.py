#usos w aplicações de bibliotecas
import math
#potência
print("2^5 = "+ str(math.pow(2,5)))
#função teto
print(math.ceil(3.45))
#função piso
print(math.floor(5.25))
#valor absoluto
print(math.fabs(-10.33))
print(math.log(1000))

#vetor
import numpy as np
u = np.array([1,2,4])
v = np.array([2,3,6])

print("Vector addition with amother vector ---> " + str(u+v))
print("Vector sum --> " +str(np.sum(u * v)))

import scipy.optimize as opt
import numpy as np

# Dados brutos inseridos manualmente pelo usuário
I =[4.0, 3.5, 3.0, 2.5, 2.0]
B =[1.31, 1.14, 0.97 ,0.81, 0.76]
IError = [0.2, 0.2, 0.2, 0.2, 0.2]
BError = [0.03, 0.02, 0.04, 0.02, 0.05]

print("estimated B for each error \n")
for i in range (5) :
  print(str(I[i]) + "+-" + str(IError[i]) + ": " + str(B[i]) + "+-" + str(BError[i]))
  
# Aplicar a biblioteca Numpy para formatar a lista de dados brutos em uma matriz multidimensional
 # Isto é necessário para a otimização das funções e para o uso adequado do pacote Scipy
xdata = np.array(I)
ydata = np.array(B)
xerror = np.array(IError)
yerror= np.array(BError)

# Definir função linear para ajuste
def func(h, m, b):
    return m*h + b

# w é uma matriz com informações sobre o valor da inclinação e do y-intercepção
w,u = opt.curve_fit(func, xdata, ydata, sigma=yerror)
print("\n")
print("Best fit parameters: ")
print("m = " + str(w[0]))
print("b = " + str(w[1]))

