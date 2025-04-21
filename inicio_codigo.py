import pygame
from random import randint

# Constantes

largura = 640
altura = 480

vel = 7

# Flag para definir se o jogo continua rodando

rodando = True

# Variáveis

x = largura/2 # variavel que controla o movimento no eixo x (retangulo azul)
y = altura/2 # variavel que controla o movimento no eixo y (retangulo azul)

x_ponto = randint(40,600)
y_ponto = randint(40,440)

lista_tudo = []

x_controle = vel
y_controle = 0

# Inicializando modulos do pygame

pygame.init()
pygame.mixer.init() # Iniciando modulo de musica
pygame.mixer.music.load("SnakeGameTheme/trilha.ogg") # Add o mp3 da musica tema
pygame.mixer.music.play(-1) # loop (-1) roda ate o jogo fechar

# Texturas 

cabeca_img = pygame.image.load("Texture/cabeca_snake.png")
cabeca_img = pygame.transform.scale(cabeca_img, (40, 40))

# Criando tela

tela = pygame.display.set_mode((largura, altura))  

# fps

relogio = pygame.time.Clock()

# Definidos elementos do texto

contador_de_pontos = 0
fonte = pygame.font.SysFont('Arial',40,False,True)

# função que faz os pontos irem para o corpo do jogador

def movecorpo(lista_tudo):
    
    for i in range (len(lista_tudo)-1,-1,-1):
        #pygame.draw.rect(tela, (0, 0, 255), (lista_tudo[i][0], lista_tudo[i][1], 40, 40))  # Desenha o retângulo azul atraz do jogador
        tela.blit(cabeca_img, (lista_tudo[i][0], lista_tudo[i][1])) #esta dando erro na cabeça do boneco

# Loop onde o jogo deve rodar

while rodando:

    mensagem = f'Pontos: {contador_de_pontos}' # mensagem dentro do while para atualizar os pontos
    texto = fonte.render(mensagem,True,(255,255,255)) #formatando texto
    
    relogio.tick(60) # fps

    tela.fill((0, 0, 0))  # Limpa a tela com cor preta
    
    for event in pygame.event.get():  # Detecta eventos
        if event.type == pygame.QUIT:
            rodando = False
        
        # ver quais teclas sao presionadas
        
        teclas = pygame.key.get_pressed() 

        if teclas[pygame.K_UP]:
            if y_controle == vel:
                pass
            else:
                y_controle = -vel
                x_controle = 0

        if teclas[pygame.K_DOWN]:
            if y_controle == -vel:
                pass
            else:
                y_controle = +vel
                x_controle = 0

        if teclas[pygame.K_LEFT]:
            if x_controle == vel:
                pass
            else:
                x_controle = -vel
                y_controle = 0

        if teclas[pygame.K_RIGHT]:
            if x_controle == -vel:
                pass
            else:    
                x_controle = vel
                y_controle = 0


    # Verifica se o jogador saiu da tela(se sim entao o progama fecha)

    if y >= altura:
        rodando = False
    if x >= largura:
        rodando = False
    if y <= 0:
        rodando = False
    if x <= 0:
        rodando = False

    # usando para o jogador nao se mover nas diagonais

    x += x_controle
    y += y_controle

    jogador = tela.blit(cabeca_img, (x, y))

    ponto = pygame.draw.rect(tela, (255, 255, 255), (x_ponto, y_ponto, 40, 40))  # Desenha os pontos

    # Ver se o jogador colidiu com o ponto se sim entao adiciona 1 ao contador e mudar o ponto para um lugar randomico

    if jogador.colliderect(ponto):
        x_ponto = randint(40,600)
        y_ponto = randint(40,440)
        contador_de_pontos += 1

    tela.blit(texto,(0,0)) #imprimindo na tela a mensagem


    # selecionando o x e y que o jogador passou
 
    lista_cabeca = []
    lista_cabeca.append(x)
    lista_cabeca.append(y)

    # salvando cada posição passada

    lista_tudo.append(lista_cabeca)

    # delimitando o tamanho da cobra

    if len(lista_tudo) > contador_de_pontos+1:
        lista_tudo.pop(0)

    # chamando a funcao

    movecorpo(lista_tudo)
    
    pygame.display.update()  # Atualiza a tela

pygame.mixer.music.stop()
pygame.quit()
