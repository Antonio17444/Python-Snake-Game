import pygame
from random import randint

# Constantes

largura = 640
altura = 480

vel = 10

# Flag para definir se o jogo continua rodando

rodando = True

# Variáveis

x = largura/2 # variavel que controla o movimento no eixo x (retangulo azul)
y = altura/2 # variavel que controla o movimento no eixo y (retangulo azul)

x_ponto = randint(40,600)
y_ponto = randint(40,440)



# Inicializando modulos do pygame

pygame.init()
pygame.mixer.init() # Iniciando modulo de musica
pygame.mixer.music.load("SnakeGameTheme/trilha.ogg") # Add o mp3 da musica tema
pygame.mixer.music.play(-1) # loop (-1) roda ate o jogo fechar
som_colisao = pygame.mixer.Sound("SnakeGameTheme/coleta.ogg")
som_colisao.set_volume(0.5)

# Texturas 

cabeca_cima = pygame.image.load("Texture/cabeca_cima.png")
cabeca_baixo = pygame.image.load("Texture/cabeca_baixo.png")
cabeca_esquerda = pygame.image.load("Texture/cabeca_esquerda.png")
cabeca_direita = pygame.image.load("Texture/cabeca_direita.png")

# ajustanto tamanho das texturas

cabeca_cima = pygame.transform.scale(cabeca_cima, (40, 40))
cabeca_baixo = pygame.transform.scale(cabeca_baixo, (40, 40))
cabeca_esquerda = pygame.transform.scale(cabeca_esquerda, (40, 40))
cabeca_direita = pygame.transform.scale(cabeca_direita, (40, 40))

cabeca_atual = cabeca_cima

# Criando tela

tela = pygame.display.set_mode((largura, altura))  

# fps

relogio = pygame.time.Clock()

# Definidos elementos do texto

contador_de_pontos = 0
fonte = pygame.font.SysFont('Arial',40,False,True)

# Loop onde o jogo deve rodar

while rodando:

    mensagem = f'Pontos: {contador_de_pontos}' # mensagem dentro do while para atualizar os pontos
    texto = fonte.render(mensagem,True,(255,255,255)) #formatando texto
    


    relogio.tick(60) # fps

    tela.fill((0, 0, 0))  # Limpa a tela com cor preta
    
    for event in pygame.event.get():  # Detecta eventos
        if event.type == pygame.QUIT:
            rodando = False

    # Verifica se o jogador saiu da tela(se sim entao o progama fecha)

    if y >= altura:
        rodando = False
    if x >= largura:
        rodando = False
    if y <= 0:
        rodando = False
    if x <= 0:
        rodando = False

    # ver quais teclas sao presionadas

    teclas = pygame.key.get_pressed() 

    if teclas[pygame.K_UP]:
        y -= vel
        cabeca_atual = cabeca_cima

    if teclas[pygame.K_DOWN]:
        y += vel
        cabeca_atual = cabeca_baixo

    if teclas[pygame.K_LEFT]:
        x -= vel
        cabeca_atual = cabeca_esquerda

    if teclas[pygame.K_RIGHT]:
        x += vel
        cabeca_atual = cabeca_direita

    jogador = tela.blit(cabeca_atual, (x, y))

    ponto = pygame.draw.rect(tela, (255, 255, 255), (x_ponto, y_ponto, 40, 40))  # Desenha os pontos

    # Ver se o jogador colidiu com o ponto se sim entao adiciona 1 ao contador e mudar o ponto para um lugar randomico

    if jogador.colliderect(ponto):
        som_colisao.play()
        x_ponto = randint(40,600)
        y_ponto = randint(40,440)
        contador_de_pontos += 1

    tela.blit(texto,(0,0)) #imprimindo na tela a mensagem

    pygame.display.update()  # Atualiza a tela

pygame.mixer.music.stop()
pygame.quit()
