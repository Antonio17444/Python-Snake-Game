import pygame
pygame.init()

def movecorpo(lista_tudo,tela,cabeca_atual):
    for i in range (len(lista_tudo)-1,-1,-1):
        tela.blit(cabeca_atual, (lista_tudo[i][0], lista_tudo[i][1])) 

def teclados(x_controle, y_controle, vel, cabeca_atual, cabeca_cima, cabeca_baixo, cabeca_esquerda, cabeca_direita,x,y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None  # Sinal para sair do jogo

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_controle != vel:
                y_controle = -vel
                x_controle = 0
                cabeca_atual = cabeca_cima

            elif event.key == pygame.K_DOWN and y_controle != -vel:
                y_controle = vel
                x_controle = 0
                cabeca_atual = cabeca_baixo

            elif event.key == pygame.K_LEFT and x_controle != vel:
                x_controle = -vel
                y_controle = 0
                cabeca_atual = cabeca_esquerda

            elif event.key == pygame.K_RIGHT and x_controle != -vel:
                x_controle = vel
                y_controle = 0
                cabeca_atual = cabeca_direita
    x += x_controle
    y += y_controle

    return x_controle, y_controle, cabeca_atual,x,y

def veriificar_se_jogador_saiu_da_tela(x,y,altura,largura):
    if y >= altura:
        return False
    if x >= largura:
        return False
    if y <= 0:
        return False
    if x <= 0:
        return False
    return True
        
