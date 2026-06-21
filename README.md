# 🐍 Jogo da Cobra - Pygame

Um clássico jogo da cobra implementado em Python com Pygame. Projeto educacional para aprender conceitos de programação como estrutura de dados, controle de fluxo, persistência de dados e detecção de colisões.

## 🎮 Sobre o Jogo

Controle uma cobra que cresce ao comer. Sobreviva a obstáculos dinâmicos, colete power-ups e gerencie sua vida para bater o recorde!

**Características:**
- 🐍 Cobra cresce dinamicamente ao comer
- 🌌 **Cenário Infinito**: Atravessa bordas (estilo Pac-man)
- 🍎 **Alimentos Especiais**: Maçã de Ouro (Speed), Pimenta (Inversão), Cogumelo (Shrink) e Morango (Heal)
- 🧱 **Labirinto Dinâmico**: Obstáculos que aparecem e desaparecem ciclicamente a cada 60 segundos
- ❤️ **Sistema de HP**: 3 corações (6 metades de HP) com sistema de imunidade
- ⏱️ Limite de tempo (5 minutos)
- 📊 Sistema de nível progressivo
- 🏆 Ranking automático (Top 10) e High Scores visual
- 💾 Persistência de recorde
- 🎨 **Visual Moderno**: Fundo em xadrez azul escuro e HUD estilo Adobe Stock

## 📊 Sistemas de Jogo

### Sistema de Pontuação e Itens
- **Maçã Normal**: +10 pontos.
- **Maçã de Ouro**: +30 pontos e aumento de velocidade temporário (5s).
- **Pimenta**: +10 pontos mas inverte os controles (5s).
- **Cogumelo**: +10 pontos e reduz o tamanho da cobra pela metade.
- **Morango**: +20 pontos e recupera 1 coração inteiro (+2 HP).
- **Bônus**: Pontos extras por tempo restante ao vencer (5 pts/segundo).

### Sistema de Fronteiras e Obstáculos
- O campo de jogo é **infinito**: ao ultrapassar qualquer borda, a cobra reaparece no lado oposto.
- **Labirinto**: A cada minuto, um labirinto de obstáculos surge por 30 segundos. Um alerta visual indica quando o labirinto está prestes a aparecer.

### Sistema de Vida e Dano
- O jogador possui **3 corações** (cada um com 2 pontos de HP, total 6).
- Colisões com obstáculos ou com o próprio corpo retiram HP.
- Após sofrer dano, a cobra ganha **imunidade temporária** (piscando na tela).

### Sistema de Tempo
- **5 minutos (300 segundos)** de tempo total
- Tempo restante exibido no HUD
- **Condição de vitória**: Tempo esgotado = VOCÊ VENCEU!
- Alerta visual quando tempo < 30 segundos

### Sistema de Nível
- Nível = (Pontos ÷ 100) + 1
- Nível 1: 0-99 pontos
- Nível 2: 100-199 pontos
- Nível 3: 200-299 pontos
- Máximo nível prático: ∞

### Sistema de Velocidade
- Velocidade base: 10 FPS
- Aumenta 1 FPS por nível
- Máximo: 30 FPS
- Fórmula: `min(FPS_base + (nível - 1), 30)`

### Sistema de Ranking
- **Top 10** jogadores ordenados por pontuação
- Salvo automaticamente em `data/ranking.json`
- Inclui: Nome, Pontos, Tempo de Jogo, Data/Hora
- Exibido após cada jogo (com opção de jogar novamente)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Pygame 2.6+

### Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd IntroAlgs_pygame_snake
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar o Jogo

```bash
python main.py
```

Ou com tratamento de erros melhorado:
```bash
python run_game.py
```

## 🎮 Controles

| Tecla | Ação |
|-------|------|
| ⬅️ **Arrow Left** | Mover esquerda |
| ➡️ **Arrow Right** | Mover direita |
| ⬆️ **Arrow Up** | Mover acima |
| ⬇️ **Arrow Down** | Mover abaixo |
| **SPACE** | Jogar novamente (em Game Over) |
| **ESC** | Sair (em Game Over) |

## 📁 Estrutura do Projeto

```
IntroAlgs_pygame_snake/
├── main.py                 # Ponto de entrada
├── run_game.py             # Runner com tratamento de erros
├── test_imports.py         # Script de teste de imports
├── requirements.txt        # Dependências Python
├── README.md              # Este arquivo
├── src/                   # Código-fonte
│   ├── __init__.py
│   ├── config.py          # Configurações globais
│   ├── funcoes.py         # Lógica do jogo
│   ├── jogo.py            # Loop principal
│   ├── dados.py           # Persistência de dados
│   ├── sprites.py         # Manipulação de sprites
│   ├── pyproject.toml     # Configuração do projeto
│   └── README.md          # Documentação de módulos
├── data/                  # Dados da aplicação
│   ├── recorde.txt        # Melhor pontuação
│   ├── ranking.json       # Ranking top 10
│   └── README.md
├── assets/                # Recursos do jogo
│   ├── imagens/
│   │   └── spritesheet.bmp
│   ├── sons/
│   └── fontes/
├── tests/                 # Testes unitários
│   ├── __init__.py
│   ├── test_logica.py     # Testes da lógica do jogo
│   └── README.md
└── docs/                  # Documentação
    └── proposta.MD
```

## 🏗️ Arquitetura

### Módulos Principais

- **`config.py`** - Constantes globais (800×600, 40×30 células, 10 FPS, cores, caminhos)
- **`funcoes.py`** - Lógica do jogo (movimento, colisões, nível, velocidade, formatação)
- **`jogo.py`** - Loop principal (entrada, atualização, renderização, HUD, ranking)
- **`dados.py`** - Persistência (recorde em TXT, ranking em JSON)
- **`sprites.py`** - Carregamento de spritesheets

### Estrutura da Cobra

A cobra é representada como uma lista de dicionários:
```python
cobra = [
    {"x": 20, "y": 15},  # Cabeça
    {"x": 19, "y": 15},  # Corpo
    {"x": 18, "y": 15},  # Cauda
]
```

### Estrutura de Ranking

Cada entrada do ranking é um dicionário:
```python
{
    "nome": "João",
    "pontos": 520,
    "tempo": 245,
    "data": "2026-06-14T15:30:45"
}
```

### Fluxo Principal

```
Inicializar Pygame
    ↓
Coleta nome do jogador
    ↓
LOOP DE JOGOS:
  1. Inicializa cobra, comida, variáveis
  2. LOOP PRINCIPAL:
     a. Capturar entrada (teclado)
     b. Mover cobra
     c. Verificar colisões
     d. Atualizar nível e velocidade
     e. Verificar tempo
     f. Renderizar HUD e objetos
  3. Game Over? → Salva no ranking
  4. Exibe tela de Game Over
  5. Exibe ranking top 10
  6. Jogar novamente? → volta ao passo 1
    ↓
Finalizar Pygame
```

## 🧪 Testes

### Estrutura de Testes

O projeto inclui testes extensivos em `tests/test_logica.py`:

- **21 testes de pontuação e nível**: Cálculo de pontos, nível, velocidade
- **12 testes de vidas e tempo**: Sistema de dano, perda, formatação
- **8 testes de movimento da cobra**: Movimento em 4 direções
- **7 testes de colisão**: Bordas, auto-colisão, alimento
- **8 testes de ranking**: Salvar, carregar, ordenar, top 10
- **3 testes de persistência**: Recorde, atualização

**Total: 59 testes unitários** 

### Executar Testes

```bash
# Instalar pytest (se ainda não estiver)
pip install pytest

# Rodar todos os testes
pytest tests/

# Rodar com verbose
pytest tests/ -v

# Rodar teste específico
pytest tests/test_logica.py::test_calcular_nivel_100_pontos -v

# Rodar com cobertura
pytest tests/ --cov=src
```

### Exemplos de Testes

```python
# Teste de pontuação
def test_calcular_pontos():
    assert calcular_pontos(10, 5) == 15

# Teste de nível
def test_calcular_nivel_200_pontos():
    assert calcular_nivel(200) == 3

# Teste de velocidade
def test_calcular_velocidade_aumenta():
    vel_1 = calcular_velocidade(1, 10)
    vel_3 = calcular_velocidade(3, 10)
    assert vel_3 > vel_1

# Teste de ranking
def test_ranking_ordenado_por_pontos():
    # Salva 3 entradas em ordem aleatória
    salvar_ranking(temp_arquivo, "Alice", 50, 30)
    salvar_ranking(temp_arquivo, "Bob", 200, 60)
    salvar_ranking(temp_arquivo, "Charlie", 150, 45)
    
    # Carrega e verifica ordenação
    ranking = carregar_ranking(temp_arquivo)
    assert ranking[0]["pontos"] == 200
    assert ranking[1]["pontos"] == 150
    assert ranking[2]["pontos"] == 50
```

## 📊 Exemplo de Gameplay

```
┌─────────────────────────────────────────────────┐
│ Pontos: 120 │ Vidas: 2 │ Tempo: 02:15 │ Nível: 2 │ Tamanho: 8 │
├─────────────────────────────────────────────────┤
│                                                 │
│           🐍🟩🟩🟩                               │
│           🟥                                    │
│                                                 │
│                                    🍎           │
│                                                 │
│                                                 │
│ Jogador: João                                   │
└─────────────────────────────────────────────────┘
```

## 🎯 Roadmap Futuro

- [ ] Diferentes níveis de dificuldade (Fácil, Normal, Difícil)
- [ ] Efeitos sonoros
- [ ] Gráficos melhorados com sprites animados
- [ ] Bonus de tempo aleatórios
- [ ] Modo multiplayer
- [ ] Pausa do jogo
- [ ] Atalhos de teclado (P para pausar, M para mute)
- [ ] Tema escuro/claro configurável
- [ ] Estatísticas detalhadas (mais jogos, média de pontos, etc.)

## 💡 Dicas de Desenvolvimento

### Aumentar Dificuldade
- Reduzir `FPS` em `src/config.py` (ex: 8 ao invés de 10)
- Reduzir `TEMPO_LIMITE` (ex: 180 segundos)
- Reduzir `VIDAS_INICIAIS` (ex: 2 vidas)

### Mudar Cores
Edite `src/config.py` (formato RGB: 0-255):
```python
VERDE = (0, 255, 0)      # Verde brilhante
VERMELHO = (255, 0, 0)   # Vermelho puro
AZUL = (0, 0, 255)       # Azul puro
```

### Adicionar Novos Sprites
Use `src/sprites.py` para carregar e gerenciar spritesheets.

### Extensões Possíveis
- Adicionar `poderes` como escudo, velocidade, comida especial
- Sistema de `achievements`
- `Replay` de melhores jogos
- `Leaderboard` online

## 📚 Conceitos Educacionais

Este projeto demonstra:

| Conceito | Implementação |
|----------|---------------|
| **Estruturas de Dados** | Listas (cobra), Dicionários (configuração, ranking) |
| **Controle de Fluxo** | Loop principal com múltiplas condições |
| **Detecção de Colisões** | Verificação de posições em grid |
| **Persistência de Dados** | TXT (recorde), JSON (ranking) |
| **Modularização** | 5 módulos com responsabilidades claras |
| **Processamento de Eventos** | Entrada de teclado com Pygame |
| **Cálculos Dinâmicos** | Nível, velocidade, pontos, tempo |
| **Testes Unitários** | 59 testes com pytest |
| **HUD (Heads-Up Display)** | Interface dinâmica com informações |
| **Ranking e Persistência** | Sistema de top 10 com JSON |

## 🏆 Recordes Esperados

| Nível | Tempo | Comidas | Pontos |
|-------|-------|--------|--------|
| Nível 1 | 5 min | 5-10 | 50-100 |
| Nível 2 | 5 min | 10-20 | 100-200 |
| Nível 3+ | 5 min | 20+ | 200+ |

## 📝 Licença

Este é um projeto educacional. Sinta-se livre para usar e modificar.

## 👤 Autor

Desenvolvido como projeto final de Introdução a Algoritmos com Pygame.

---

**Divirta-se jogando! 🎮**

### Changelog

#### v1.0.0 (2026-06-14)
- ✅ Sistema completo de vidas (3 vidas)
- ✅ Sistema de tempo limite (5 minutos)
- ✅ Sistema de nível progressivo (100 pontos = 1 nível)
- ✅ Aumento dinâmico de velocidade (até 30 FPS)
- ✅ Ranking automático (Top 10) com JSON
- ✅ HUD com informações de jogo
- ✅ Menu de nome do jogador
- ✅ Telas de Game Over e Ranking
- ✅ 59 testes unitários
- ✅ Documentação completa
