from src.funcoes import (
    calcular_pontos,
    limitar_valor,
    mover_cobra,
    cobra_perde_segmento,
    cobra_colidiu_com_borda,
    cobra_colidiu_consigo_mesma,
    cobra_comeu_comida,
)
from src.config import LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA


# ===== TESTES BASICOS =====

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_zero():
    """Deve funcionar com pontos zerados."""
    assert calcular_pontos(0, 10) == 10


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


# ===== TESTES DO JOGO DA COBRA =====

def test_mover_cobra_direita():
    """A cobra deve se mover para a direita."""
    cobra = [{"x": 10, "y": 10}, {"x": 9, "y": 10}]
    mover_cobra(cobra, "RIGHT")
    # Nova cabeca adicionada
    assert cobra[0]["x"] == 11
    assert cobra[0]["y"] == 10


def test_mover_cobra_esquerda():
    """A cobra deve se mover para a esquerda."""
    cobra = [{"x": 10, "y": 10}, {"x": 9, "y": 10}]
    mover_cobra(cobra, "LEFT")
    assert cobra[0]["x"] == 9
    assert cobra[0]["y"] == 10


def test_mover_cobra_acima():
    """A cobra deve se mover para acima."""
    cobra = [{"x": 10, "y": 10}, {"x": 9, "y": 10}]
    mover_cobra(cobra, "UP")
    assert cobra[0]["x"] == 10
    assert cobra[0]["y"] == 9


def test_mover_cobra_abaixo():
    """A cobra deve se mover para abaixo."""
    cobra = [{"x": 10, "y": 10}, {"x": 9, "y": 10}]
    mover_cobra(cobra, "DOWN")
    assert cobra[0]["x"] == 10
    assert cobra[0]["y"] == 11


def test_cobra_perde_segmento():
    """Ao se mover, a cobra perde o ultimo segmento (sem crescimento)."""
    cobra = [{"x": 10, "y": 10}, {"x": 9, "y": 10}, {"x": 8, "y": 10}]
    tamanho_inicial = len(cobra)
    mover_cobra(cobra, "RIGHT")
    cobra_perde_segmento(cobra)
    assert len(cobra) == tamanho_inicial


def test_cobra_colidiu_com_borda_esquerda():
    """Cobra deve colidir ao sair pela esquerda."""
    cobra = [{"x": -1, "y": 10}]
    assert cobra_colidiu_com_borda(cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA)


def test_cobra_colidiu_com_borda_direita():
    """Cobra deve colidir ao sair pela direita."""
    max_x = LARGURA_TELA // TAMANHO_CELULA
    cobra = [{"x": max_x, "y": 10}]
    assert cobra_colidiu_com_borda(cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA)


def test_cobra_colidiu_com_borda_cima():
    """Cobra deve colidir ao sair pela cima."""
    cobra = [{"x": 10, "y": -1}]
    assert cobra_colidiu_com_borda(cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA)


def test_cobra_colidiu_com_borda_baixo():
    """Cobra deve colidir ao sair pela baixo."""
    max_y = ALTURA_TELA // TAMANHO_CELULA
    cobra = [{"x": 10, "y": max_y}]
    assert cobra_colidiu_com_borda(cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA)


def test_cobra_nao_colidiu_com_borda():
    """Cobra dentro da tela nao deve colidir com bordas."""
    cobra = [{"x": 10, "y": 10}]
    assert not cobra_colidiu_com_borda(cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA)


def test_cobra_colidiu_consigo_mesma():
    """Cobra deve detectar auto-colisao (cabeca bate no corpo)."""
    cobra = [
        {"x": 10, "y": 10},  # Cabeca
        {"x": 9, "y": 10},
        {"x": 8, "y": 10},
        {"x": 7, "y": 10},
        {"x": 8, "y": 10},   # Volta para cabeca
    ]
    assert cobra_colidiu_consigo_mesma(cobra)


def test_cobra_nao_colidiu_consigo_mesma():
    """Cobra em linha reta nao deve se auto-colidir."""
    cobra = [
        {"x": 10, "y": 10},
        {"x": 9, "y": 10},
        {"x": 8, "y": 10},
        {"x": 7, "y": 10},
    ]
    assert not cobra_colidiu_consigo_mesma(cobra)


def test_cobra_comeu_comida():
    """Deve detectar quando cobra come a comida."""
    cobra = [{"x": 10, "y": 10}]
    comida = {"x": 10, "y": 10}
    assert cobra_comeu_comida(cobra, comida)


def test_cobra_nao_comeu_comida():
    """Deve detectar quando cobra nao comeu a comida."""
    cobra = [{"x": 10, "y": 10}]
    comida = {"x": 15, "y": 15}
    assert not cobra_comeu_comida(cobra, comida)