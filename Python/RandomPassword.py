#Gerador de senhas, primeiro pega a quantidade de caracteres da senha, guarde isso, crie uma variavel.
#Essa variavel vai ser a senha, faça com que os caracteres maximos sejam o que for escrito no input.
#E gere caracteres aleatorios, e exiba pro usuario.

import random
import string
quant_max = int(input("Quantidade máxima de caracteres:"))
charac = string.ascii_letters
senha = random.choices(charac, k=quant_max)
print("".join(senha))
