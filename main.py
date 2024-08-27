import numpy as np
import mean_var_std as mvs

l_n = np.array([])
for i in range(9):
    num = int(input(f"Ingrese el numero {i+1}:"))
    l_n = np.append(l_n, num)
result = mvs.calculate(l_n)
print(result)