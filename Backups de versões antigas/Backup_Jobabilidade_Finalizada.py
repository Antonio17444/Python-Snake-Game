import pygame
import Funcoes_jogabilidade

rodando, largura, altura = Funcoes_jogabilidade.Constates() # Constantes

PRETO,BRANCO,AZUL,VERMELHO,VERDE = Funcoes_jogabilidade.Cores() # Cores

Vel,tamanho_bloco,x,y,x_controle,y_controle,FPS,x_comida,y_comida,contador_de_pontos,lista_corpo = Funcoes_jogabilidade.Variaveis(largura,altura) # Outras Variaveis

pygame.init()

# TELA/JANELA
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Da Cobrinha")
fonte = pygame.font.SysFont('Arial',40,False,True)
# TELA/JANELA

clock = pygame.time.Clock()  # Cria o relógio

while rodando:

    clock.tick(FPS)
    tela.fill(PRETO)
    
    Funcoes_jogabilidade.texto(fonte,contador_de_pontos,BRANCO,tela)

    # Teclado
    teclado = Funcoes_jogabilidade.teclados(x_controle, y_controle,Vel,x,y)
    if teclado is None:
        rodando = False
    else:
        x_controle, y_controle,x,y = teclado
    # Teclado

    # DESENHO DO JOGADOR E DA COMIDA
    jogador = pygame.draw.rect(tela,AZUL,(x,y,tamanho_bloco,tamanho_bloco))
    comida = pygame.draw.rect(tela,BRANCO,(x_comida,y_comida,tamanho_bloco,tamanho_bloco))
    # DESENHO DO JOGADOR E DA COMIDA

    x_comida,y_comida,contador_de_pontos = Funcoes_jogabilidade.colisao(jogador,comida,contador_de_pontos)
    
    rodando = Funcoes_jogabilidade.colisao_corpo(x, y, lista_corpo)
    rodando = Funcoes_jogabilidade.Jogador_saiu_tela(rodando,x,y,largura,altura)

    Funcoes_jogabilidade.comida_ir_para_o_corpo(x, y, lista_corpo, tela, VERDE, tamanho_bloco,AZUL,contador_de_pontos)
    
    pygame.display.update()
pygame.quit()