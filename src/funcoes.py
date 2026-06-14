def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


# ===== FUNÇÕES DO JOGO DA COBRA =====

def mover_cobra(cobra, direcao):
    """Move a cobra na direção especificada.
    
    A cobra é uma lista de dicionários com 'x' e 'y'.
    Adiciona um novo segmento na cabeça e remove o último.
    """
    cabeca = cobra[0].copy()
    
    # Calcula a nova posição da cabeça
    if direcao == "UP":
        cabeca["y"] -= 1
    elif direcao == "DOWN":
        cabeca["y"] += 1
    elif direcao == "LEFT":
        cabeca["x"] -= 1
    elif direcao == "RIGHT":
        cabeca["x"] += 1
    
    cobra.insert(0, cabeca)


def cobra_cresce(cobra):
    """A cobra cresce ao comer comida (não remove o último segmento)."""
    # Não fazemos nada aqui, pois o crescimento é feito por NÃO remover
    pass


def cobra_perde_segmento(cobra):
    """Remove o último segmento da cobra (movimento normal)."""
    if len(cobra) > 1:
        cobra.pop()


def cobra_colidiu_com_borda(cobra, largura_tela, altura_tela, tamanho_celula):
    """Verifica se a cabeça da cobra colidiu com a borda da tela."""
    cabeca = cobra[0]
    if cabeca["x"] < 0 or cabeca["x"] >= largura_tela // tamanho_celula:
        return True
    if cabeca["y"] < 0 or cabeca["y"] >= altura_tela // tamanho_celula:
        return True
    return False


def cobra_colidiu_consigo_mesma(cobra):
    """Verifica se a cobra colidiu consigo mesma."""
    cabeca = cobra[0]
    # Verifica se a cabeça está na mesma posição de algum segmento (a partir do terceiro)
    for segmento in cobra[4:]:  # Começa do quarto segmento
        if cabeca["x"] == segmento["x"] and cabeca["y"] == segmento["y"]:
            return True
    return False


def cobra_comeu_comida(cobra, comida):
    """Verifica se a cobra comeu a comida."""
    cabeca = cobra[0]
    return cabeca["x"] == comida["x"] and cabeca["y"] == comida["y"]


def gerar_comida_aleatoria(largura_tela, altura_tela, tamanho_celula, cobra):
    """Gera uma nova posição de comida aleatória que não colida com a cobra."""
    import random
    
    max_x = largura_tela // tamanho_celula
    max_y = altura_tela // tamanho_celula
    
    while True:
        x = random.randint(0, max_x - 1)
        y = random.randint(0, max_y - 1)
        
        # Verifica se não está na cobra
        colisao = False
        for segmento in cobra:
            if segmento["x"] == x and segmento["y"] == y:
                colisao = True
                break
        
        if not colisao:
            return {"x": x, "y": y}