# -*- coding: utf-8 -*-
"""
Módulo de Menu - Telas do menu inicial
"""

import pygame
from src.config import (
    LARGURA_TELA, ALTURA_TELA, BRANCO, PRETO, VERDE, VERMELHO, AMARELO, CINZA
)


def exibir_menu_principal(tela):
    """
    Exibe o menu principal e retorna a escolha do jogador.
    
    Args:
        tela: Objeto pygame display
    
    Returns:
        str: "JOGAR", "RECORDES" ou "SAIR"
    """
    relogio = pygame.time.Clock()
    opcao_selecionada = 0
    opcoes = ["JOGAR", "RECORDES", "SAIR"]
    
    selecionando = True
    while selecionando:
        relogio.tick(30)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "SAIR"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
                elif evento.key == pygame.K_DOWN:
                    opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN:
                    return opcoes[opcao_selecionada]
        
        # Desenha menu
        tela.fill(PRETO)
        
        fonte_titulo = pygame.font.Font(None, 72)
        fonte_opcao = pygame.font.Font(None, 48)
        fonte_info = pygame.font.Font(None, 24)
        
        titulo = fonte_titulo.render("JOGO DA COBRA", True, VERDE)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 80))
        
        y = 250
        for i, opcao in enumerate(opcoes):
            cor = AMARELO if i == opcao_selecionada else BRANCO
            texto = fonte_opcao.render(opcao, True, cor)
            tela.blit(texto, (LARGURA_TELA // 2 - texto.get_width() // 2, y))
            y += 80
        
        info = fonte_info.render("Use SETA ACIMA/ABAIXO para navegador e ENTER para selecionar", True, CINZA)
        tela.blit(info, (LARGURA_TELA // 2 - info.get_width() // 2, ALTURA_TELA - 50))
        
        pygame.display.flip()
    
    return "SAIR"


def exibir_tela_pausa(tela):
    """
    Exibe a tela de pausa.
    
    Args:
        tela: Objeto pygame display
    
    Returns:
        bool: True se continuar, False se sair
    """
    relogio = pygame.time.Clock()
    
    aguardando = True
    while aguardando:
        relogio.tick(30)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return True
                elif evento.key == pygame.K_q:
                    return False
        
        # Overlay de pausa
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(128)
        overlay.fill(PRETO)
        tela.blit(overlay, (0, 0))
        
        fonte_titulo = pygame.font.Font(None, 72)
        fonte_normal = pygame.font.Font(None, 36)
        
        titulo = fonte_titulo.render("PAUSADO", True, AMARELO)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 200))
        
        instrucao1 = fonte_normal.render("Pressione ESC para continuar", True, BRANCO)
        instrucao2 = fonte_normal.render("Pressione Q para sair", True, VERMELHO)
        
        tela.blit(instrucao1, (LARGURA_TELA // 2 - instrucao1.get_width() // 2, 350))
        tela.blit(instrucao2, (LARGURA_TELA // 2 - instrucao2.get_width() // 2, 430))
        
        pygame.display.flip()
    
    return False


def exibir_tela_game_over(tela, pontos, alimentos, recorde):
    """
    Exibe a tela de game over.
    
    Args:
        tela: Objeto pygame display
        pontos: Pontos do jogo
        alimentos: Alimentos coletados
        recorde: Recorde salvo
    
    Returns:
        str: "REINICIAR" ou "SAIR"
    """
    relogio = pygame.time.Clock()
    
    aguardando = True
    while aguardando:
        relogio.tick(30)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "SAIR"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return "REINICIAR"
                elif evento.key == pygame.K_ESCAPE:
                    return "SAIR"
        
        tela.fill(PRETO)
        
        fonte_titulo = pygame.font.Font(None, 72)
        fonte_grande = pygame.font.Font(None, 48)
        fonte_normal = pygame.font.Font(None, 32)
        fonte_pequena = pygame.font.Font(None, 24)
        
        titulo = fonte_titulo.render("GAME OVER", True, VERMELHO)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 60))
        
        pontos_text = fonte_grande.render(f"Pontos: {pontos}", True, AMARELO)
        alimentos_text = fonte_normal.render(f"Alimentos coletados: {alimentos}", True, BRANCO)
        recorde_text = fonte_normal.render(f"Recorde: {recorde}", True, VERDE if pontos < recorde else AMARELO)
        
        y = 220
        tela.blit(pontos_text, (LARGURA_TELA // 2 - pontos_text.get_width() // 2, y))
        y += 80
        tela.blit(alimentos_text, (LARGURA_TELA // 2 - alimentos_text.get_width() // 2, y))
        y += 60
        tela.blit(recorde_text, (LARGURA_TELA // 2 - recorde_text.get_width() // 2, y))
        
        if pontos > recorde:
            novo_recorde = fonte_normal.render("NOVO RECORDE!", True, VERDE)
            tela.blit(novo_recorde, (LARGURA_TELA // 2 - novo_recorde.get_width() // 2, y + 80))
        
        instrucao1 = fonte_pequena.render("Pressione R para reiniciar", True, BRANCO)
        instrucao2 = fonte_pequena.render("Pressione ESC para sair", True, CINZA)
        
        tela.blit(instrucao1, (LARGURA_TELA // 2 - instrucao1.get_width() // 2, ALTURA_TELA - 100))
        tela.blit(instrucao2, (LARGURA_TELA // 2 - instrucao2.get_width() // 2, ALTURA_TELA - 50))
        
        pygame.display.flip()
    
    return "SAIR"


def exibir_tela_recordes(tela, recorde):
    """
    Exibe a tela de recordes.
    
    Args:
        tela: Objeto pygame display
        recorde: O valor do recorde atual
    """
    relogio = pygame.time.Clock()
    aguardando = True
    
    while aguardando:
        relogio.tick(30)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_RETURN:
                    return
                    
        tela.fill(PRETO)
        
        fonte_titulo = pygame.font.Font(None, 72)
        fonte_normal = pygame.font.Font(None, 48)
        fonte_pequena = pygame.font.Font(None, 24)
        
        titulo = fonte_titulo.render("RECORDES", True, AMARELO)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 80))
        
        texto_recorde = fonte_normal.render(f"Melhor Pontuação: {recorde}", True, BRANCO)
        tela.blit(texto_recorde, (LARGURA_TELA // 2 - texto_recorde.get_width() // 2, 250))
        
        instrucao = fonte_pequena.render("Pressione ESC ou ENTER para voltar", True, CINZA)
        tela.blit(instrucao, (LARGURA_TELA // 2 - instrucao.get_width() // 2, ALTURA_TELA - 50))
        
        pygame.display.flip()

