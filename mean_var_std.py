import numpy as np

def calculate(numeros):
    if len(numeros) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(numeros).reshape(3, 3)
    
    funciones = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    calculations = {key: [func(matriz, axis=0).tolist(), 
                          func(matriz, axis=1).tolist(), 
                          func(matriz).tolist()] for key, func in funciones.items()}
    
    return calculations
