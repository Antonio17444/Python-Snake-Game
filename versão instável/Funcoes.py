import pygame
from random import randint

pygame.init()

def som():
    trilha = pygame.mixer.Sound("music/SnakeTheme.mp3")
    som_morder = pygame.mixer.Sound("music/morder.mp3")
    return trilha, som_morder

def Constates():
    rodando = True
    largura = 640
    altura = 480
    return rodando,largura,altura

def Cores():
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    AZUL = (0, 0, 255)
    VERMELHO = (255, 0, 0)
    VERDE = (0, 255, 0)
    return PRETO,BRANCO,AZUL,VERMELHO,VERDE

def Variaveis(largura,altura):
    velocidade = 30  #para evitar bug das textura uma dentro da outra deixar velocidade = tamanho do bloco
    tamanho_bloco = 30
    x = (largura - tamanho_bloco) // 2
    y = (altura - tamanho_bloco) // 2
    x_controle = 0
    y_controle = 0
    FPS = 15
    x_comida = randint(40,600)
    y_comida = randint(40,440)
    contador_de_pontos = 0
    lista_Corpo = []
    return velocidade,tamanho_bloco,x,y,x_controle,y_controle,FPS,x_comida,y_comida,contador_de_pontos,lista_Corpo

def teclados(x_controle, y_controle, vel,x,y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_controle != vel:
                y_controle = -vel
                x_controle = 0

            elif event.key == pygame.K_DOWN and y_controle != -vel:
                y_controle = vel
                x_controle = 0

            elif event.key == pygame.K_LEFT and x_controle != vel:
                x_controle = -vel
                y_controle = 0

            elif event.key == pygame.K_RIGHT and x_controle != -vel:
                x_controle = vel
                y_controle = 0

    x += x_controle
    y += y_controle

    return x_controle, y_controle,x,y

def colisao(jogador,comida,contador_de_pontos, som_morder):
    if jogador.colliderect(comida):
        som_morder.play()
        x_comida = randint(40, 600)
        y_comida = randint(40, 440)
        contador_de_pontos += 1
    else:
        x_comida = comida.x
        y_comida = comida.y
    return x_comida, y_comida, contador_de_pontos

def texto(fonte,contador_de_pontos,BRANCO,tela):
    mensagem = f'Pontos: {contador_de_pontos}' # mensagem dentro do while para atualizar os pontos
    texto = fonte.render(mensagem,True,(BRANCO)) #formatando texto
    return tela.blit(texto,(0,0))

def Jogador_saiu_tela(rodando,x,y,largura,altura):
    if x <= 0:
        rodando = False
    if x >= largura:
        rodando = False
    if y <= 0:
        rodando = False
    if y >= altura:
        rodando = False
    return rodando

def comida_ir_para_o_corpo(x, y, lista_corpo, tela, VERDE, tamanho_bloco,AZUL,contador_de_pontos):
    lista_corpo.append((x, y))
    for bloco in lista_corpo:
        pygame.draw.rect(tela, VERDE, (*bloco, tamanho_bloco, tamanho_bloco))
    jogador = pygame.draw.rect(tela,AZUL,(x,y,tamanho_bloco,tamanho_bloco))

    if len(lista_corpo) > contador_de_pontos:
        lista_corpo.pop(0)

def colisao_corpo(x, y, lista_corpo):
    corpo_sem_cabeca = lista_corpo[:-1]
    if (x, y) in corpo_sem_cabeca:
        return False
    return True
