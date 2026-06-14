#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script de teste para validar que o projeto está funcionando."""

import sys
import os

print("=" * 60)
print("TESTE DE IMPORTACOES - PROJETO PYGAME")
print("=" * 60)

# Testes
testes_ok = True

# 1. Pygame
try:
    import pygame
    print(f"[OK] Pygame {pygame.__version__}")
except ImportError as e:
    print(f"[ERRO] Pygame: {e}")
    testes_ok = False

# 2. Modulos locais
try:
    from src.config import (
        LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
        BRANCO, PRETO, CINZA,
        CAMINHO_RECORDE, CAMINHO_SPRITES
    )
    print(f"[OK] config.py - Tela: {LARGURA_TELA}x{ALTURA_TELA} @ {FPS}FPS")
except ImportError as e:
    print(f"[ERRO] config.py: {e}")
    testes_ok = False

try:
    from src.dados import salvar_recorde, carregar_recorde
    print(f"[OK] dados.py")
except ImportError as e:
    print(f"[ERRO] dados.py: {e}")
    testes_ok = False

try:
    from src.funcoes import (
        calcular_pontos, tomar_dano, jogador_perdeu,
        limitar_valor, verificar_colisao
    )
    print(f"[OK] funcoes.py")
except ImportError as e:
    print(f"[ERRO] funcoes.py: {e}")
    testes_ok = False

try:
    from src.sprites import pegar_sprite
    print(f"[OK] sprites.py")
except ImportError as e:
    print(f"[ERRO] sprites.py: {e}")
    testes_ok = False

try:
    from src.jogo import executar_jogo
    print(f"[OK] jogo.py")
except ImportError as e:
    print(f"[ERRO] jogo.py: {e}")
    testes_ok = False

# 3. Verificar arquivos necessarios
print("\n" + "=" * 60)
print("VERIFICACAO DE ARQUIVOS")
print("=" * 60)

arquivos_necessarios = [
    "data/recorde.txt",
    "assets/imagens/spritesheet.bmp",
]

for arquivo in arquivos_necessarios:
    caminho = f"c:/Users/Daniel Guerra/OneDrive/Documentos/GitHub/IntroAlgs_pygame_template/{arquivo}"
    if os.path.exists(caminho):
        tamanho = os.path.getsize(caminho)
        print(f"[OK] {arquivo} ({tamanho} bytes)")
    else:
        print(f"[AVISO] {arquivo} nao encontrado")

print("\n" + "=" * 60)
if testes_ok:
    print("RESULTADO: TODOS OS TESTES PASSARAM!")
    print("O projeto esta pronto para rodar com: python main.py")
else:
    print("RESULTADO: ALGUNS TESTES FALHARAM")
print("=" * 60)
