#Spiegazioni lambda function

if __name__ == "__main__":
    
    #Per lunghezza
    print("Sort per lunghezza: ")
    example = ["cacca", "Abacoladro", "PorcoDioCantante", "abacoladro", "DioZucca"]
    example.sort(key = lambda x : len(x))
    print("\t " + str(example))
    
    #Per ordine alfabetico senza contare le maiuscole
    print("Sort per ordine alfabetico senza contare le maiuscole: ")
    example = ["cacca", "Abacoladro", "PorcoDioCantante", "abacoladro", "DioZucca"]
    example.sort(key = lambda x : x.lower())
    print("\t " + str(example))
    
    #Per ordine di lunghezza e poi per ordine alfabetico senza contare la maiuscole
    print("Sort per ordine di lunghezza e poi per ordine alfabetico senza contare la maiuscole")
    example = ["cacca", "AbacoladroAAAAAAA", "PorcoDioCantante", "abacoladro", "DioZucca", "AAAAAAAAAA"]
    example.sort(key = lambda x : (len(x), x.lower()), reverse = True)
    print("\t " + str(example))
    
    #Per il modulo
    print("Sort per il modulo")
    example = [1, 3, -2, -6, 2]
    example.sort(key = lambda x : x * -1 if x < 0 else x)
    print("\t " + str(example))
    
    #Per secondo elemento della tupla
    print("Sort per secondo elemento della tupla")
    example = [(1, 2, 3), (1, -4, 3), (1, 0, 3), (1, 7, 3), (1, 5, 3)]
    example.sort(key = lambda x : x[1])
    print("\t " + str(example))
