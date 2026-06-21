# Código-fonte (`src`)

Esta pasta contém os módulos principais do **Jogo da Cobra**.

## 🐍 Sobre o Jogo

O Jogo da Cobra é um clássico onde você controla uma cobra que cresce ao comer comida. O objetivo é acumular pontos sem bater nas bordas da tela ou em si mesma.

**Características:**
- Tela: 800×600 pixels (40×30 células)
- Velocidade: 10 FPS base + progressão e buffs
- Cenário: Infinito (atravessa bordas)
- Itens: 4 tipos de alimentos (Normal, Ouro, Pimenta, Cogumelo)
- Cobra inicial: 3 segmentos
- Sistema de recorde: visual e persistente

## Arquivos

### `jogo.py` - Loop Principal
Implementa o loop principal do jogo:
- Inicialização da cobra (lista de células)
- Processamento de entrada (suporta inversão de controles)
- Movimentação (com travessia de bordas) e detecção de colisões
- Lógica de Timers para Power-ups e Debuffs
- Renderização (cobra dinâmica, HUD com efeitos, 4 tipos de comida)
- Telas de Menu, Pausa e Game Over

### `config.py` - Configurações Globais
Constantes centralizadas:
- **Dimensões**: `LARGURA_TELA=800`, `ALTURA_TELA=600`
- **Gameplay**: `FPS=10`, `TAMANHO_CELULA=20`
- **Cores**: `VERDE` (cobra), `VERMELHO` (comida), `PRETO` (fundo)
- **Persistência**: `CAMINHO_RECORDE` (arquivo de dados)

### `funcoes.py` - Lógica do Jogo
Funções auxiliares divididas em duas seções:

**Funções Genéricas:**
- `calcular_pontos()` - Soma pontos
- `limitar_valor()` - Mantém valor em intervalo
- `verificar_colisao()` - Colisão entre retângulos

**Funções da Cobra:**
- `mover_cobra(cobra, direcao)` - Move cobra na direção especificada
- `cobra_perde_segmento(cobra)` - Remove último segmento
- `cobra_colidiu_com_borda()` - Detecta saída da tela
- `cobra_colidiu_consigo_mesma()` - Detecta auto-colisão
- `cobra_comeu_comida()` - Verifica captura de comida
- `gerar_comida_aleatoria()` - Cria nova comida em posição segura

### `dados.py` - Persistência
Sistema de salva/carregamento:
- `salvar_recorde(caminho, pontuacao)` - Escreve recorde em arquivo
- `carregar_recorde(caminho)` - Lê recorde anterior (ou 0 se novo)

### `sprites.py` - Manipulação de Sprites
Funções para carregar e processar spritesheets (não usado no Jogo da Cobra atual, mas disponível para expansões futuras).

### `__init__.py` - Package Python
Arquivo vazio que torna `src/` um pacote Python importável.

## 🎮 Controles

| Tecla | Ação |
|-------|------|
| ⬅️ Arrow Left | Mover esquerda |
| ➡️ Arrow Right | Mover direita |
| ⬆️ Arrow Up | Mover acima |
| ⬇️ Arrow Down | Mover abaixo |
| ESC | Sair (na tela de Game Over) |

## 📊 Estrutura de Dados

**Cobra:**
```python
cobra = [
    {"x": 20, "y": 15},  # Cabeça
    {"x": 19, "y": 15},  # Corpo
    {"x": 18, "y": 15},  # Cauda
]
```

**Comida:**
```python
comida = {"x": 10, "y": 8}
```

## 🔄 Fluxo do Jogo

1. Inicializa pygame e cria tela
2. Coloca cobra no meio da tela
3. Gera primeira comida
4. **Loop Principal:**
   - Processa entrada (teclado)
   - Move cobra (mantendo histórico de direção)
   - Verifica colisão com comida → cresce e novo alimento
   - Verifica colisão com borda → Game Over
   - Verifica auto-colisão → Game Over
   - Atualiza recorde se necessário
   - Renderiza cena
5. Ao Game Over, exibe mensagem (ESC para sair)
6. Finaliza pygame

## 💡 Dica de Evolução

Quando o projeto crescer:
- **Mantenha módulos pequenos**: cada responsabilidade em seu arquivo
- **Adicione novos recursos**: diferentes fases, velocidade progressiva, inimigos
- **Use sprites**: integre gráficos via `sprites.py`
- **Expandir dados**: ranking de múltiplos jogadores em `dados.py`
