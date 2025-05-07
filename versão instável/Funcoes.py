import pygame
from random import randint

pygame.init()

def som():
    trilha = pygame.mixer.Sound("music/SnakeTheme.mp3")
    som_morder = pygame.mixer.Sound("music/morder.mp3")
    som_death = pygame.mixer.Sound("music/Death.mp3")
    som_death.set_volume(0.5)
    trilha.set_volume(0.2)
    som_morder.set_volume(0.5)
    return trilha, som_morder, som_death

# Texturas 

def textura():

    textura_ponto = pygame.image.load("textura/maça.png").convert_alpha()
    cabeca_cima = pygame.image.load("textura/cabeca_cima.png").convert_alpha()
    cabeca_baixo = pygame.image.load("textura/cabeca_baixo.png").convert_alpha()
    cabeca_direita = pygame.image.load("textura/cabeca_direita.png").convert_alpha()
    cabeca_esquerda = pygame.image.load("textura/cabeca_esquerda.png").convert_alpha()
    corpo = pygame.image.load("textura/corpo.png").convert_alpha()

    textura_ponto = pygame.transform.scale(textura_ponto, (40, 40))
    cabeca_cima = pygame.transform.scale(cabeca_cima, (40, 40))
    cabeca_baixo = pygame.transform.scale(cabeca_baixo, (40, 40))
    cabeca_direita = pygame.transform.scale(cabeca_direita, (40, 40))
    cabeca_esquerda = pygame.transform.scale(cabeca_esquerda, (40, 40))
    corpo = pygame.transform.scale(corpo, (40, 40))

    return corpo, cabeca_baixo, cabeca_cima, cabeca_direita, cabeca_esquerda, textura_ponto

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

def teclados(x_controle, y_controle, vel,x,y, direcao, cabeca_baixo, cabeca_cima, cabeca_esquerda, cabeca_direita):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_controle != vel:
                y_controle = -vel
                x_controle = 0
                direcao = cabeca_cima

            elif event.key == pygame.K_DOWN and y_controle != -vel:
                y_controle = vel
                x_controle = 0
                direcao = cabeca_baixo


            elif event.key == pygame.K_LEFT and x_controle != vel:
                x_controle = -vel
                y_controle = 0
                direcao = cabeca_esquerda

            elif event.key == pygame.K_RIGHT and x_controle != -vel:
                x_controle = vel
                y_controle = 0
                direcao = cabeca_direita

    x += x_controle
    y += y_controle

    return x_controle, y_controle,x,y, direcao

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

def Jogador_saiu_tela(x, y, tamanho_bloco, largura, altura, som_death, trilha):
    if x < 0 or x + tamanho_bloco > largura or y < 0 or y + tamanho_bloco > altura:
        som_death.play()
        trilha.stop()
        rodando = False
    else:
        rodando = True
    return rodando

def comida_ir_para_o_corpo(x, y, lista_corpo, tela, corpo, direcao, contador_de_pontos):
    lista_corpo.append((x, y))
    for bloco in lista_corpo:
        tela.blit(corpo, bloco)
    jogador = tela.blit(direcao, (x,y))

    if len(lista_corpo) > contador_de_pontos:
        lista_corpo.pop(0)

def colisao_corpo(x, y, lista_corpo, som_death, trilha):
    corpo_sem_cabeca = lista_corpo[:-1]
    if (x, y) in corpo_sem_cabeca:
        som_death.play()
        trilha.stop()
        return False
    return True

def jogo():

    rodando, largura, altura = Constates() # Constantes

    PRETO,BRANCO,AZUL,VERMELHO,VERDE = Cores() # Cores

    corpo, cabeca_baixo, cabeca_cima, cabeca_direita, cabeca_esquerda, textura_ponto = textura()  # Texturas

    Vel,tamanho_bloco,x,y,x_controle,y_controle,FPS,x_comida,y_comida,contador_de_pontos,lista_corpo = Variaveis(largura,altura) # Outras Variaveis

    # Sons do Game

    trilha, som_morder, som_death = som()

    trilha.play(-1)

    # TELA/JANELA

    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption("Snake Game")
    fonte = pygame.font.SysFont('Arial',40,False,True)

    # TELA/JANELA

    clock = pygame.time.Clock()  # Cria o relógio
    direcao = cabeca_cima

    while rodando:

        clock.tick(FPS)
        tela.fill(PRETO)
        
        texto(fonte,contador_de_pontos,BRANCO,tela)

        # Teclado
        teclado = teclados(x_controle, y_controle,Vel,x,y,direcao,cabeca_cima, cabeca_baixo, cabeca_direita, cabeca_esquerda)
        if teclado is None:
            rodando = False
        else:
            x_controle, y_controle,x,y, direcao = teclado

        
        # Teclado

        jogador = tela.blit(direcao, (x, y))

        comida = comida = tela.blit(textura_ponto, (x_comida, y_comida))
        # DESENHO DO JOGADOR E DA COMIDA

        x_comida,y_comida,contador_de_pontos = colisao(jogador,comida,contador_de_pontos, som_morder)
        
        rodando = colisao_corpo(x, y, lista_corpo, som_death, trilha)
        rodando = Jogador_saiu_tela(x, y, tamanho_bloco, largura, altura, som_death, trilha)

        comida_ir_para_o_corpo(x, y, lista_corpo, tela, corpo, direcao, contador_de_pontos)
        
        pygame.display.update()
    pygame.quit()
    menu()

def creditos():
    rodando, largura, altura = Constates()  # Constantes
    PRETO, BRANCO, AZUL, VERMELHO, VERDE = Cores()  # Cores

    # TELA/JANELA
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Snake Game")

    # Texto
    fonte = pygame.font.SysFont('Arial', 40, False, True)
    fonte1 = pygame.font.SysFont('Arial', 80, False, True)
    texto0 = fonte1.render("CRÉDITOS", True, VERMELHO)
    texto1 = fonte.render("Antonio Henrique Vigo Leite", True, VERDE)
    texto2 = fonte.render("Fernando Pereira Dos Santos", True, VERDE)

    # Retângulos dos textos com centralização
    rect0 = texto0.get_rect(center=(largura // 2, altura // 2 - 180))
    rect1 = texto1.get_rect(center=(largura // 2, altura // 2 - 60))
    rect2 = texto2.get_rect(center=(largura // 2, altura // 2))

    while rodando:
        tela.fill(PRETO)

        # Desenhar os textos
        tela.blit(texto0, rect0)
        tela.blit(texto1, rect1)
        tela.blit(texto2, rect2)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        pygame.display.update()

    pygame.quit()
    menu()
    
def menu():
    rodando, largura, altura = Constates()  # Constantes
    PRETO, BRANCO, AZUL, VERMELHO, VERDE = Cores()  # Cores

    pygame.init()

    # TELA/JANELA
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Snake Game")

    # Texto
    fonte = pygame.font.SysFont('Arial', 40, False, True)
    fonte1 = pygame.font.SysFont('Arial', 80, False, True)
    texto0 = fonte1.render("Snake Game", True, VERMELHO)
    texto1 = fonte.render("PLAY", True, VERDE)
    texto2 = fonte.render("CRÉDITOS", True, VERDE)
    texto3 = fonte.render("SAIR", True, VERDE)

    # Retângulos dos textos com centralização
    rect0 = texto0.get_rect(center=(largura // 2, altura // 2 - 180))
    rect1 = texto1.get_rect(center=(largura // 2, altura // 2 - 60))
    rect2 = texto2.get_rect(center=(largura // 2, altura // 2))
    rect3 = texto3.get_rect(center=(largura // 2, altura // 2 + 60))

    while rodando:
        tela.fill(PRETO)

        # Desenhar os blocos com mesmo tamanho do texto
        bloco_play = pygame.draw.rect(tela, BRANCO, rect1.inflate(5, 5), border_radius=8)
        bloco_creditos = pygame.draw.rect(tela, BRANCO, rect2.inflate(5, 5), border_radius=8)
        bloco_sair = pygame.draw.rect(tela, BRANCO, rect3.inflate(5, 5), border_radius=8)

        # Desenhar os textos
        tela.blit(texto0, rect0)
        tela.blit(texto1, rect1)
        tela.blit(texto2, rect2)
        tela.blit(texto3, rect3)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    pos_mouse = pygame.mouse.get_pos()
                    if bloco_play.collidepoint(pos_mouse):
                        jogo()

                    elif bloco_creditos.collidepoint(pos_mouse):
                        creditos()

                    elif bloco_sair.collidepoint(pos_mouse):
                        rodando = False
        pygame.display.update()

    pygame.quit()
