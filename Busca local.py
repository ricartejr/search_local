from funciones.func import copycopy
from os import path, walk


contador = 0
des_local = r'D:/VIDEOS/Videos YT/1 - Python Downloads/BuscasPython'

print('\n\nOpciones: Buscar por nombre o extension.\n\n')
buscar_en = path.abspath(input('Buscar en  -> ').strip())
buscar_por = str(input('Buscar por -> ').lower().strip())

if path.exists(buscar_en) == True:
    for camino, carpetas, archivos in walk(f'{buscar_en}', topdown=True, onerror=None):
        for archivo in archivos:
            if archivo.lower().find(buscar_por) != -1:
                contador += 1
                try:
                    des_arq = path.abspath(f'{des_local}/{buscar_por}')
                    copy_arq = path.abspath(f'{camino}/{archivo}')
                    # copycopy(copy_arq, des_arq, des_local, buscar_por, archivo)
                except KeyboardInterrupt as error:
                    print('Cancelado por el usuario...')
                    break
                else:
                    print(f'{"":-<160}')
                    print('->', path.abspath(f'{camino}/{archivo}'))

else:
    print(f'\n-> {buscar_en} Invalido.')

print(f'\n-> [{contador}] - [{buscar_por}] encontrados.\n')
