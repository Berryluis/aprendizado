#Gerador de senhas, primeiro pega a quantidade de caracteres da senha, guarde isso, crie uma variavel.
#Essa variavel vai ser a senha, faça com que os caracteres maximos sejam o que for escrito no input.
#E gere caracteres aleatorios, e exiba pro usuario.
import PySimpleGUI as sg
import random
import string
from subprocess import check_call

sg.theme('reddit')

quant_max = 0

layout = [
    [sg.Text('Length:'), sg.Input(key='length')],
    [sg.Text('Numbers:'), sg.Checkbox('', key='checkbox')],
    [sg.Button('Generate Password')],
    [sg.Text('Result: ', key='resultado'), sg.Button('Copy')]
]

janela = sg.Window('Random Password Generator', layout=layout)
seq = string.ascii_letters

def copy2paste(t):
    cmd='echo '+t.strip()+'|clip'
    return check_call(cmd, shell=True)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Generate Password':
        print('Apertou!')

        if valores['checkbox']:
            seq = seq + f'{string.digits}'


        try:
            if int(valores['length']) > 0:
                q = valores['length']
                print(q)
                senha = random.choices(seq, k=int(q))
                result = ''.join(senha)
                print(result)
                janela.Element('resultado').update(f'Result: {result}')

                
        except Exception:
            print('Erro!')
            print(Exception)
            continue

    if eventos == 'Copy':
        copy2paste(result)
        

                          


        

    
            
        

