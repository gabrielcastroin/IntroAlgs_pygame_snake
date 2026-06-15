# 🐍 Jogo da Cobra - Guia de Setup

## Pré-requisitos

- Python 3.8+ 
- pip (gerenciador de pacotes Python)
- Virtual Environment (recomendado)

## Instalação

### 1. Clonar ou abrir o repositório

```bash
cd IntroAlgs_pygame_snake
```

### 2. Criar Virtual Environment (Recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

## Executando o Jogo

### Opção 1: Via main.py (Recomendado)

```bash
python main.py
```

### Opção 2: Via run_game.py (Com verificações)

```bash
python run_game.py
```

### Opção 3: Direto com Pygame

```bash
python -m src.jogo
```

## Estrutura do Projeto

```
IntroAlgs_pygame_snake/
├── src/
│   ├── __init__.py
│   ├── config.py           # Configurações centralizadas
│   ├── cobra.py            # Classe Cobra (serpente)
│   ├── utils.py            # Funções utilitárias
│   ├── pontuacao.py        # Gerenciamento de recordes
│   ├── menu.py             # Telas do menu e pausa
│   ├── dados.py            # Persistência (ranking JSON)
│   ├── funcoes.py          # Funções legadas (em refatoração)
│   ├── sprites.py          # Definições de sprites
│   ├── jogo.py             # Loop principal do jogo
│   └── main.py             # (Desuetudo - usar main.py raiz)
├── data/
│   ├── recorde.txt         # Melhor pontuação
│   ├── ranking.json        # Top 5 recordes
│   └── log_pontuacoes.txt  # Log de pontuações
├── tests/
│   └── test_logica.py      # 59 testes unitários
├── assets/
│   ├── imagens/            # Sprites e recursos gráficos
│   ├── sons/               # Efeitos sonoros (futuro)
│   └── fontes/             # Fontes personalizadas (futuro)
├── main.py                 # Ponto de entrada
├── run_game.py             # Runner com verificações
├── requirements.txt        # Dependências
└── README.md              # Documentação principal
```

## Controles do Jogo

**Menu Principal:**
- ⬆️/⬇️ - Navegar entre opções
- ENTER - Selecionar opção

**Durante o Jogo:**
- ⬆️ - Mover para cima
- ⬇️ - Mover para baixo
- ⬅️ - Mover para esquerda
- ➡️ - Mover para direita
- ESC - Pausar jogo / Voltar ao menu

**Game Over:**
- R - Reiniciar partida
- ESC - Sair do jogo

## Funcionários Implementadas

✅ **Sistema de Pontuação**
- 10 pontos por alimento
- Multiplier por tempo bônus (futuro)

✅ **Níveis Dinâmicos**
- A cada 5 alimentos = +1 nível
- Cor da cobra muda por nível (verde → amarelo → vermelho)
- Velocidade aumenta com nível (10-25 FPS)

✅ **Menu Principal**
- Jogar nova partida
- Ver recorde
- Sair do jogo

✅ **Pausa**
- Pausar/Despausar com ESC
- Voltar ao menu

✅ **Ranking**
- Top 5 recordes salvos em JSON
- Nome, pontos, alimentos e timestamp

✅ **Persistência**
- Recorde em TXT
- Ranking em JSON

## Resolvendo Problemas

### Erro: "ModuleNotFoundError: No module named 'pygame'"

**Solução:**
```bash
pip install pygame
```

### Erro: "Externally managed environment" no Linux/WSL

**Solução:**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Jogo rodando muito rápido ou muito lento

**Solução:** Ajustar `FPS_BASE` em `src/config.py`:
```python
FPS_BASE = 10  # Aumentar para mais rápido
```

## Executando Testes

```bash
pytest tests/test_logica.py -v
```

Resultado esperado: **59 testes passando ✓**

## Desenvolvimento

### Adicionando Novas Features

1. Criar módulo em `src/`
2. Importar em `src/config.py` se necessário
3. Adicionar testes em `tests/test_logica.py`
4. Executar `pytest` para validar

### Melhorias Planejadas

- [ ] Sistema de som
- [ ] Níveis com obstáculos
- [ ] Multiplayer
- [ ] Temas personalizados

## Autor

Projeto educacional de Introdução a Algoritmos com Python e Pygame

## Licença

MIT
