from datetime import datetime
from time import sleep
import winsound
import os
import threading


def toque():
    # RÉ MAIOR
    winsound.Beep(145, 200)
    winsound.Beep(222, 300)
    winsound.Beep(369, 200)
    winsound.Beep(296, 300)

    # LÁ MENOR
    winsound.Beep(109, 200)
    winsound.Beep(165, 300)
    winsound.Beep(262, 200)
    winsound.Beep(220, 300)

    # DO MAIOR
    winsound.Beep(130, 200)
    winsound.Beep(165, 300)
    winsound.Beep(262, 200)
    winsound.Beep(196, 300)

    # MI MENOR
    winsound.Beep(82, 200)
    winsound.Beep(165, 300)
    winsound.Beep(246, 200)
    winsound.Beep(196, 300)



def despertador():
    hora = input('Digite a hora para despertar: ')
    minuto = input('Digite o minuto para despertar: ')
    segundo = input('Digite o segundo para despertar: ')

    if len(hora) == 1:
        hora = f'0{hora}'

    despertador = f'{hora}:{minuto}:{segundo}'

    while True:
        agora = datetime.now().strftime('%H:%M:%S')
        print(agora)
        if agora == despertador:
            t = threading.Thread(target=toque)
            t.start()
            
        sleep(1)
        os.system('cls')


if __name__ == '__main__':
    despertador()
