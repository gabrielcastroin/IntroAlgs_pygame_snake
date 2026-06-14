# 🐍 Jogo da Cobra - Pygame

Um clássico jogo da cobra implementado em Python com Pygame. Projeto educacional para aprender conceitos de programação como estrutura de dados, controle de fluxo e detecção de colisões.

## 🎮 Sobre o Jogo

Controle uma cobra que cresce ao comer comida vermelha. Acumule pontos evitando bater nas bordas da tela ou em si mesma. Simples, mas viciante!

**Características:**
- Cobra cresce dinamicamente ao comer
- Sistema de recorde automático
- Detecção de colisões com bordas e auto-colisão
- Interface limpa e responsiva

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Pygame 2.6+

### Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd IntroAlgs_pygame_template
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
| **ESC** | Sair (na tela de Game Over) |

## 📁 Estrutura do Projeto

```
IntroAlgs_pygame_template/
├── main.py                 # Ponto de entrada
├── run_game.py             # Runner com tratamento de erros
├── requirements.txt        # Dependências Python
├── README.md              # Este arquivo
├── src/                   # Código-fonte
│   ├── __init__.py
│   ├── config.py          # Configurações globais
│   ├── funcoes.py         # Lógica do jogo
│   ├── jogo.py            # Loop principal
│   ├── dados.py           # Persistência de dados
│   ├── sprites.py         # Manipulação de sprites
│   └── README.md          # Documentação de módulos
├── data/                  # Dados da aplicação
│   ├── recorde.txt        # Melhor pontuação
│   └── ranking.txt        # Ranking de jogadores (futuro)
├── assets/                # Recursos do jogo
│   ├── imagens/
│   │   └── spritesheet.bmp
│   ├── sons/
│   └── fontes/
├── tests/                 # Testes unitários
│   └── test_logica.py
└── docs/                  # Documentação
    └── proposta.MD
```

## 📊 Gameplay

**Objetivo:** Acumular a maior pontuação possível

**Pontuação:**
- +10 pontos por cada comida comida

**Game Over:**
- Cobra bate na borda da tela
- Cobra bate em si mesma

**Recorde:**
- Automaticamente salvo em `data/recorde.txt`
- Carregado ao reiniciar o jogo

## 🏗️ Arquitetura

### Módulos Principais

- **`config.py`** - Constantes globais (tela 800×600, 40×30 células)
- **`funcoes.py`** - Lógica do jogo (movimento, colisões)
- **`jogo.py`** - Loop principal (entrada, atualização, renderização)
- **`dados.py`** - Persistência de recorde
- **`sprites.py`** - Carregamento de spritesheets (preparado para futuras expansões)

### Estrutura da Cobra

A cobra é representada como uma lista de células:
```python
cobra = [
    {"x": 20, "y": 15},  # Cabeça
    {"x": 19, "y": 15},  # Corpo
    {"x": 18, "y": 15},  # Cauda
]
```

### Fluxo Principal

```
Inicializar Pygame
    ↓
Criar Cobra e Comida
    ↓
LOOP:
  1. Capturar entrada (teclado)
  2. Mover cobra
  3. Verificar colisões
  4. Atualizar recorde
  5. Renderizar cena
    ↓
Game Over? → Exibir mensagem e aguardar ESC
    ↓
Finalizar Pygame
```

## 🧪 Testes

Execute os testes de lógica:
```bash
python -m pytest tests/
```

Ou teste manualmente o import:
```bash
python test_imports.py
```

## 📚 Conceitos Educacionais

Este projeto demonstra:

- **Estruturas de Dados**: Uso de listas e dicionários para representar a cobra
- **Controle de Fluxo**: Loop principal com múltiplas condições
- **Detecção de Colisões**: Verificação de posições
- **Persistência de Dados**: Salva/carregamento de arquivo
- **Modularização**: Separação de responsabilidades em múltiplos arquivos
- **Eventos**: Processamento de entrada de teclado

## 🎯 Roadmap

- [ ] Diferentes níveis de dificuldade
- [ ] Velocidade progressiva
- [ ] Efeitos sonoros
- [ ] Gráficos melhorados com sprites
- [ ] Ranking de múltiplos jogadores
- [ ] Modo multiplayer
- [ ] Pausa do jogo

## 💡 Dicas

- Para aumentar a dificuldade, reduza `FPS` em `src/config.py`
- Para mudar cores, edite `src/config.py` (RGB: 0-255)
- Para adicionar novos sprites, use `src/sprites.py`

## 📝 Licença

Este é um projeto educacional. Sinta-se livre para usar e modificar.

## 👤 Autor

Desenvolvido como projeto final de Introdução a Algoritmos com Pygame.

---

**Divirta-se jogando! 🎮**
