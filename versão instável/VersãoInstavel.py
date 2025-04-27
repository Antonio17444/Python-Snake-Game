import pygame
import Funcoes

rodando, largura, altura = Funcoes.Constates() # Constantes

PRETO,BRANCO,AZUL,VERMELHO,VERDE = Funcoes.Cores() # Cores

Vel,tamanho_bloco,x,y,x_controle,y_controle,FPS,x_comida,y_comida,contador_de_pontos,lista_corpo = Funcoes.Variaveis(largura,altura) # Outras Variaveis

pygame.init()

# Sons do Game

trilha, som_morder, som_death = Funcoes.som()

trilha.play(-1)

# TELA/JANELA

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake Game")
fonte = pygame.font.SysFont('Arial',40,False,True)

# TELA/JANELA

clock = pygame.time.Clock()  # Cria o relógio

while rodando:

    clock.tick(FPS)
    tela.fill(PRETO)
    
    Funcoes.texto(fonte,contador_de_pontos,BRANCO,tela)

    # Teclado
    teclado = Funcoes.teclados(x_controle, y_controle,Vel,x,y)
    if teclado is None:
        rodando = False
    else:
        x_controle, y_controle,x,y = teclado
    # Teclado

    # DESENHO DO JOGADOR E DA COMIDA
    jogador = pygame.draw.rect(tela,AZUL,(x,y,tamanho_bloco,tamanho_bloco))
    comida = pygame.draw.rect(tela,BRANCO,(x_comida,y_comida,tamanho_bloco,tamanho_bloco))
    # DESENHO DO JOGADOR E DA COMIDA

    x_comida,y_comida,contador_de_pontos = Funcoes.colisao(jogador,comida,contador_de_pontos, som_morder)
    
    rodando = Funcoes.colisao_corpo(x, y, lista_corpo, som_death)
    rodando = Funcoes.Jogador_saiu_tela(rodando,x,y,largura,altura, som_death)

    Funcoes.comida_ir_para_o_corpo(x, y, lista_corpo, tela, VERDE, tamanho_bloco,AZUL,contador_de_pontos)
    
    pygame.display.update()
pygame.quit()
