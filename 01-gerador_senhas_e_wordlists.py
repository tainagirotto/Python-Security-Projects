import itertools
import random, string


def linha():
    print('-=' * 30)

def gerador_wordlists():
    string = input('String a ser permutada: ')
    resultado = itertools.permutations(string, len(string))
    for i in resultado:
        print(''.join(i))
    linha()
    resp = input('Deseja voltar ao menu principal? [S/N] ')
    if resp in 'Ss':
        main()
    else:
        print('<<< FINALIZANDO PROGRAMA >>>')

def gerador_senhas():
    tamanho = int(input('Digite o tamanho de senha que você deseja: '))
    # ascii letters envolve o lower e o upper/ digts de 0 a 9
    chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+.,;/?'
    rnd = random.SystemRandom()  # os.urandom => gera senhas aleatórias a partir de fontes fornecidas pelo S.O
    print(''.join(rnd.choice(chars) for i in range(tamanho)))
    linha()
    resp = input('Deseja voltar ao menu principal? [S/N] ')
    if resp in 'Ss':
        main()
    else:
        print('<<< FINALIZANDO PROGRAMA >>>')


def main():
    op = int(input('''-------- MENU PRINCIPAL --------
    1- Gerador de wordlists
    2- Gerador de senhas
    Digite a opção desejada: '''))
    linha()
    if op == 1:
        gerador_wordlists()
    elif op == 2:
        gerador_senhas()
    else:
        print('<<< OPÇÃO INVÁLIDA >>> ')

if __name__ == '__main__':
    main()

