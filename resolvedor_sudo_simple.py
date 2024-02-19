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
    while band:
        opcion = menu()

        if opcion == 1:
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

                                print(f'\nLos posibles números para la posición ({i},{j}) son:')
                                print(resultado)

                                if len(resultado) == 1:
                                    M[i, j] = resultado[0]
                                    bandera = True
                
                                     
            resolucion(M)
            
            print('\nEl sudoku tiene solucion!\n')                   
            print(f'El sudoku queda:\n\n {M}')
            break

        elif opcion == 0:
            print('Hasta pronto!\n')
            band = False

resolver(M)