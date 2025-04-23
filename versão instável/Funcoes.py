import pygame
pygame.init()

def Constates():
    rodando = True
    largura = 640
    altura = 480
    return rodando,largura,altura

def Cores():
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    AZUL = (0, 0, 255)
    VERMELHO = (255, 0, 0)
    VERDE = (0, 255, 0)
    return PRETO,BRANCO,AZUL,VERMELHO,VERDE

def Variaveis(largura,altura):
    velocidade = 10
    tamanho_bloco = 30
    x = (largura - tamanho_bloco) // 2
    y = (altura - tamanho_bloco) // 2
    x_controle = 0
    y_controle = 0
    FPS = 60
    return velocidade,tamanho_bloco,x,y,x_controle,y_controle,FPS

def teclados(x_controle, y_controle, vel,x,y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_controle != vel:
                y_controle = -vel
                x_controle = 0

            elif event.key == pygame.K_DOWN and y_controle != -vel:
                y_controle = vel
                x_controle = 0

            elif event.key == pygame.K_LEFT and x_controle != vel:
                x_controle = -vel
                y_controle = 0

            elif event.key == pygame.K_RIGHT and x_controle != -vel:
                x_controle = vel
                y_controle = 0

    x += x_controle
    y += y_controle

    return x_controle, y_controle,x,y
