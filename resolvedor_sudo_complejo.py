import numpy as np

M = np.array([[4, 0, 9, 3, 7, 0, 0, 0, 0],
              [1, 0, 0, 4, 2, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 0, 1, 0],
              [5, 0, 0, 0, 0, 6, 0, 7, 0],
              [0, 6, 2, 0, 0, 0, 5, 8, 0],
              [0, 1, 0, 2, 0, 0, 0, 0, 3],
              [0, 2, 0, 8, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 5, 2, 0, 0, 8],
              [0, 0, 0, 0, 9, 7, 6, 0, 5]], dtype=int)

# Muestro el sudoku
def mostrar_sudo(sudoku):
    for fila in sudoku:
        print (fila)

# Metodo resolutivo
def resolucion(M):
    
    # Definir elementos que vamos a reutilizar
    def arreglos(i, j, arr_fila, arr_columna):
        for k in range(9):
            arr_fila[k] = M[i, k]
            arr_columna[k] = M[k, j]
        return arr_fila, arr_columna
    
    # Ubicar elemento en submatriz
    def busqueda_submatriz(i, j, arr_aux):
        k = 0
        for g in range(3):
            for h in range(3):
                ubi_sub_fila, ubi_sub_col = (i // 3 * 3 + g), (j // 3 * 3 + h)
                arr_aux[k] = M[ubi_sub_fila,ubi_sub_col]
                k += 1
        return arr_aux
    
    bandera = True
    while bandera:
        bandera = False
        for i in range(9):
            for j in range(9):
                if M[i, j] == 0:
                    arreglo = np.arange(1, 10)
                    arr_fila = np.empty(9, dtype=int)
                    arr_columna = np.empty(9, dtype=int)
                    
                    arr_aux = np.empty(9, dtype=int)
                    busqueda_submatriz(i, j, arr_aux)
                    
                    arreglos(i, j, arr_fila, arr_columna)
                    inter_1 = np.union1d(arr_fila, arr_columna)
                    inter_2 = np.union1d(inter_1, arr_aux)
                    resultado = np.setdiff1d(arreglo, inter_2)
                    
                    for numero in resultado:
                        M[i, j] = numero
                        if resolucion(M):
                            return True
                        M[i, j] = 0  # Retroceder si no lleva a una solución válida
                    return False
    return True

mostrar_sudo(M) 
                        
resolucion(M)
print("\nResolviendo Sudoku..\n")

mostrar_sudo(M)