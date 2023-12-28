import serial
import time
import PySimpleGUI as sg
import random

lista_de_valores_jogados = []
porta_serial = serial.Serial('COM3', 9600)
lista_do_usuario = []
contador = 1
contador_de_jogadas = 0

def resultado():
    global flag
    print(lista_de_valores_jogados)
    print(lista_do_usuario)
    flag = False

    for i in range(len(lista_do_usuario)):
        if lista_do_usuario[i] == lista_de_valores_jogados[i]:
            flag = True
        else:
            flag = False
    if flag:
        return True
    return False


def iniciando():
    global contador
    global lista_de_valores_jogados     
    global lista_do_usuario

    lista_do_usuario = []
    lista_valores = ['1', '2', '3', '4', '5']
    
    
    while True: 
        print(lista_de_valores_jogados)
        time.sleep(2)
        valor = random.choice(lista_valores)
        lista_de_valores_jogados.append(valor)
        print(lista_de_valores_jogados)

        for v in lista_de_valores_jogados:
            porta_serial.write(v.encode())
            time.sleep(1)
            porta_serial.write('d'.encode())
            time.sleep(1)
        # for i in range(contador):
        #     valor = random.choice(lista_valores)
        #     porta_serial.write(valor.encode())
        #     print(valor)
        #     lista_de_valores_jogados.append(valor)
        #     time.sleep(1)
        #     porta_serial.write('d'.encode())
        #     time.sleep(1)
        contador += 1
        break

def tela_inicial():
    global contador
    global lista_de_valores_jogados
    global lista_do_usuario
    global contador_de_jogadas
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
            [sg.Text("Joga da memoria", font=('Arial 16'))],
            [sg.Text(f"Placar: {contador}", font=('Arial 12'))],
            [sg.Button('LED 1', size=(7,3), key='1'), sg.Button('LED 2', size=(7,3), key='2'), sg.Button('LED 3', size=(7,3), key='3')],
            [sg.Button('LED 4', size=(7,3), key='4'), sg.Button('LED 5', size=(7,3), key='5')],
            [sg.Button('Começar', size=(7,1), key='comecar')]
        ]

    janela = sg.Window('Produtos', layout, element_justification='c')

    ledUm = 0
    ledDois = 0
    ledTres = 0
    ledQuatro = 0
    ledCinco = 0

    def ligar_led(led):
        time.sleep(1)
        comando = str(led)
        porta_serial.write(comando.encode())
        time.sleep(1)
        porta_serial.write('d'.encode())

    # def desligar_led(led):
    #     comando = str(led)
    #     porta_serial.write(comando.encode())
    #     time.sleep(0.1)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED: 
            break

        elif eventos == 'comecar':
            contador = 1
            contador_de_jogadas = 0
            lista_de_valores_jogados = []
            lista_do_usuario = []
            iniciando()
        elif eventos == '1':
            ligar_led(eventos)
            lista_do_usuario.append(eventos)
            if resultado():
                print('Acertou')
                iniciando()
            else:
                print('errou')
        
        elif eventos == '2':
            ligar_led(eventos)
            lista_do_usuario.append(eventos)
            if resultado():
                print('Acertou')
                iniciando()
            else:
                print('errou')
        

        elif eventos == '3':
            ligar_led(eventos)
            lista_do_usuario.append(eventos)
            if resultado():
                print('Acertou')
                iniciando()
            else:
                print('errou')
        
            
        elif eventos == '4':
            ligar_led(eventos)
            lista_do_usuario.append(eventos)
            if resultado():
                print('Acertou')
                iniciando()
            else:
                print('errou')
        
        
        elif eventos == '5':
            ligar_led(eventos)
            lista_do_usuario.append(eventos)
            if resultado():
                print('Acertou')
                iniciando() 
            else:
                print('errou')
        
tela_inicial()