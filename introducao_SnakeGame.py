import pygame
import sys 

pygame.init() # iniciando o Pygame - Henrique

# Tamanho da Janela:

largura = 800
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game - Henrique and Fernando")

# Contagem de FPS:
relogio = pygame.time.Clock()

# Loop do Game:

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Inicio da criação do Game:





