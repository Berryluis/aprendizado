import random # importa modulo random
import requests #importa modulo requests

ideias = requests.get('https://random-word-api.herokuapp.com/all').json() #da um requests na url e transforma o resultado em uma lista e guarda na variavel ideias.
resultado = (random.choices(ideias, k=random.randint(2,12))) #escolhe um numero de até 12 palavras na lista ideias.
resultado = list(dict.fromkeys(resultado)) #retira as palavras duplicadas da lista transformando em chaves
resultado = " ".join(resultado) #transforma a lista em uma unica string separando por espaços.
print(resultado) #mostra o resultado na tela

