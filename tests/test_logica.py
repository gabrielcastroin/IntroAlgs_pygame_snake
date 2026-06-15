import json
import os
import tempfile
from src.funcoes import (
    calcular_pontos,
    calcular_nivel,
    calcular_velocidade,
    tomar_dano,
    jogador_perdeu,
    tempo_expirou,
    formatar_tempo,
    limitar_valor,
    mover_cobra,
    cobra_perde_segmento,
    cobra_colidiu_com_borda,
    cobra_colidiu_consigo_mesma,
    cobra_comeu_comida,
)
from src.dados import (
    salvar_ranking,
    carregar_ranking,
    formatar_ranking,
    obter_melhor_ranking,
    salvar_recorde,
    carregar_recorde,
)
from src.config import LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA


# ===== TESTES DE PONTUACAO =====

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_zero():
    """Deve funcionar com pontos zerados."""
    assert calcular_pontos(0, 10) == 10


def test_calcular_pontos_grande():
    """Deve funcionar com números grandes."""
    assert calcular_pontos(1000, 500) == 1500


# ===== TESTES DE NIVEL E VELOCIDADE =====

def test_calcular_nivel_inicial():
    """Nível 1 com 0 pontos."""
    assert calcular_nivel(0) == 1


def test_calcular_nivel_100_pontos():
    """Nível 2 com 100 pontos."""
    assert calcular_nivel(100) == 2


def test_calcular_nivel_200_pontos():
    """Nível 3 com 200 pontos."""
    assert calcular_nivel(200) == 3


def test_calcular_nivel_progressivo():
    """Nível aumenta a cada 100 pontos."""
    assert calcular_nivel(50) == 1
    assert calcular_nivel(100) == 2
    assert calcular_nivel(150) == 2
    assert calcular_nivel(300) == 4


def test_calcular_velocidade_nivel_1():
    """Velocidade base no nível 1."""
    assert calcular_velocidade(1, 10) == 10


def test_calcular_velocidade_aumenta():
    """Velocidade aumenta com o nível."""
    vel_nivel_1 = calcular_velocidade(1, 10)
    vel_nivel_3 = calcular_velocidade(3, 10)
    assert vel_nivel_3 > vel_nivel_1


def test_calcular_velocidade_maxima():
    """Velocidade máxima é 30 FPS."""
    assert calcular_velocidade(100, 10) == 30


# ===== TESTES DE VIDAS =====

def test_tomar_dano_basico():
    """Reduz vidas corretamente."""
    assert tomar_dano(3, 1) == 2


def test_tomar_dano_multiplo():
    """Reduz múltiplos danos."""
    assert tomar_dano(5, 3) == 2


def test_tomar_dano_sem_negativo():
    """Vidas não ficam negativas."""
    assert tomar_dano(1, 5) == 0


def test_jogador_perdeu_vidas_zero():
    """Jogador perdeu com 0 vidas."""
    assert jogador_perdeu(0)


def test_jogador_nao_perdeu():
    """Jogador não perdeu com vidas restantes."""
    assert not jogador_perdeu(1)
    assert not jogador_perdeu(3)


# ===== TESTES DE TEMPO =====

def test_tempo_nao_expirou():
    """Tempo não expirou com tempo restante."""
    assert not tempo_expirou(10)
    assert not tempo_expirou(1)


def test_tempo_expirou_zero():
    """Tempo expirou com 0 segundos."""
    assert tempo_expirou(0)


def test_tempo_expirou_negativo():
    """Tempo expirou com tempo negativo."""
    assert tempo_expirou(-5)


def test_formatar_tempo():
    """Formata tempo corretamente em MM:SS."""
    assert formatar_tempo(0) == "00:00"
    assert formatar_tempo(60) == "01:00"
    assert formatar_tempo(65) == "01:05"
    assert formatar_tempo(125) == "02:05"
    assert formatar_tempo(300) == "05:00"


# ===== TESTES UTILITARIOS =====

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
        {"x": 10, "y": 10},   # Volta para cabeca (auto-colisao)
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


# ===== TESTES DE RANKING =====

def test_salvar_e_carregar_ranking():
    """Deve salvar e carregar ranking corretamente."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_arquivo = f.name

    try:
        # Limpa arquivo
        ranking_inicial = carregar_ranking(temp_arquivo)
        assert ranking_inicial == []

        # Salva uma entrada
        salvar_ranking(temp_arquivo, "João", 100, 50)
        ranking = carregar_ranking(temp_arquivo)
        
        assert len(ranking) == 1
        assert ranking[0]["nome"] == "João"
        assert ranking[0]["pontos"] == 100
        assert ranking[0]["tempo"] == 50

    finally:
        if os.path.exists(temp_arquivo):
            os.remove(temp_arquivo)


def test_ranking_ordenado_por_pontos():
    """Ranking deve estar ordenado por pontos decrescentes."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_arquivo = f.name

    try:
        salvar_ranking(temp_arquivo, "Alice", 50, 30)
        salvar_ranking(temp_arquivo, "Bob", 200, 60)
        salvar_ranking(temp_arquivo, "Charlie", 150, 45)
        
        ranking = carregar_ranking(temp_arquivo)
        
        assert ranking[0]["pontos"] == 200
        assert ranking[1]["pontos"] == 150
        assert ranking[2]["pontos"] == 50

    finally:
        if os.path.exists(temp_arquivo):
            os.remove(temp_arquivo)


def test_ranking_top_10():
    """Ranking deve manter apenas top 10."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_arquivo = f.name

    try:
        # Salva 15 entradas
        for i in range(15):
            salvar_ranking(temp_arquivo, f"Jogador{i}", i * 100, 30)
        
        ranking = carregar_ranking(temp_arquivo)
        assert len(ranking) == 10

    finally:
        if os.path.exists(temp_arquivo):
            os.remove(temp_arquivo)


def test_obter_melhor_ranking():
    """Deve retornar melhor pontuação do ranking."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_arquivo = f.name

    try:
        salvar_ranking(temp_arquivo, "Alice", 100, 30)
        salvar_ranking(temp_arquivo, "Bob", 200, 60)
        
        ranking = carregar_ranking(temp_arquivo)
        melhor = obter_melhor_ranking(ranking)
        
        assert melhor == 200

    finally:
        if os.path.exists(temp_arquivo):
            os.remove(temp_arquivo)


def test_formatar_ranking():
    """Deve formatar ranking corretamente."""
    ranking = [
        {"nome": "Alice", "pontos": 200, "tempo": 60, "data": "2026-01-15T10:30:00"},
        {"nome": "Bob", "pontos": 150, "tempo": 45, "data": "2026-01-14T15:20:00"},
    ]
    
    formatado = formatar_ranking(ranking)
    
    assert "Alice" in formatado
    assert "200" in formatado
    assert "Bob" in formatado
    assert "150" in formatado


def test_formatar_ranking_vazio():
    """Deve formatar ranking vazio."""
    formatado = formatar_ranking([])
    assert "Nenhuma entrada" in formatado


# ===== TESTES DE PERSISTENCIA =====

def test_salvar_recorde():
    """Deve salvar recorde em arquivo."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_arquivo = f.name

    try:
        salvar_recorde(temp_arquivo, 500)
        recorde = carregar_recorde(temp_arquivo)
        assert recorde == 500

    finally:
        if os.path.exists(temp_arquivo):
            os.remove(temp_arquivo)


def test_carregar_recorde_inexistente():
    """Deve retornar 0 se arquivo não existir."""
    recorde = carregar_recorde("arquivo_inexistente_xyz.txt")
    assert recorde == 0


def test_atualizar_recorde():
    """Deve atualizar recorde se novo valor for maior."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_arquivo = f.name

    try:
        salvar_recorde(temp_arquivo, 300)
        salvar_recorde(temp_arquivo, 500)
        recorde = carregar_recorde(temp_arquivo)
        assert recorde == 500

    finally:
        if os.path.exists(temp_arquivo):
            os.remove(temp_arquivo)