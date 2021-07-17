# oculta arquivos ou diretórios inteiros do sistema operacional

import ctypes


pasta = input('Digite o caminho da pasta a ser ocultada ex (C:/pasta): ')

# atributo hexadecimal
atributo_ocultar = 0x02


retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar) # ou coloca pasta no lugar de 'ocultar.txt'


if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')

