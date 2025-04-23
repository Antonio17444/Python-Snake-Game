import pygame
import Funcoes

rodando, largura, altura = Funcoes.Constates() # Constantes

PRETO,BRANCO,AZUL,VERMELHO,VERDE = Funcoes.Cores() # Cores

Vel,tamanho_bloco,x,y,x_controle,y_controle,FPS = Funcoes.Variaveis(largura,altura) # Outras Variaveis

pygame.init()

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Da Cobrinha")

clock = pygame.time.Clock()  # Cria o relógio

while rodando:
    clock.tick(FPS)
    tela.fill(PRETO)
    
    # Teclado
    teclado = Funcoes.teclados(x_controle, y_controle,Vel,x,y)
    if teclado is None:
        rodando = False
    else:
        x_controle, y_controle,x,y = teclado
    # Teclado

    jogador = pygame.draw.rect(tela,VERMELHO,(x,y,tamanho_bloco,tamanho_bloco))

    pygame.display.update()
pygame.quit()