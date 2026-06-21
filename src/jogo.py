# -*- coding: utf-8 -*-
"""
Loop principal do Jogo da Cobra
"""

import pygame
import time

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS_BASE, TITULO_JOGO, TAMANHO_CELULA,
    VERDE, VERMELHO, BRANCO, CINZA, CINZA_CLARO,
    PONTOS_POR_COMIDA, 
    FUNDO_1, FUNDO_2, FUNDO_HUD, COR_OBSTACULO, COR_LETRA_HUD,
    CAMINHO_RECORDE,
)
from src.cobra import Cobra
from src.utils import (
    gerar_comida_aleatoria, calcular_velocidade, calcular_nivel, 
    obter_cor_cobra, limitar_valor
)
from src.pontuacao import salvar_recorde, carregar_recorde
from src.menu import exibir_menu_principal, exibir_tela_pausa, exibir_tela_game_over


def desenhar_hud(tela, pontos, nivel, hp, fonte=None):
    """
    Desenha o HUD estilo 'SCORE: 0128   LEVEL: 06   [Corações]'
    """
    if fonte is None:
        fonte = pygame.font.Font(None, 36)
        
    pygame.draw.rect(tela, FUNDO_HUD, (0, 0, LARGURA_TELA, 40))
    pygame.draw.rect(tela, (20, 22, 35), (0, 38, LARGURA_TELA, 2)) # Sombra
    
    # Texto SCORE
    txt_score = fonte.render(f"SCORE:{pontos:04d}", True, COR_LETRA_HUD)
    tela.blit(txt_score, (20, 10))
    
    # Texto LEVEL
    txt_level = fonte.render(f"LEVEL:{nivel:02d}", True, COR_LETRA_HUD)
    tela.blit(txt_level, (LARGURA_TELA // 2 - txt_level.get_width() // 2, 10))
    
    # Corações (HP)
    # Total de HP: 6 (3 corações inteiros * 2 metades)
    x_icon = LARGURA_TELA - 40
    for i in range(3):
        # hp vai de 0 a 6
        valor = max(0, min(2, hp - (2-i)*2))
        
        # Desenha coracoes simplificados com Pygame
        # Numa implementacao real isso seria um .blit() de imagem de coracao
        if valor == 2:
            # Inteiro
            pygame.draw.circle(tela, VERMELHO, (x_icon + 10, 20), 8)
            pygame.draw.circle(tela, VERMELHO, (x_icon + 20, 20), 8)
            pygame.draw.polygon(tela, VERMELHO, [(x_icon + 2, 22), (x_icon + 28, 22), (x_icon + 15, 32)])
        elif valor == 1:
            # Metade
            pygame.draw.circle(tela, VERMELHO, (x_icon + 10, 20), 8)
            pygame.draw.circle(tela, (50, 0, 0), (x_icon + 20, 20), 8)
            pygame.draw.polygon(tela, VERMELHO, [(x_icon + 2, 22), (x_icon + 15, 22), (x_icon + 15, 32)])
            pygame.draw.polygon(tela, (50, 0, 0), [(x_icon + 15, 22), (x_icon + 28, 22), (x_icon + 15, 32)])
        else:
            # Vazio
            pygame.draw.circle(tela, (50, 0, 0), (x_icon + 10, 20), 8)
            pygame.draw.circle(tela, (50, 0, 0), (x_icon + 20, 20), 8)
            pygame.draw.polygon(tela, (50, 0, 0), [(x_icon + 2, 22), (x_icon + 28, 22), (x_icon + 15, 32)])
            
        x_icon -= 35

def desenhar_instrucoes(tela):
    """Desenha instruções na parte inferior da tela."""
    fonte = pygame.font.Font(None, 20)
    instrucao = fonte.render("ESC: Pausar | Setas: Controlar cobra", True, CINZA)
    tela.blit(instrucao, (10, ALTURA_TELA - 25))


def executar_jogo_sessao(tela):
    """
    Executa uma sessão completa de jogo.
    
    Args:
        tela: Objeto pygame display
    
    Returns:
        bool: True se quer jogar novamente, False se quer sair
    """
    relogio = pygame.time.Clock()
    
    # Inicialização
    largura_celulas = LARGURA_TELA // TAMANHO_CELULA
    altura_celulas = (ALTURA_TELA - 40) // TAMANHO_CELULA
    
    # Gerador de labirinto simples
    def gerar_labirinto():
        import random
        obstaculos = []
        # Cria uns "bloquinhos" de 3x3 espalhados pela tela
        for _ in range(3):
            px = random.randint(3, largura_celulas - 4)
            py = random.randint(3, altura_celulas - 4)
            for dx, dy in [(0,0), (1,0), (-1,0), (0,1), (0,-1)]:
                obstaculos.append({"x": px + dx, "y": py + dy})
        return obstaculos

    cobra = Cobra(largura_celulas // 2, altura_celulas // 2)
    obstaculos = []
    comida = gerar_comida_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA, cobra.corpo, obstaculos)
    
    pontos = 0
    alimentos_coletados = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    
    hp = 6  # 3 corações inteiros * 2 metades (1 colisão custa 1)
    
    game_over = False
    
    tempo_inicio = time.time()
    tempo_imunidade = 0
    
    # Temporizadores para os efeitos das comidas especiais
    tempo_velocidade = 0
    tempo_inversao = 0
    
    # Status Labirinto
    avisando_labirinto = False
    labirinto_ativo = False
    
    # Imagens pre-carregadas (Simulação de Load - fallbacks p/ Pygame)
    # Exemplo: img_maca = pygame.image.load("assets/imagens/fruta_normal.png").convert_alpha()
    
    # Loop principal do jogo
    rodando = True
    while rodando:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicio
        segundos_totais = int(tempo_decorrido)
        
        # Lógica temporal do obstáculo (60s loop)
        ciclo = segundos_totais % 60
        if ciclo >= 55:
            if not avisando_labirinto:
                avisando_labirinto = True
                obstaculos = []
                labirinto_ativo = False
        elif ciclo < 30:
            if not labirinto_ativo:
                avisando_labirinto = False
                labirinto_ativo = True
                obstaculos = gerar_labirinto()
        else:
            obstaculos = []
            avisando_labirinto = False
            labirinto_ativo = False

        is_rapido = tempo_velocidade > tempo_atual
        is_invertido = tempo_inversao > tempo_atual
        is_imune = tempo_imunidade > tempo_atual
        
        fps_atual = calcular_velocidade(alimentos_coletados, FPS_BASE)
        if is_rapido:
            fps_atual = min(45, int(fps_atual * 1.5))
            
        relogio.tick(fps_atual)
        
        # Captura eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    continuar = exibir_tela_pausa(tela)
                    if not continuar:
                        return False
                    # Ajusta temporizadores de efeitos após a pausa
                    dif = time.time() - tempo_atual
                    if is_rapido: tempo_velocidade += dif
                    if is_invertido: tempo_inversao += dif
                    if is_imune: tempo_imunidade += dif
                    tempo_inicio += dif
                elif evento.key == pygame.K_UP:
                    cobra.definir_direcao("DOWN" if is_invertido else "UP")
                elif evento.key == pygame.K_DOWN:
                    cobra.definir_direcao("UP" if is_invertido else "DOWN")
                elif evento.key == pygame.K_LEFT:
                    cobra.definir_direcao("RIGHT" if is_invertido else "LEFT")
                elif evento.key == pygame.K_RIGHT:
                    cobra.definir_direcao("LEFT" if is_invertido else "RIGHT")
        
        # Atualiza o jogo
        if not game_over:
            cobra.mover()
            cobra.atravessar_borda(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA)
            
            cabeca = cobra.corpo[0]
            
            # Checa colisão c/ comida
            if cobra.comeu_comida(comida):
                tipo = comida.get("tipo", "NORMAL")
                alimentos_coletados += 1
                
                if tipo == "NORMAL":
                    pontos += PONTOS_POR_COMIDA
                    cobra.comer()
                elif tipo == "OURO":
                    pontos += PONTOS_POR_COMIDA * 3
                    cobra.comer()
                    tempo_velocidade = tempo_atual + 5.0
                elif tipo == "PIMENTA":
                    pontos += PONTOS_POR_COMIDA
                    cobra.comer()
                    tempo_inversao = tempo_atual + 5.0
                elif tipo == "COGUMELO":
                    pontos += PONTOS_POR_COMIDA
                    novo_tam = max(3, len(cobra.corpo) // 2)
                    cobra.corpo = cobra.corpo[:novo_tam]
                elif tipo == "MORANGO":
                    pontos += PONTOS_POR_COMIDA * 2
                    hp = min(6, hp + 2) # Cura 1 coração inteiro
                    cobra.comer()
                
                comida = gerar_comida_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA, cobra.corpo, obstaculos)
            else:
                cobra.remover_cauda()
                
            # Verifica colisões se não estiver imune
            if not is_imune:
                colidiu_agora = False
                
                # Auto-colisão
                if cobra.colidiu_consigo_mesma():
                    colidiu_agora = True
                
                # Labirinto
                for obs in obstaculos:
                    if cabeca["x"] == obs["x"] and cabeca["y"] == obs["y"]:
                        colidiu_agora = True
                        break
                        
                if colidiu_agora:
                    hp -= 1
                    if hp <= 0:
                        game_over = True
                    else:
                        tempo_imunidade = tempo_atual + 2.0
                        
        
        # Atualiza recorde se necessário
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)
        
        # Define o background (XADREZ AZUL ESCURO)
        for y in range(altura_celulas):
            for x in range(largura_celulas):
                cor_fundo = FUNDO_1 if (x+y)%2 == 0 else FUNDO_2
                pygame.draw.rect(tela, cor_fundo, (x * TAMANHO_CELULA, y * TAMANHO_CELULA + 40, TAMANHO_CELULA, TAMANHO_CELULA))
        
        # Desenha Obstáculos
        for obs in obstaculos:
            px = obs["x"] * TAMANHO_CELULA
            py = obs["y"] * TAMANHO_CELULA + 40
            pygame.draw.rect(tela, COR_OBSTACULO, (px, py, TAMANHO_CELULA, TAMANHO_CELULA))
        
        # Desenha HUD
        nivel = calcular_nivel(alimentos_coletados)
        desenhar_hud(tela, pontos, nivel, hp)
        
        # EFEITOS ATIVOS
        fonte_efeito = pygame.font.Font(None, 24)
        if is_rapido or is_invertido or avisando_labirinto:
            textos = []
            if is_rapido: textos.append(("VELOCIDADE!", (255, 255, 0)))
            if is_invertido: textos.append(("INVERTIDO!", (255, 100, 100)))
            if avisando_labirinto: textos.append((f"LABIRINTO EM {60 - ciclo}...", (255, 150, 0)))
            
            x_offset = 250
            for txt, cor in textos:
                img = fonte_efeito.render(txt, True, cor)
                tela.blit(img, (x_offset, 15))
                x_offset += 160
        
        # Desenha a cobra (Se imune, pisca sumindo frames alternados)
        piscarFrame = is_imune and int(tempo_atual * 10) % 2 == 0
        if not piscarFrame:
            cor_cobra = obter_cor_cobra(nivel)
            cor_cabeca = (min(cor_cobra[0] + 55, 255), min(cor_cobra[1] + 55, 255), min(cor_cobra[2] + 55, 255))
            
            for i, segmento in enumerate(cobra.corpo):
                x_pixel = segmento["x"] * TAMANHO_CELULA
                y_pixel = segmento["y"] * TAMANHO_CELULA + 40
                
                cor = cor_cabeca if i == 0 else cor_cobra
                # Ideal: Aqui seria `tela.blit(IMG_CORPO, (x, y))`
                pygame.draw.rect(tela, cor, (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.draw.rect(tela, (20, 22, 35), (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA), 1)
        
        # Desenha a comida
        x_pixel = comida["x"] * TAMANHO_CELULA
        y_pixel = comida["y"] * TAMANHO_CELULA + 40
        
        tipo_comida = comida.get("tipo", "NORMAL")
        # Ideal: Aqui seria `tela.blit(IMG_MACA, (x, y))` de acordo com o tipo
        if tipo_comida == "NORMAL":
            pygame.draw.circle(tela, VERMELHO, (x_pixel + 10, y_pixel + 10), 8)
            pygame.draw.circle(tela, (0, 100, 0), (x_pixel + 10, y_pixel + 3), 3) # Cabinho verde
        elif tipo_comida == "OURO":
            pygame.draw.circle(tela, (255, 215, 0), (x_pixel + 10, y_pixel + 10), 9)
            pygame.draw.circle(tela, (255, 255, 255), (x_pixel + 6, y_pixel + 6), 3) # Brilho
        elif tipo_comida == "PIMENTA":
            pygame.draw.polygon(tela, (255, 60, 60), [(x_pixel+5, y_pixel+15), (x_pixel+15, y_pixel+15), (x_pixel+10, y_pixel+5)])
        elif tipo_comida == "COGUMELO":
            pygame.draw.circle(tela, (200, 100, 255), (x_pixel + 10, y_pixel + 8), 8)
            pygame.draw.rect(tela, (250, 250, 250), (x_pixel + 7, y_pixel + 12, 6, 6))
        elif tipo_comida == "MORANGO":
            pygame.draw.polygon(tela, (255, 20, 80), [(x_pixel+2, y_pixel+5), (x_pixel+18, y_pixel+5), (x_pixel+10, y_pixel+18)])
            pygame.draw.rect(tela, (0, 150, 0), (x_pixel + 7, y_pixel, 6, 4)) # folha do morango
        
        # Se game over, exibe tela e aguarda ação
        if game_over:
            resultado = exibir_tela_game_over(tela, pontos, alimentos_coletados, recorde)
            if resultado == "REINICIAR":
                return True
            else:
                return False
        
        pygame.display.flip()
    
    return False


def executar_jogo():
    """Executa o jogo completo com menu e loop de sessões."""
    pygame.init()
    
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    
    # Menu principal
    acao = exibir_menu_principal(tela)
    
    if acao == "SAIR":
        pygame.quit()
        return
    elif acao == "RECORDES":
        recorde = carregar_recorde(CAMINHO_RECORDE)
        from src.menu import exibir_tela_recordes
        exibir_tela_recordes(tela, recorde)
        # Volta ao menu
        executar_jogo()
        return
    
    # Loop de jogos
    while True:
        jogar_novamente = executar_jogo_sessao(tela)
        
        if not jogar_novamente:
            break
    
    pygame.quit()
