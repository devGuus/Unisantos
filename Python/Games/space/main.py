import pygame
import random
import webbrowser
from pyvidplayer2 import Video

# Inicialização do pygame
pygame.init()

# Configurações da tela
RESOLUCOES = [(800, 600), (1024, 768), (1280, 720)]
resolucao_atual = 0  # Índice da resolução atual
LARGURA, ALTURA = RESOLUCOES[resolucao_atual]
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Tiro")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Fonte personalizada (Press Start 2P)
fonte_jogo = pygame.font.Font("Python/Games/space/Fonts/8-bit Arcade In.ttf", 60)

# Placar
score = 0
life = 5
damage_enemy_small = 1

# Configurações do jogador
player_width = 50
player_height = 50
player_x = LARGURA // 2 - player_width // 2
player_y = ALTURA - player_height - 20
player_vel = 5

# Configuração dos projéteis
balas = []
bala_vel = -7
bala_width = 5
bala_height = 10

# Configuração dos inimigos
inimigos = []
inimigo_vel = 2
inimigo_width = 50
inimigo_height = 50

# Relógio para FPS
clock = pygame.time.Clock()

# Botões do menu
menu_font = pygame.font.Font(None, 50)
menu_opcoes = ["Iniciar Jogo", "Opçoes", "Sair"]
selecionar_opcoes = 0

# Vídeo menu
video_menu = Video('Python/Games/space/movies/video_menu.mp4')

# Carregamento de imagens
try:
    # Background
    bg_image = pygame.image.load('Python/Games/space/imagens/bg_espaço_roxo.png') 
    fundo_menu = pygame.image.load('Python/Games/space/imagens/imagem-fundo2.jpg')
    # Redimensionar imagem player
    nave_player = pygame.image.load('Python/Games/space/imagens/nave.png')
    nave_player = pygame.transform.scale(nave_player, (50, 50)) 
    # Redimensionar imagem inimigo
    nave_enemy = pygame.image.load('Python/Games/space/imagens/enemy_nave.png')
    nave_enemy = pygame.transform.scale(nave_enemy, (inimigo_width, inimigo_height))
    # Icone do GitHub
    github_icone = pygame.image.load('Python/Games/space/imagens/icone_github.png')
    github_icone = pygame.transform.scale(github_icone, (40, 40))
except pygame.error as e:
    print(f"Erro ao carregar imagens: {e}")
    pygame.quit()
    exit()

def draw_menu():
    tela.fill((0, 0, 0))  # Garante que a tela fique preta antes de desenhar o vídeo
    #video_menu.draw(tela, (0, 0))  # Desenha o vídeo cobrindo a tela inteira
    tela.blit(fundo_menu, (0,0))

    for i, option in enumerate(menu_opcoes):
        color = VERDE if i == selecionar_opcoes else BRANCO
        text = fonte_jogo.render(option, True, color)
        text_centralizar = text.get_rect(center=(LARGURA // 2, 250 + i * 60))
        tela.blit(text, text_centralizar)
    # Insere o icone do GitHub no canto da tela
    tela.blit(github_icone, (LARGURA - 50, ALTURA - 50))
    pygame.display.update()

def menu():
    global selecionar_opcoes
    video_menu.restart()  # Reinicia o vídeo no início do menu
    rodando = True
    while rodando:
        draw_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                video_menu.close() # Fechar o video menu
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionar_opcoes = (selecionar_opcoes + 1) % len(menu_opcoes)
                if evento.key == pygame.K_UP:
                    selecionar_opcoes = (selecionar_opcoes - 1) % len(menu_opcoes)
                if evento.key == pygame.K_RETURN:
                    if selecionar_opcoes == 0:
                        return  # Start Game
                    elif selecionar_opcoes == 1:
                        opcoes()
                    elif selecionar_opcoes == 2:
                        pygame.quit()
                        exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if LARGURA - 50 <= x <= LARGURA and ALTURA - 50 <= y <= ALTURA:
                    webbrowser.open("https://github.com/devGuus")
def opcoes():
    global som_ativo, resolucao_atual, LARGURA, ALTURA, tela

    opcoes_lista = ["Som  ON", f"Resolucao  {RESOLUCOES[resolucao_atual][0]}x{RESOLUCOES[resolucao_atual][1]}", "Voltar"]
    selecionar_opcao = 0

    rodando = True
    while rodando:
        tela.fill((0, 0, 0))
        tela.blit(fundo_menu, (0,0))

        for i, opcao in enumerate(opcoes_lista):
            color = VERDE if i == selecionar_opcao else BRANCO
            text = fonte_jogo.render(opcao, True, color)
            text_centralizar = text.get_rect(center=(LARGURA // 2, 250 + i * 60))
            tela.blit(text, text_centralizar)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionar_opcao = (selecionar_opcao + 1) % len(opcoes_lista)
                if evento.key == pygame.K_UP:
                    selecionar_opcao = (selecionar_opcao - 1) % len(opcoes_lista)
                if evento.key == pygame.K_RETURN:
                    if selecionar_opcao == 0:  # Ativar/desativar som
                        som_ativo = not som_ativo
                        if som_ativo:
                            pygame.mixer.music.play(-1)
                            opcoes_lista[0] = "Som: ON"
                        else:
                            pygame.mixer.music.stop()
                            opcoes_lista[0] = "Som: OFF"
                    elif selecionar_opcao == 1:  # Mudar resolução
                        resolucao_atual = (resolucao_atual + 1) % len(RESOLUCOES)
                        LARGURA, ALTURA = RESOLUCOES[resolucao_atual]
                        tela = pygame.display.set_mode((LARGURA, ALTURA))
                        opcoes_lista[1] = f"Resolução: {LARGURA}x{ALTURA}"
                    elif selecionar_opcao == 2:  # Voltar ao menu
                        return
            
menu()

# Restart game
def restart_game():
    global score, life, player_x, balas, inimigos
    score = 0
    life = 5
    player_x = LARGURA // 2 - player_width // 2
    balas.clear()
    inimigos.clear()

# Loop principal
def main():
    global score, player_x, life
    rodando = True
    pausado = False
    while rodando:
        clock.tick(60)  # Limita a 60 FPS
        
        # Eventos (Pause)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = not pausado
                if evento.key == pygame.K_r and life < 1:
                    restart_game()
        
        if pausado:
            newFont = pygame.font.SysFont("comicsansms", 115)
            pause_text = newFont.render(f'Pausado', False, (0, 255, 0))
            centralizar = pause_text.get_rect(center=(LARGURA // 2, ALTURA // 2))
            tela.blit(pause_text, centralizar)
            pygame.display.flip()
            continue
        
        # Controles do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and player_x > 0:
            player_x -= player_vel
        if teclas[pygame.K_RIGHT] and player_x < LARGURA - player_width:
            player_x += player_vel
        if teclas[pygame.K_SPACE]:
            balas.append(pygame.Rect(player_x + player_width // 2 - bala_width // 2, player_y, bala_width, bala_height))
        
        # Movimentação das balas
        for bala in balas[:]:
            bala.y += bala_vel
            if bala.y < 0:
                balas.remove(bala)
        
        # Spawn de inimigos
        if random.randint(1, 60) == 1:
            inimigos.append({"rect": pygame.Rect(random.randint(0, LARGURA - inimigo_width), 0, inimigo_width, inimigo_height), "img": nave_enemy})

        
        # Movimentação dos inimigos e eliminação
        for inimigo in inimigos[:]:
            inimigo["rect"].y += inimigo_vel
            if inimigo["rect"].y > ALTURA:
                inimigos.remove(inimigo)
                life -= damage_enemy_small
                if life < 1:
                    break     
        
        # Colisão entre balas e inimigos
        for bala in balas[:]:
            for inimigo in inimigos[:]:
                if bala.colliderect(inimigo["rect"]):
                    balas.remove(bala)
                    inimigos.remove(inimigo)
                    score += 1
                    break           

        # Desenho na tela
        tela.blit(bg_image, (0, 0))
        tela.blit(nave_player, (player_x, player_y))  # Desenhando a nave no lugar do retângulo azul
        
        for bala in balas:
            pygame.draw.rect(tela, VERMELHO, bala)
        for inimigo in inimigos:
            tela.blit(inimigo["img"], (inimigo["rect"].x, inimigo["rect"].y))

        
        # Desenhando Score
        font = pygame.font.Font(None, 48)
        score_text = font.render(f'Pontos: {score}', True, (0, 255, 0))
        tela.blit(score_text, (10, 10))

        # Vida do Player
        life_text = font.render(f'Vida: {life}', True, (0, 255, 0))
        tela.blit(life_text, (680, 10))

        if life < 1:
            gameover_text = font.render("Game Over", True, (255, 0, 0))
            restart_text = font.render("Pressione R para reiniciar", True, (255, 0, 0))
            centralizar = gameover_text.get_rect(center=(LARGURA // 2, ALTURA // 2 - 30))
            centralizar_restart = restart_text.get_rect(center=(LARGURA // 2, ALTURA // 2 + 20))
            tela.blit(gameover_text, centralizar)
            tela.blit(restart_text, centralizar_restart)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
