# -*- coding: utf-8 -*-
"""
Loop principal do Jogo da Cobra
"""

import pygame
import time

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS_BASE, TITULO_JOGO, TAMANHO_CELULA,
    PRETO, VERDE, VERMELHO, BRANCO, CINZA, CINZA_CLARO,
    PONTOS_POR_COMIDA, ALIMENTOS_POR_NIVEL,
    CAMINHO_RECORDE,
)
from src.cobra import Cobra
from src.utils import (
    gerar_comida_aleatoria, calcular_velocidade, calcular_nivel, 
    obter_cor_cobra, limitar_valor
)
from src.pontuacao import salvar_recorde, carregar_recorde
from src.menu import exibir_menu_principal, exibir_tela_pausa, exibir_tela_game_over


def desenhar_hud(tela, pontos, alimentos, recorde, nivel, tamanho_cobra):
    """Desenha o HUD (informações na tela)."""
    fonte = pygame.font.Font(None, 24)
    
    info_pontos = f"Pontos: {pontos}"
    info_alimentos = f"Alimentos: {alimentos}"
    info_recorde = f"Recorde: {recorde}"
    info_nivel = f"Nível: {nivel}"
    info_tamanho = f"Tamanho: {tamanho_cobra}"
    
    texto_pontos = fonte.render(info_pontos, True, VERDE)
    texto_alimentos = fonte.render(info_alimentos, True, BRANCO)
    texto_recorde = fonte.render(info_recorde, True, CINZA_CLARO)
    texto_nivel = fonte.render(info_nivel, True, BRANCO)
    texto_tamanho = fonte.render(info_tamanho, True, BRANCO)
    
    x_start = 10
    y = 5
    
    tela.blit(texto_pontos, (x_start, y))
    tela.blit(texto_alimentos, (x_start + 150, y))
    tela.blit(texto_recorde, (x_start + 300, y))
    tela.blit(texto_nivel, (x_start + 470, y))
    tela.blit(texto_tamanho, (x_start + 600, y))


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
    altura_celulas = ALTURA_TELA // TAMANHO_CELULA
    
    cobra = Cobra(largura_celulas // 2, altura_celulas // 2)
    comida = gerar_comida_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA, cobra.corpo)
    
    pontos = 0
    alimentos_coletados = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    
    game_over = False
    tempo_inicio = time.time()
    
    # Loop principal do jogo
    rodando = True
    while rodando:
        fps_atual = calcular_velocidade(alimentos_coletados, FPS_BASE)
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
                    tempo_inicio = time.time() - (time.time() - tempo_inicio)  # Ajusta tempo
                elif evento.key == pygame.K_UP:
                    cobra.definir_direcao("UP")
                elif evento.key == pygame.K_DOWN:
                    cobra.definir_direcao("DOWN")
                elif evento.key == pygame.K_LEFT:
                    cobra.definir_direcao("LEFT")
                elif evento.key == pygame.K_RIGHT:
                    cobra.definir_direcao("RIGHT")
        
        # Atualiza o jogo
        if not game_over:
            cobra.mover()
            
            # Verifica colisão com comida
            if cobra.comeu_comida(comida):
                alimentos_coletados += 1
                pontos += PONTOS_POR_COMIDA
                cobra.comer()  # Cresce
                comida = gerar_comida_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA, cobra.corpo)
            else:
                cobra.remover_cauda()  # Movimento normal (sem crescimento)
            
            # Verifica colisão com bordas
            if cobra.colidiu_com_borda(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA):
                game_over = True
            
            # Verifica auto-colisão
            elif cobra.colidiu_consigo_mesma():
                game_over = True
        
        # Atualiza recorde se necessário
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)
        
        # Desenha a cena
        tela.fill(PRETO)
        
        # Desenha HUD
        nivel = calcular_nivel(alimentos_coletados)
        desenhar_hud(tela, pontos, alimentos_coletados, recorde, nivel, cobra.obter_tamanho())
        desenhar_instrucoes(tela)
        
        # Desenha a cobra com cor que muda conforme nível
        cor_cobra = obter_cor_cobra(nivel)
        cor_cabeca = (min(cor_cobra[0] + 55, 255), min(cor_cobra[1] + 55, 255), min(cor_cobra[2] + 55, 255))
        
        for i, segmento in enumerate(cobra.corpo):
            x_pixel = segmento["x"] * TAMANHO_CELULA
            y_pixel = segmento["y"] * TAMANHO_CELULA + 30  # Offset para HUD
            
            cor = cor_cabeca if i == 0 else cor_cobra
            pygame.draw.rect(tela, cor, (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA))
            pygame.draw.rect(tela, (0, 0, 0), (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA), 1)
        
        # Desenha a comida
        x_pixel = comida["x"] * TAMANHO_CELULA
        y_pixel = comida["y"] * TAMANHO_CELULA + 30
        pygame.draw.rect(tela, VERMELHO, (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA))
        pygame.draw.rect(tela, (150, 0, 0), (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA), 2)
        
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
        print(f"\n=== RECORDE ===\nMelhor pontuação: {recorde} pontos\n")
        # Volta ao menu
        executar_jogo()
        return
    
    # Loop de jogos
    while True:
        jogar_novamente = executar_jogo_sessao(tela)
        
        if not jogar_novamente:
            break
    
    pygame.quit()
