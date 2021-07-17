# Python Security :closed_lock_with_key:
Exercícios realizados durante o curso de Python Security da Digital Innovation One, ministrada pelo professor Bruno de Campos Dias no bootcamp **Banco Carrefour Data Engineer.**


## 01- Gerador de senhas e Wordlists :1234: :capital_abcd:
##### O que são Wordlists? 
São arquivos contendo uma palavra por linha. São utilizados em ataques de força bruta como quebra de autenticação, pode ser usada para testar a autenticação e confidencialidade de um sistema.
##### Bibliotecas usadas: 
- Itertools: fornece condições para iterações como permutação e combinação(Usada no gerador de wordlists)
- Random: gera números pseudoaleatórios para várias distribuições (usada no gerador de senhas)
- String:

## 02- Comparador e gerador de Hashes :key: 
##### O que é Hash? 
O hash é como se fosse um identificador único gerado através de um algoritmo que irá analisar byte a byte de determinado dado para gerar de uma forma única um determinado código que só aquele arquivo terá. Se neste mesmo arquivo um único bit for alterado o hash gerado será diferente.
##### Biblioteca usada:
- hashlib: implementa uma interface comum para muitos algoritmos de hash seguro como SHA1, SHA256, MD5 etc.

## 03 - Web Scraping :globe_with_meridians:
##### O que é Web Scraping?
É uma ferramenta de coleta de dados web, uma forma de mineração que permite a extração de dados de dites da web convertendo-ps em informação estruturada para posterior análise.
##### Bibliotecas usadas:
- BeautifulSoup: biblioteca de extração de dados de arquivos HTML e XML;
- requests: Permite que você envie solicitações HTTP em Python.

## 04- Web Crawler :globe_with_meridians:
 ##### O que é Web Crawler?
 É uma ferramenta uusada para encontrar, ler e indexar páginas de um site. É como um rodô que captura informações de cada um dos links que encontra, cadastra e compreende o que é mais relevante (palavras-chaves). Muito utilizada em processo de Pentest.
 ##### Bibliotecas usadas:
 - Requests: _já citada anteriormente_
 - BeautifulSoup: _já citada anteriormente_
 - Operator: exporta um conjunto de funções eficientes correspondentes aos operadores intrínsecos do Python;
 - Collections: implementa tipos de dados de contêiner especializados que fornecem alternativas aos contêineres embutidos do Python, dict, list, set e tuple.
 
## 05- Verificador de Telefone :telephone_receiver:
##### Bibliotecas usadas:
 - Phonenumbers: oferece informações básicas de um número de telefone, validação de um número, entre outros.

## 06- Ocultador de arquivos :page_with_curl:
##### Bibliotecas usadas:
 - Ctypes: fornece tipos de dados compatíveis com C e permite funções de chamada em DLLs ou bibliotecas compartilhadas.

## 07- Verificador de IP externo :key: 
##### Bibliotecas usadas:
 - re: Permite operações com expressões regulares;
 - JSON: Fornece operações de codificação e decodificação de JSON;
 - Urllib.requests import urlopen: Funções e classes que ajudam a abrir URLs.

## 08- Ferramenta gráfica para abrir navegador :globe_with_meridians:
##### Bibliotecas usadas:
 - webbrowser: fornece uma interface de alto nível para permitir a exibição de documentos web aos usuários
 - tkinter: fornece interface padrão do Python para o kit de ferramentas gráficas Tk. 

*Fonte: Anotações da aula do [professor Bruno Dias](https://www.linkedin.com/in/brunodecamposdias/).*
