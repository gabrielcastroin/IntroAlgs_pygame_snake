# -*- coding: utf-8 -*-
"""
Módulo de Pontuação - Leitura e escrita de recordes
"""


def salvar_recorde(caminho_arquivo, pontuacao):
    """
    Salva a pontuação recorde em arquivo texto.
    
    Args:
        caminho_arquivo: Caminho do arquivo de recorde
        pontuacao: Pontuação a ser salva
    """
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(str(pontuacao))
    except Exception as e:
        print(f"Erro ao salvar recorde: {e}")


def carregar_recorde(caminho_arquivo):
    """
    Carrega o recorde salvo; retorna 0 se não existir valor válido.
    
    Args:
        caminho_arquivo: Caminho do arquivo de recorde
    
    Returns:
        int: Recorde salvo ou 0 se arquivo não existir
    """
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            
            if conteudo == "":
                return 0
            
            return int(conteudo)
    
    except FileNotFoundError:
        return 0
    except ValueError:
        print("Erro: Valor inválido no arquivo de recorde")
        return 0


def registrar_pontuacao(caminho_arquivo, nome_jogador, pontuacao, alimentos):
    """
    Registra a pontuação em log (futuro para ranking expandido).
    
    Args:
        caminho_arquivo: Caminho do arquivo de log
        nome_jogador: Nome do jogador
        pontuacao: Pontuação alcançada
        alimentos: Alimentos coletados
    """
    try:
        with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
            linha = f"{nome_jogador} - {pontuacao} pontos ({alimentos} alimentos)\n"
            arquivo.write(linha)
    except Exception as e:
        print(f"Erro ao registrar pontuação: {e}")
