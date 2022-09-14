def creare_lista_int():
    n = int(input('Numarul de elemente: '))
    lista_locala = []
    for i in range(n):
        element = input(f'Elementul {i+1} este: ')
        try:
            lista_locala.append(int(element))
        except ValueError:
            while not element.isnumeric():
                element=input("Introdu un nr. int:")
            lista_locala.append(int(element))
    return lista_locala
    
print(creare_lista_int())

def creare_lista_float():
    n = int(input('Numarul de elemente: '))
    lista_locala = []
    for i in range(n):
        element = input(f'Elementul {i+1} este: ')
        try:
            lista_locala.append(float(element))
        except ValueError:
            while not element.isdecimal():
                element=input("Introdu un nr. int:")
            lista_locala.append(float(element))
    return lista_locala
    
print(creare_lista_float())
