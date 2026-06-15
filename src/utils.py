# -*- coding: utf-8 -*-
"""
Módulo de Utilidades - Funções auxiliares do jogo
"""

import random


def gerar_comida_aleatoria(largura_tela, altura_tela, tamanho_celula, cobra_corpo):
    """
    Gera uma nova posição de comida aleatória que não colida com a cobra.
    
    Args:
        largura_tela: Largura da tela em pixels
        altura_tela: Altura da tela em pixels
        tamanho_celula: Tamanho de cada célula em pixels
        cobra_corpo: Lista com o corpo da cobra
    
    Returns:
        Dict com coordenadas {"x": ..., "y": ...}
    """
    max_x = largura_tela // tamanho_celula
    max_y = altura_tela // tamanho_celula
    
    while True:
        x = random.randint(0, max_x - 1)
        y = random.randint(0, max_y - 1)
        
        # Verifica se não está na cobra
        colisao = False
        for segmento in cobra_corpo:
            if segmento["x"] == x and segmento["y"] == y:
                colisao = True
                break
        
        if not colisao:
            return {"x": x, "y": y}


def calcular_velocidade(alimentos_coletados, fps_base=10):
    """
    Calcula a velocidade (FPS) baseada em alimentos coletados.
    A cada 5 alimentos, aumenta 1 FPS.
    
    Args:
        alimentos_coletados: Número de alimentos já coletados
        fps_base: FPS inicial (padrão 10)
    
    Returns:
        int: FPS atual (máximo 25)
    """
    nivel = alimentos_coletados // 5
    velocidade = fps_base + nivel
    return min(velocidade, 25)  # Máximo 25 FPS


def calcular_nivel(alimentos_coletados):
    """
    Calcula o nível baseado em alimentos coletados.
    A cada 5 alimentos = 1 nível.
    
    Args:
        alimentos_coletados: Número de alimentos coletados
    
    Returns:
        int: Nível (mínimo 1)
    """
    return max(1, alimentos_coletados // 5 + 1)


def obter_cor_cobra(nivel):
    """
    Retorna a cor da cobra baseada no nível.
    Muda de cor conforme o nível aumenta.
    
    Args:
        nivel: Nível atual
    
    Returns:
        Tuple: Cor RGB (r, g, b)
    """
    cores = [
        (0, 200, 0),        # Nível 1: Verde
        (0, 255, 100),      # Nível 2: Verde claro
        (100, 255, 0),      # Nível 3: Verde amarelado
        (255, 200, 0),      # Nível 4: Amarelo
        (255, 150, 0),      # Nível 5: Laranja
        (255, 100, 0),      # Nível 6: Laranja escuro
        (255, 0, 0),        # Nível 7+: Vermelho
    ]
    
    indice = min(nivel - 1, len(cores) - 1)
    return cores[indice]


def limitar_valor(valor, minimo, maximo):
    """
    Limita um valor dentro de um intervalo.
    
    Args:
        valor: Valor a ser limitado
        minimo: Valor mínimo
        maximo: Valor máximo
    
    Returns:
        Valor limitado
    """
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor
