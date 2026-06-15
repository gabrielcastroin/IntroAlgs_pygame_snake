# 🎮 Referência Rápida - Jogo da Cobra v1.0.0

## 📊 Novos Sistemas

```
VIDAS                TEMPO              NÍVEL           RANKING
─────────────────    ──────────────────  ────────────    ──────────
❤️ 3 vidas            ⏱️ 5 minutos        📊 Dinâmico      🏆 Top 10
Perde 1 por colisão   Alerta: < 30s      +1 a cada 100   JSON persistente
Game Over: 0 vidas    Bônus ao vencer    Máx 30 FPS      Auto-salvo
Reinício na colisão   Vitória!           Exibição HUD    Mostra após jogo
```

## 🎯 Fluxo de Jogo

```
┌─────────────────────┐
│  TELA DE NOME       │
│ Digite seu nome     │
└────────────┬────────┘
             │
┌────────────▼──────────────┐
│   INICIALIZA JOGO         │
│  - 3 vidas, 5 minutos     │
│  - Cobra no centro        │
│  - Nível 1 (10 FPS)       │
└────────────┬──────────────┘
             │
        ┌────▼────────────────────────────────┐
        │     LOOP PRINCIPAL                  │
        │ • Captura entrada                   │
        │ • Move cobra                        │
        │ • Verifica colisões                 │
        │ • Atualiza tempo/nível/velocidade   │
        │ • Desenha HUD e objetos             │
        └────┬───────────────────┬────────────┘
             │                   │
             │            ┌──────▼──────┐
             │            │ Colisão?    │
             │            ├─ Borda      │
             │            ├─ Auto-col.  │
             │            └─ Comida     │
             │                   │
             │       ┌───────────┴──────────┐
             │       │ Tempo expirou?       │
             │       │ Vidas = 0?           │
             │       └───────────┬──────────┘
             │                   │
             │            ┌──────▼──────────┐
             │            │  GAME OVER      │
             │            │ • Motivo        │
             │            │ • Pontos        │
             │            │ • Tempo jogado  │
             │            └──────┬──────────┘
             │                   │
             │            ┌──────▼──────────┐
             │            │ Salva ranking   │
             │            └──────┬──────────┘
             │                   │
             │            ┌──────▼────────────────┐
             │            │ EXIBE RANKING (Top 10)│
             │            └──────┬────────────────┘
             │                   │
             │         ┌─────────▼────────┐
             │         │ Jogar novamente?  │
             └────────►│ ┌─ SIM: volta ⬆ │
                       │ └─ NÃO: Sair    │
                       └──────────────────┘
```

## 🧪 Exemplos de Testes

```python
# Pontuação
assert calcular_pontos(10, 5) == 15

# Nível (0-99: L1, 100-199: L2, 200-299: L3, ...)
assert calcular_nivel(0) == 1
assert calcular_nivel(100) == 2
assert calcular_nivel(200) == 3

# Velocidade (Base: 10 FPS, +1 por nível, Máx: 30)
assert calcular_velocidade(1, 10) == 10   # L1: 10 FPS
assert calcular_velocidade(5, 10) == 14   # L5: 14 FPS
assert calcular_velocidade(100, 10) == 30 # Máximo

# Vidas
assert tomar_dano(3, 1) == 2      # Perde 1
assert tomar_dano(1, 5) == 0      # Não fica negativo
assert jogador_perdeu(0)           # Perdeu com 0
assert not jogador_perdeu(1)       # Não perdeu com 1

# Tempo
assert not tempo_expirou(10)       # Tempo disponível
assert tempo_expirou(0)            # Expirou
assert formatar_tempo(0) == "00:00"
assert formatar_tempo(60) == "01:00"
assert formatar_tempo(300) == "05:00"
```

## 📁 Arquivos-Chave

| Arquivo | Propósito | Linhas |
|---------|-----------|--------|
| `src/config.py` | Constantes e configurações | ~30 |
| `src/funcoes.py` | Lógica de jogo | ~140 |
| `src/dados.py` | Persistência (TXT, JSON) | ~80 |
| `src/jogo.py` | Loop principal | ~350 |
| `tests/test_logica.py` | 59 testes unitários | ~500 |
| `README.md` | Documentação completa | ~400 |

## 🎮 Controles

| Tecla | Ação |
|-------|------|
| ⬅️ **LEFT** | Move esquerda |
| ➡️ **RIGHT** | Move direita |
| ⬆️ **UP** | Move acima |
| ⬇️ **DOWN** | Move abaixo |
| **SPACE** | Jogar novamente |
| **ESC** | Sair |

## 📊 Exemplo de HUD

```
┌─────────────────────────────────────────┐
│ Pontos: 120 │ Vidas: 2 │ Tempo: 02:15 │ Nível: 2 │ Tamanho: 8 │
├─────────────────────────────────────────┤
│                                         │
│           🐍🟩🟩🟩                        │
│           🟥                           │
│                                         │
│                              🍎        │
│                                         │
└─────────────────────────────────────────┘
```

## 🏆 Exemplo de Ranking

```
TOP 10 RANKING
 1. Alice          -  500 pts (120s) [2026-01-15]
 2. Bob            -  450 pts (110s) [2026-01-14]
 3. Charlie        -  320 pts (95s)  [2026-01-14]
```

## 🔧 Configurações (src/config.py)

```python
# Tela
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 10

# Jogo
VIDAS_INICIAIS = 3
TEMPO_LIMITE = 300  # segundos
PONTOS_POR_COMIDA = 10
TAMANHO_CELULA = 20

# Arquivos
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.json"
```

## 🚀 Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Jogar
python main.py

# Ou com melhor tratamento de erros
python run_game.py

# Testar
pytest tests/ -v

# Verificar imports
python test_imports.py
```

## 📈 Progressão Esperada

| Nível | Pontos | FPS | Dificuldade |
|-------|--------|-----|-------------|
| 1     | 0-99   | 10  | Fácil       |
| 2     | 100-199| 11  | Normal      |
| 3     | 200-299| 12  | Desafiador  |
| 4     | 300-399| 13  | Difícil     |
| 5+    | 400+   | 14+ | Muito Difícil|
| Max   | ∞      | 30  | Extremo     |

## 💾 Estrutura de Dados

### Cobra (Lista de Posições)
```python
cobra = [
    {"x": 20, "y": 15},  # Cabeça
    {"x": 19, "y": 15},  # Corpo
    {"x": 18, "y": 15},  # Cauda
]
```

### Ranking (JSON)
```json
[
  {
    "nome": "João",
    "pontos": 520,
    "tempo": 245,
    "data": "2026-06-14T15:30:45"
  }
]
```

## ✨ Status

- ✅ Sistema de vidas funcional
- ✅ Sistema de tempo com vitória
- ✅ Nível progressivo com aumento de velocidade
- ✅ Ranking top 10 com persistência JSON
- ✅ HUD completo com informações em tempo real
- ✅ 59 testes unitários (100% passando)
- ✅ Documentação completa
- ✅ Múltiplos jogos sem reiniciar programa

---

**Pronto para jogar! 🎮** 

Execute `python main.py` e divirta-se! 🐍
