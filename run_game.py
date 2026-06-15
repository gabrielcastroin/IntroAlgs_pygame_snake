#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Runner do Jogo da Cobra com tratamento de erros
"""

import sys
import os


def verificar_dependencias():
    """Verifica se as dependências estão instaladas."""
    try:
        import pygame
        print(f"✓ Pygame {pygame.__version__} encontrado")
        return True
    except ImportError:
        print("✗ Pygame não está instalado!")
        print("  Execute: pip install pygame")
        return False


def verificar_diretorios():
    """Verifica e cria diretórios necessários."""
    diretorios = ["data", "assets/imagens", "assets/sons", "assets/fontes"]
    
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"✓ Diretório '{diretorio}' criado")


def main():
    """Função principal do runner."""
    print("\n" + "="*50)
    print("  JOGO DA COBRA - Inicializando...")
    print("="*50 + "\n")
    
    # Verifica dependências
    print("[1/3] Verificando dependências...")
    if not verificar_dependencias():
        print("\nInstalação de dependências abortada.")
        sys.exit(1)
    
    # Verifica diretórios
    print("\n[2/3] Verificando diretórios...")
    verificar_diretorios()
    
    # Inicia o jogo
    print("\n[3/3] Iniciando jogo...")
    print("="*50 + "\n")
    
    try:
        from src.jogo import executar_jogo
        executar_jogo()
    except Exception as e:
        print(f"\n✗ Erro ao executar o jogo:")
        print(f"  {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n✓ Jogo encerrado com sucesso!")


if __name__ == "__main__":
    main()
