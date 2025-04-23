import pygame
import Funcoes

rodando, largura, altura = Funcoes.Constates() # Constantes

PRETO,BRANCO,AZUL,VERMELHO,VERDE = Funcoes.Cores() # Cores

Vel,x,y = Funcoes.Variaveis() # Outras Variaveis

pygame.init()

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Da Cobrinha")

while rodando:
    tela.fill(PRETO)


    jogador = pygame.draw.rect(tela,VERMELHO,(x,y,30,30))

    pygame.display.update()
pygame.quit()