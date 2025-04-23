import pygame
import Funções.Funcoes

rodando, largura, altura = Funções.Funcoes.Constates() # Constantes

pygame.init()

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Da Cobrinha")

while rodando:
    tela.fill(cor)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False




    pygame.display.update()
pygame.quit()