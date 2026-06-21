# -*- coding: utf-8 -*-
"""
Configurações centrais do jogo
"""

# ===== TELA =====
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS_BASE = 10  # FPS inicial - aumenta conforme nível
TITULO_JOGO = "🐍 Jogo da Cobra"

# ===== CORES (RGB) =====
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (128, 128, 128)
CINZA_CLARO = (212, 212, 212)
VERDE = (0, 200, 0)
VERDE_CLARO = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
LARANJA = (255, 165, 0)

# Cores Temáticas Modificadas (Visual do Print)
FUNDO_1 = (37, 40, 61)      # Azul escuro fundo
FUNDO_2 = (46, 50, 74)      # Azul menos escuro fundo (xadrez)
FUNDO_HUD = (30, 32, 50)    # Cor da barra superior (HUD)
COR_OBSTACULO = (120, 120, 150) # Bloquinhos do labirinto
COR_LETRA_HUD = (180, 190, 220)

# ===== JOGO DA COBRA =====
TAMANHO_CELULA = 20  # Tamanho de cada célula em pixels
PONTOS_POR_COMIDA = 10
ALIMENTOS_POR_NIVEL = 5  # A cada 5 alimentos coletados, aumenta nível

# ===== SISTEMA DE JOGO =====
# Nota: Sistema de vidas/tempo foi adicionado como melhoria,
# mas pode ser desativado alterando o modo de jogo

# ===== CAMINHOS DE ARQUIVOS =====
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.json"
CAMINHO_LOG_PONTUACOES = "data/log_pontuacoes.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"