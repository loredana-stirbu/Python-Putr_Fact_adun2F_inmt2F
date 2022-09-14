def creare_lista():
    n = int(input('Numarul de elemente: '))
    lista_locala = []
    lista2=[]
    for i in range(n):
        element = input(f'Elementul {i} este: ')
        lista2.append(element)
        integer_map=map(int,lista2)
        integer_list=list(integer_map)
    if isinstance(integer_list, int) == True:
        lista_locala.append(integer_list[i])
    return lista_locala
    
print(creare_lista())