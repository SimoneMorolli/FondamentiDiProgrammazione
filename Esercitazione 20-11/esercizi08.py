# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')



# Scrivere una funzione che data una matrice di interi, restituisce la matrice trasposta
# Ad esempio:
# 5 2 9    ->  5 3
# 3 1 0        2 1
#              9 0
def transpose(m : List[List[int]]) -> List[List[int]]:
    resultMatrix = []

    for i in range(len(m[0])):
        tempList = []
        for j in range(len(m)):
            tempList.append(m[j][i])
        resultMatrix.append(tempList)
    return resultMatrix
            
        
            

# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente alla somma fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       2 2 2
#     2 1 1   +    2 3 1   =   4 4 2
#     0 1 1        4 2 2       4 3 3
#     1 1 2        1 2 3       2 3 5
# Restituire None se le due matrici non possono essere sommate.
def matrix_matrix_sum(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    resultList = []
    j = 0
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for raw in A:
            tempList = []
            for i in range(len(raw)):
                tempList.append(raw[i] + B[j][i])
            j += 1
            resultList.append(tempList)
    else:
        resultList = None
    return resultList
        
        
        

# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente al prodotto fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       5  4 3
#     2 1 1   x    2 3 1   =   8  9 5
#     0 1 1        4 2 2       6  5 3
#     1 1 2                    11 9 6
# Restituire None se le due matrici non possono essere moltiplicate.
def matrix_matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    collNumA = len(A[0])
    collNumB = len(B[0])
    rawNumA = len(A)
    rawNumB = len(B)
    resultMatrix = []
    
    if collNumA == rawNumB:
        for rawA in A:  
            j = 0
            temp = 0
            count = 0
            tempList = []
            while count < collNumB:
                for i in range(rawNumB):
                    temp += rawA[i] * B[i][j]
                tempList.append(temp)
                temp = 0
                j += 1
                count += 1  
            resultMatrix.append(tempList)
    else:
        resultMatrix = None
    return resultMatrix

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine rotata di 90 gradi a destra e invertita rispetto l'asse verticale.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_rotate_right_and_flip_v(img_in: str, img_out : str):
    imgStart = images.load(img_in)
    newImage = newMatrixEmpty(len(imgStart), len(imgStart[0]))
    newImgRow = len(newImage)
    imgStartColl = len(imgStart[0])
    newImgColl = len(newImage[0])
    imgStartRow = len(imgStart)
    
    
    
    for i in range(imgStartRow):
        for j in range(imgStartColl):
            newImage[j][imgStartRow - i - 1] = imgStart[i][j]

    newFlippedImg = newMatrixEmpty(newImgColl, newImgRow)
    for i in range(newImgRow):
        for j in range(newImgColl):
            newFlippedImg[i][newImgColl - j - 1] = newImage[i][j]
    
    images.save(newFlippedImg, img_out)
    
    
def newMatrixEmpty(coll: int, row: int):
    newMatrix = [[0 for _ in range(coll)] for _ in range(row)]
    return newMatrix
    
# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine con i canali rosso e blu invertiti.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_invert_channels(img_in: str, img_out : str):
    startImg = images.load(img_in)
    newImg = []
    
    for row in startImg:
        tempList = []
        for element in row:
            newTuple = (element[2], element[1], element[0])
            tempList.append(newTuple)
        newImg.append(tempList)
    images.save(newImg, img_out)

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui ognuno dei 3 canali è quantizzato su 128 possibili valori (cioè, ogni canale può solo assumere 128 valori anzichè 256).
# Ad esempio, (21, 126, 3) diventa (10, 63, 2)
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_quantize(img_in: str, img_out : str):
    startImg = images.load(img_in)
    newImg = []
    
    for row in startImg:
        tempList = []
        for element in row:
            newTuple = (element[0] // 2, element[1] // 2, element[2] // 2)
            tempList.append(newTuple)
        newImg.append(tempList)
    images.save(newImg, img_out)

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui la metà destra dell'immagine è scambiata con la metà sinistra.
# (Cioè, le colonne nel range [0, N/2] diventano le colonne [N/2, N] nella nuova immagine,
# e le colonne [N, N/2] nella vecchia immagine diventano le colonne [0, N/2] nella nuova immagine).
# Si può assumere che l'immagine abbia un numero di colonne divisibile per 2.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_invert_half(img_in: str, img_out : str):
    startImg = images.load(img_in)
    newHalfLeftImg = newMatrixEmpty(len(startImg[0]) // 2, len(startImg))
    newHalfRightImg = newMatrixEmpty(len(startImg[0]) // 2, len(startImg))
    newImg = newMatrixEmpty(len(startImg[0]), len(startImg))
    
    for i in range(len(startImg)):
        for j in range(len(startImg[0]) // 2):
            newImg[i][j + len(startImg[0]) // 2] = startImg[i][j]
            newImg[i][j] = startImg[i][j + len(startImg[0]) // 2]


    images.save(newImg, img_out)

# Test funzioni
check_test(transpose, [[5, 3], [2, 1]], [[5, 2], [3, 1]])
check_test(transpose, [[5, 3], [2, 1], [9, 0]], [[5, 2, 9], [3, 1, 0]])
check_test(transpose, [[5, 3]], [[5], [3]])
check_test(transpose, [[5], [3]], [[5, 3]])
check_test(matrix_matrix_sum, [[2, 2, 2], [4, 4, 2], [4, 3, 3], [2, 3, 5]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2], [1, 2, 3]])
check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2], [2, 3], [4, 2], [1, 2]])
check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
check_test(matrix_matrix_mul, [[5, 4, 3], [8, 9, 5], [6, 5, 3], [11, 9, 6]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
check_test(matrix_matrix_mul, [[5], [8], [6], [11]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1], [2], [4]])
check_test(matrix_matrix_mul, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1]])
img_rotate_right_and_flip_v("img1.png", "img1_rotate_flip.png")
img_invert_channels("img1.png", "img1_invert_channels.png")
img_quantize("img1.png", "img1_quantized.png")
img_invert_half("img1.png", "img1_inverted_half.png")