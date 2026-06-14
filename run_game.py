#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Runner para o jogo Pygame - Projeto Final
Executa o jogo com tratamento de erros apropriado.
"""

import sys
import os

def main():
    """Funcao principal que executa o jogo."""
    try:
        print("Iniciando jogo...")
        print("-" * 40)
        
        # Importar e executar o jogo
        from src.jogo import executar_jogo
        
        # Rodar o loop principal
        executar_jogo()
        
        print("-" * 40)
        print("Obrigado por jogar!")
        
    except ImportError as e:
        print(f"Erro: Modulo nao encontrado: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro durante a execucao do jogo: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
