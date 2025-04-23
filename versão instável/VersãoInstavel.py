import pygame
import Funcoes

rodando, largura, altura = Funcoes.Constates() # Constantes

PRETO,BRANCO,AZUL,VERMELHO,VERDE = Funcoes.Cores() # Cores

Vel,tamanho_bloco,x,y,x_controle,y_controle,FPS,x_comida,y_comida = Funcoes.Variaveis(largura,altura) # Outras Variaveis

pygame.init()

# TELA/JANELA
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Da Cobrinha")
# TELA/JANELA

# TEXTO
contador_de_pontos = 0
fonte = pygame.font.SysFont('Arial',40,False,True)

# TEXTO

clock = pygame.time.Clock()  # Cria o relógio

while rodando:
    
    clock.tick(FPS)
    tela.fill(PRETO)
    
    # TEXTO
    mensagem = f'Pontos: {contador_de_pontos}' # mensagem dentro do while para atualizar os pontos
    texto = fonte.render(mensagem,True,(255,255,255)) #formatando texto
    tela.blit(texto,(0,0))
    # TEXTO

    # Teclado
    teclado = Funcoes.teclados(x_controle, y_controle,Vel,x,y)
    if teclado is None:
        rodando = False
    else:
        x_controle, y_controle,x,y = teclado
    # Teclado

    jogador = pygame.draw.rect(tela,VERDE,(x,y,tamanho_bloco,tamanho_bloco))
    comida = pygame.draw.rect(tela,BRANCO,(x_comida,y_comida,tamanho_bloco,tamanho_bloco))

    # Colisao
    x_comida,y_comida,contador_de_pontos = Funcoes.colisao(jogador,comida,contador_de_pontos)
    # Colisao

    pygame.display.update()
pygame.quit()