import pygame
from time import sleep
print('''Escolha seu estilo musical.
[1] - Black
[2] - Gospel
[3] - Rap
[4] - Eletrônica''')
opção = int(input('Digite a opção desejada: '))
if opção == 1:
    pygame.init()
    pygame.mixer.music.load('Get Your Shine On.mp3')
    pygame.mixer.music.play()
    #pygame.event.wait()
    sleep(90)
elif opção == 2:
    pygame.init()
    pygame.mixer.music.load('Já Posso Suportar.mp3')
    pygame.mixer.music.play()
    #pygame.event.wait()
    sleep(90)
elif opção == 3:
    pygame.init()
    pygame.mixer.music.load('Antes Do Meu Fim.mp3')
    pygame.mixer.music.play()
    #pygame.event.wait()
    sleep(90)
elif opção == 4:
    pygame.init()
    pygame.mixer.music.load('Sebastian Ingrosso.mp3')
    pygame.mixer.music.play()
    #pygame.event.wait()
    sleep(90)
else:
    print('Opção invalida')


