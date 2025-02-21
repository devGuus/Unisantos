import pygame
import random

# Inicialização do pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Tiro")
#bg_image = pygame.image.load('C:\Users\gumar\OneDrive\Documentos\GitHub\Unisantos\Python\Games\space\imagens\imagem-fundo.jpg')
# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

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
#nave_player = pygame.image.load('Python\Games\space\imagens\nave.png')

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
    global score
    global player_x
    global life
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
            newFont = pygame.font.SysFont("comicsansms",115)
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
            inimigos.append(pygame.Rect(random.randint(0, LARGURA - inimigo_width), 0, inimigo_width, inimigo_height))
        
        # Movimentação dos inimigos e eliminação
        global damage_enemy_small
        for inimigo in inimigos[:]:
            inimigo.y += inimigo_vel
            if inimigo.y > ALTURA:
                inimigos.remove(inimigo)
                life -= damage_enemy_small
                if life < 1:
                    break     
        
        # Colisão entre balas e inimigos
        for bala in balas[:]:
            for inimigo in inimigos[:]:
                if bala.colliderect(inimigo):
                    balas.remove(bala)
                    inimigos.remove(inimigo)
                    score = score+1
                    break            

        # Desenho na tela
        tela.fill(BRANCO)
        pygame.draw.rect(tela, AZUL, (player_x, player_y, player_width, player_height))
        for bala in balas:
            pygame.draw.rect(tela, VERMELHO, bala)
        for inimigo in inimigos:
            pygame.draw.rect(tela, (0, 255, 0), inimigo)
        
        # Desenhando Score
        font = pygame.font.Font(None, 48)
        score_text = font.render(f'Pontos: {score}', True, (0, 255, 0))
        tela.blit(score_text, (10, 10))

        # Vida do Player
        life_text = font.render(f'Vida: {life}', True, (0, 255, 0))
        tela.blit(life_text, (680, 10))

        if life < 1:
            gameover_text = font.render("Pressione R para reiniciar", True, (255, 0, 0))
            restart_text = font.render("Pressione R para reiniciar", True, (255, 0, 0))
            centralizar = gameover_text.get_rect(center=(LARGURA // 2, ALTURA // 2))
            centralizar_restart = restart_text.get_rect(center=(LARGURA // 2, ALTURA // 2))
            tela.blit(gameover_text, centralizar)
            tela.blit(restart_text, centralizar_restart)

        #tela.blit(bg_image, (0, 0))
        #tela.blit(nave_player, (400, 300)) 

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

"""
Linhas 11, 28, 145, 146 estão comentadas
Inserir imagem player e imagem de fundo 
"""