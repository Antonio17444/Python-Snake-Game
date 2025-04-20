import pygame
import sys 

pygame.init() # iniciando o Pygame - Henrique

# Tamanho da Janela:

largura = 800
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game - Henrique and Fernando")

# Informações básicas: 
relogio = pygame.time.Clock() # FPS
rodando = True # Determina o fechamendo do programa True/False
branco = (255, 255, 255)

# Loop do Game:

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            rodando = False

    # Inicio da criação do Game:
    tela.fill(branco)


    # VAMOS COLOCAR O CÓDIGO DO GAME ESSE INTERVALO ENTRE O fill/flip - Henrique


    pygame.display.flip()
    relogio.tick(60)  # Trás a variavel "relogio", para limitar o FPS em 60 - Henrique

pygame.quit()



