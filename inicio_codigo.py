import pygame
import sys

# Definindo as cores.
BRANCO = (255,255,255)
PRETO = (0, 0, 0) #Tabuleiro
VERMELHO = (255, 0, 0) #Pontos 
AZUL = (0, 0, 255) # Cobra

#Outras constates

Vel = 5 # velocidade da personagem (cobra) pixel/seg
TAMANHOBLOCO = 20 #Tamanho do lado do bloco em pixels

#função mover jogador

def mover(jogador,tecla,dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if tecla['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if tecla['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    if tecla['cima'] and jogador['objRect'].top > borda_superior:
        jogador['objRect'].y -= jogador['vel']
    if tecla['baixo'] and jogador['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']
                                        
#função mover bloco

def moverBloco(bloco):
    bloco['objRect'].y += bloco['vel']
                             
# iniciando o Pygame - Henrique                                    

pygame.init() 

# Tamanho da Janela:

largura = 800
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game - Henrique and Fernando")

# Informações básicas: 
relogio = pygame.time.Clock() # FPS
rodando = True # Determina o fechamendo do programa True/False

#Criado jogador

jogador = {'objRect': pygame.Rect(300, 100, 50, 50), 'cor': AZUL, 'vel': Vel}

# definindo o dicionario que guardará as direcoes pressionadas

tecla = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}

#outras variaveis

blocos = []

# Loop do Game:

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            rodando = False

        # quando uma tecla é pressionada
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            deve_continuar = False
        if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
            tecla['esquerda'] = True
        if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
            tecla['direita'] = True
        if evento.key == pygame.K_UP or evento.key == pygame.K_w:
            tecla['cima'] = True
        if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
            tecla['baixo'] = True

    # quando uma tecla é solta
    if evento.type == pygame.KEYUP:
        if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
            tecla['esquerda'] = False
        if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
            tecla['direita'] = False
        if evento.key == pygame.K_UP or evento.key == pygame.K_w:
            tecla['cima'] = False
        if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
            tecla['baixo'] = False

    # quando um botão do mouse é pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            blocos.append({'objRect': pygame.Rect(evento.pos[0], evento.pos[1], TAMANHOBLOCO, TAMANHOBLOCO), 'cor': BRANCO, 'vel': 1})

    # Inicio da criação do Game:
    tela.fill(PRETO)

    # movendo o jogador

    mover(jogador, tecla, (largura, altura))

    # desenhando jogador

    pygame.draw.rect(tela, jogador['cor'], jogador['objRect'])
                                                     
    for bloco in blocos[:]:
        bateu = jogador['objRect'].colliderect(bloco['objRect'])
        if bateu or bloco['objRect'].y > altura:
            blocos.remove(bloco)

    pygame.display.flip()
    relogio.tick(60)  # Trás a variavel "relogio", para limitar o FPS em 60 - Henrique

pygame.quit()



