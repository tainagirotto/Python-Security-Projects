# Analise do site -top 10 de palavras mais usadas.

import requests
from bs4 import BeautifulSoup # trabalho com html e xml
import operator
from collections import Counter


def start(url):
    # armazenar todo cont do site
    wordlist = []
    source_code = requests.get(url).text
    # requisita os dados do site e transforma em html:
    soup = BeautifulSoup(source_code, 'html.parser')
    # procurar tudo que existe em div e class:
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text # joga pra content e transforma em string

        words = content.lower().split() #split -> cada conteudo será uma linha

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    # função para remover os símbolos indesejados
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-=+{[}]|\"<>:.,;/? '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    # contagem de palavras e faz um top 20 de palavras mais usadas
    for key, value in sorted(word_count.items(), key= operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    #start('https://www.djangoproject.com/')
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')