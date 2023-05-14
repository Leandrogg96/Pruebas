import numpy as np

M = np.array([[1, 0, 6, 0, 0, 2, 3, 0, 0],
              [0, 5, 0, 0, 0, 6, 0, 9, 1],
              [0, 0, 9, 5, 0, 1, 4, 6, 2],
              [0, 3, 7, 9, 0, 5, 0, 0, 0],
              [5, 8, 1, 0, 2, 7, 9, 0, 0],
              [0, 0, 0, 4, 0, 8, 1, 5, 7],
              [0, 0, 0, 2, 6, 0, 5, 4, 0],
              [0, 0, 4, 1, 5, 0, 6, 9, 0],
              [9, 0, 0, 8, 7, 4, 2, 1, 0]], dtype=int)

# Menu interactivo:

def menu():  

    print("""
            Ingresa 1: Detecta los posibles números en tu sudoku.
            Ingresa 0: Para salir.
            """)
    
    opcion = int(input("Ingresa tu opción: "))
    
    return opcion

# Programa principal:
def principal():

    band = True

    while band == True:

        opcion = menu()

        if opcion == 1:
        
            p = int(input("Ingresa la ubicación de la fila dentro del sudoku: "))
            l = int(input("Ingresa la ubicación de la columna dentro del sudoku: "))

            # Valido que la posicion elegida en el sudoku este realmente vacia
            def validar_posicion(p,l):
                while M[p,l] != 0:
                    print("La posición que elegiste ya tiene un número!\nIngresa otra! ")
                    p = int(input("Ingresa la ubicación de la fila dentro del sudoku: "))
                    l = int(input("Ingresa la ubicación de la columna dentro del sudoku: "))

                return p,l
                
            
            p,l = validar_posicion(p,l)

            # Definos elementos que vamos a reutilizar:    
            arreglo = np.arange(1, 10)   # Creo arreglo auxiliar

            arr_fila = np.empty(9, dtype=int)  #
            print(arr_fila)

            arr_columna = np.empty(9, dtype=int)
            print(arr_columna)

            arr_aux = np.empty(9, dtype=int)
            print(arr_aux)

            # Dividir las filas en 3 partes iguales
            filas = np.split(M, 3)

            # Dividir cada parte en 3 partes iguales
            arreglo_matrices = np.array([np.split(fila, 3, axis=1) for fila in filas])

            print(arreglo_matrices)
            print(arreglo_matrices[0,0,0,0])

            """ 
            Otra manera 
            
            for i in range(3):
                for j in range(3):
                    matriz = M[i*3:(i+1)*3, j*3:(j+1)*3]
                    print(f"Matriz {i*3+j+1}:\n{matriz}\n")
            """

            # Creo 2 arreglos que contienen los numeros contenidos en la fila y columna de la posicion ingresada:

            def arreglos(arr_fila, arr_columna):
                for i in range(9):  
                    for j in range(9):
                        if i == p and j == l and M[i, j] == 0:
                            for k in range(9):
                                arr_fila[k] = M[p,k]  
                                arr_columna[k] = M[k,l]
                return arr_fila, arr_columna
            
            arreglos(arr_fila, arr_columna)

            # Busco en cual de las 9 matrices se encuentra la posicion:

            def busqueda_submatriz(p,l,arr_aux):
                k = 0
                if p < 3 and l < 3: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[0, 0, i, j]
                            k += 1
                elif p < 3 and l >= 3 and l < 6: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[0, 1, i, j]
                            k += 1
                elif p < 3 and l >= 6 and l < 9: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[0, 2, i, j]
                            k += 1                                              # Busco por la primera fila, en las tres primeras matrices
                elif p >= 3 and p < 6 and l < 3: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[1, 0, i, j]
                            k += 1
                elif p >= 3 and p < 6 and l >= 3 and l < 6: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[1, 1, i, j]
                            k += 1
                elif p >= 3 and p < 6 and l >= 6 and l < 9: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[1, 2, i, j]
                            k += 1                                              # Busco por la segunda fila, en las tres segundas matrices
                elif p >= 6 and p < 9 and l < 3: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[2, 0, i, j]
                            k += 1
                elif p >= 6 and p < 9 and l >= 3 and l < 6: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[2, 1, i, j]
                            k += 1
                elif p >= 6 and p < 9 and l >= 6 and l < 9: 
                    for i in range(3):
                        for j in range(3):
                            arr_aux[k] = arreglo_matrices[2, 2, i, j]
                            k += 1                                              # Busco por la tercera fila, en las tres terceras matrices
                
                return arr_aux                                            # Retorno submatriz

            busqueda_submatriz(p,l,arr_aux)
                        
            print("Arreglo con los elementos de la fila contenida en la posición:", arr_fila)
            print("Arreglo con los elementos de la columna contenida en la posición:", arr_columna)
            print("Arreglo con los elementos de la submatriz correspondiente:", arr_aux)

            inter_1 = np.union1d(arr_fila, arr_columna)        # Union entre los arreglos arr_fila y arr_columna                     
            inter_2= np.union1d(inter_1, arr_aux)              # Union entre los arreglos inter_1 y arr_aux

            print("Arreglo con los elementos que estan, al menos una vez, en los anteriores arreglos auxiliares:", inter_2)

            resultado = np.setdiff1d(arreglo, inter_2)

            print("\nLos posibles números son:", resultado)
    
        elif opcion == 0:

            print("Hasta pronto!\n")
            band = False

principal()