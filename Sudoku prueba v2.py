import numpy as np

M = np.array([[1, 0, 6, 0, 0, 2, 3, 0, 0],
              [0, 5, 0, 0, 0, 6, 0, 9, 1],
              [0, 0, 9, 5, 0, 1, 4, 6, 2],
              [0, 3, 7, 9, 0, 5, 0, 0, 0],
              [5, 8, 1, 0, 2, 7, 9, 0, 0],
              [0, 0, 0, 4, 0, 8, 1, 5, 7],
              [0, 0, 0, 2, 6, 0, 5, 4, 0],
              [0, 0, 4, 1, 5, 0, 6, 0, 9],
              [9, 0, 0, 8, 7, 4, 2, 1, 0]], dtype=int)



# Menu interactivo:

def menu():  

    print("""
            Ingresa 1: Resolver sudoku.
            Ingresa 0: Para salir.
            """)
    
    opcion = int(input("Ingresa tu opción: "))
    
    return opcion

# Programa principal:
def resolver(M):
    band = True
    while band == True:

        opcion = menu()

        if opcion == 1:
            
            def resolucion(M):
                
                # Definos elementos que vamos a reutilizar:    
                def arreglos(i, j, arr_fila, arr_columna):
                    for g in range(9):  
                        for h in range(9):
                            if g == i and h == j:
                                for k in range(9):
                                    arr_fila[k] = M[i,k]  
                                    arr_columna[k] = M[k,j]
                    return arr_fila, arr_columna
            
                def busqueda_submatriz(i,j,arr_aux):
                    k = 0
                    if i < 3 and j < 3: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[0, 0, g, h]
                                k += 1
                    elif i < 3 and j >= 3 and j < 6: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[0, 1, g, h]
                                k += 1
                    elif i < 3 and j >= 6 and j < 9: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[0, 2, g, h]
                                k += 1                                              # Busco por la primera fila, en las tres primeras matrices
                    elif i >= 3 and i < 6 and j < 3: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[1, 0, g, h]
                                k += 1
                    elif i >= 3 and i < 6 and j >= 3 and j < 6: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[1, 1, g, h]
                                k += 1
                    elif i >= 3 and i < 6 and j >= 6 and j < 9: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[1, 2, g, h]
                                k += 1                                              # Busco por la segunda fila, en las tres segundas matrices
                    elif i >= 6 and i < 9 and j < 3: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[2, 0, g, h]
                                k += 1
                    elif i >= 6 and i < 9 and j >= 3 and j < 6: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[2, 1, g, h]
                                k += 1
                    elif i >= 6 and i < 9 and j >= 6 and j < 9: 
                        for g in range(3):
                            for h in range(3):
                                arr_aux[k] = arreglo_matrices[2, 2, g, h]
                                k += 1                                              # Busco por la tercera fila, en las tres terceras matrices
                    
                    return arr_aux                                            # Retorno submatriz

                bandera = True
                while bandera:
                    bandera = False
                    for i in range (9):
                        for j in range(9):
                            if M[i,j] == 0:

                                arreglo = np.arange(1, 10)   

                                arr_fila = np.empty(9, dtype=int)  
                                arr_columna = np.empty(9, dtype=int)
                                arr_aux = np.empty(9, dtype=int)
                                
                                # Dividir las filas en 3 partes iguales
                                filas = np.split(M, 3)

                                # Dividir cada parte en 3 partes iguales
                                arreglo_matrices = np.array([np.split(fila, 3, axis=1) for fila in filas])

                                busqueda_submatriz(i,j, arr_aux)
                                
                                arreglos(i, j, arr_fila, arr_columna)

                                inter_1 = np.union1d(arr_fila, arr_columna)                        
                                inter_2= np.union1d(inter_1, arr_aux)              

                                resultado = np.setdiff1d(arreglo, inter_2)

                                print("\nLos posibles números son:", resultado)
                                print(arr_fila)
                                print(arr_columna)
                                print(arr_aux)
                                
                                print("VALOR DE I Y J", i ,j)

                                if len(resultado) == 1:
                                    print("PASE1", M[i,j])
                                    M[i,j] = resultado[0]
                                    bandera = True
                                    intercambios = True
                                    print("PASE2", resultado[0])
                return M    
            
            resolucion(M)
            
            print("El sudoku queda: \n", M)

        elif opcion == 0:

            print("Hasta pronto!\n")
            band = False
    
resolver(M)


