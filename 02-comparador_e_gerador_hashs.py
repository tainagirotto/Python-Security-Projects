import hashlib

def linha():
    print('-=' * 30)

def comparador(arquivo1, arquivo2):
    hash1 = hashlib.new('ripemd160')  # new -> passa uma string pra falar qual algoritmo de hash vai usar sha1, etc
    hash1.update(
        open(arquivo1, 'rb').read())  # update -> comparação do hash - passar o arquivo ou frase que será comparada.

    hash2 = hashlib.new('ripemd160')
    hash2.update(open(arquivo2, 'rb').read())

    # comparando os hashs
    # a função digest -> faz um resumo dos dados passados pelo método update
    if hash1.digest() != hash2.digest():
        print(f'O arquivo: {arquivo1} é diferende do arquivo: {arquivo2}')
        print(f'O hash do arquivo a.txt é: {hash1.hexdigest()}')
        print(f'O hash do arquivo b.txt é: {hash2.hexdigest()}')
    else:
        print(f'O arquivo {arquivo1} é igual ao arquivo {arquivo2}')
        print(f'O hash do arquivo a.txt é: {hash1.hexdigest()}')
        print(f'O hash do arquivo b.txt é: {hash2.hexdigest()}')
    linha()
    menu_princ = input('Deseja voltar ao menu principal? [S/N] ')
    if menu_princ in 'Ss':
        main()
    else:
        print('<<< PROGRAMA FINALIZADO >>>')

def gerador():
    while True:
        string = input('Digite o texto a ser convertido: ')
        print('###      ESCOLHA O TIPO DE HASH       ###')
        menu = int(input('''
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA 512
        Digite o número a ser gerado: '''))
        print('-' * 90)
        if menu == 1:
            resultado = hashlib.md5(string.encode('utf-8'))
            print(f'O hash MD5 da string {string} é: {resultado.hexdigest()}')
        elif menu == 2:
            resultado = hashlib.sha1(string.encode('utf-8'))
            print(f'O hash SHA1 da string {string} é: {resultado.hexdigest()}')
        elif menu == 3:
            resultado = hashlib.sha256(string.encode('utf-8'))
            print(f'O hash SHA256 da string {string} é: {resultado.hexdigest()}')
        elif menu == 4:
            resultado = hashlib.sha512(string.encode('utf-8'))
            print(f'O hash SHA512 da string {string} é: {resultado.hexdigest()}')
        else:
            print('Opção incorreta. Tente novamente')
        print('-' * 90)
        resp = input('Deseja voltar ao MENU DE HASH? [S/N]')
        print('-' * 90)
        if resp in 'Nn':
            print('<<< FINALIZANDO GERADOR DE HASHS >>>')
            break
    linha()
    menu_princ = input('Deseja voltar ao MENU PRINCIPAL? [S/N] ')
    if menu_princ in 'Ss':
        main()
    else:
        print('<<< PROGRAMA FINALIZADO >>>')

def main():
    print(' ######   MENU PRINCIPAL ###### '.center(20))
    op = int(input('''
    1- Comparador de hashs
    2- Gerador de hashs
    Digite a opção desejada: '''))
    linha()
    if op == 1:
        comparador('a.txt', 'b.txt')
    elif op == 2:
        gerador()
    else:
        print('<<< Opção inválida! >>>')

if __name__ == '__main__':
    main()

