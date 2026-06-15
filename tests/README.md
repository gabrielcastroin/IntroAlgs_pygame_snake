# Testes

Esta pasta contém **59 testes automatizados** do projeto do Jogo da Cobra.

## Arquivos

- `test_logica.py`: Testes completos da lógica em `src/funcoes.py`, `src/dados.py` e `src/config.py`.
- `__init__.py`: Pacote Python para testes.

## Categorias de Testes

### 1. Pontuação (3 testes)
- `test_calcular_pontos()` - Soma de pontos
- `test_calcular_pontos_zero()` - Soma com zero
- `test_calcular_pontos_grande()` - Números grandes

### 2. Nível e Velocidade (8 testes)
- `test_calcular_nivel_inicial()` - Nível inicial
- `test_calcular_nivel_100_pontos()` - Cálculo de nível
- `test_calcular_nivel_progressivo()` - Progressão
- `test_calcular_velocidade_*()` - Cálculo e limite de velocidade

### 3. Vidas (5 testes)
- `test_tomar_dano_*()` - Redução de vidas
- `test_jogador_perdeu_*()` - Verificação de derrota
- Sem vidas negativas

### 4. Tempo (5 testes)
- `test_tempo_nao_expirou()` - Tempo disponível
- `test_tempo_expirou_*()` - Expiração
- `test_formatar_tempo()` - Formatação MM:SS

### 5. Movimento (5 testes)
- `test_mover_cobra_*()` - Movimento em 4 direções
- `test_cobra_perde_segmento()` - Comprimento mantido

### 6. Colisão (9 testes)
- `test_cobra_colidiu_com_borda_*()` - Colisões com bordas (4 lados)
- `test_cobra_nao_colidiu_com_borda()` - Posição válida
- `test_cobra_colidiu_consigo_mesma()` - Auto-colisão
- `test_cobra_nao_colidiu_consigo_mesma()` - Sem auto-colisão
- `test_cobra_comeu_comida()` - Detecção de comida
- `test_cobra_nao_comeu_comida()` - Comida distante

### 7. Ranking (5 testes)
- `test_salvar_e_carregar_ranking()` - Persistência
- `test_ranking_ordenado_por_pontos()` - Ordenação
- `test_ranking_top_10()` - Limitação
- `test_obter_melhor_ranking()` - Melhor pontuação
- `test_formatar_ranking()` - Formatação

### 8. Persistência (3 testes)
- `test_salvar_recorde()` - Salvar em arquivo
- `test_carregar_recorde_inexistente()` - Arquivo ausente
- `test_atualizar_recorde()` - Atualização

### 9. Utilidades (2 testes)
- `test_limitar_valor_*()` - Limites de valores
- `test_formatar_ranking_vazio()` - Ranking vazio

**Total: 59 testes** ✅

## Como Executar

### Com pytest (recomendado)
```bash
# Instalar pytest
pip install pytest

# Todos os testes
pytest tests/test_logica.py -v

# Teste específico
pytest tests/test_logica.py::test_calcular_nivel_100_pontos -v

# Com cobertura
pytest tests/ --cov=src

# Output curto
pytest tests/ -q
```

### Teste manual de imports
```bash
python test_imports.py
```

## Resultado Esperado

```
====== 59 passed in 0.24s ======
```

Todos os testes devem passar sem erros.

## Estrutura de Um Teste

```python
def test_exemplo():
    """Descrição clara do que está sendo testado."""
    resultado = funcao(param1, param2)
    assert resultado == valor_esperado
```

## Dependências

- **pytest**: Framework de testes (opcional mas recomendado)
- **pygame**: Instalado em requirements.txt

## Cobertura

Os testes cobrem:
- ✅ Toda lógica de pontuação e nível
- ✅ Sistema completo de vidas
- ✅ Sistema de tempo com formatação
- ✅ Movimento em 4 direções
- ✅ Detecção de colisões
- ✅ Ranking e persistência
- ✅ Formatação e utilitários

## Desenvolvimento

Ao adicionar nova funcionalidade:
```bash
pytest tests/test_logica.py::test_mover_cobra_direita -v
```

## Cobertura de Testes

Para ver cobertura de código:
```bash
pip install pytest-cov
pytest --cov=src tests/
```

## Boas Práticas

- ✅ Crie testes para toda regra de pontuação, colisões e condições de fim de jogo
- ✅ Prefira funções pequenas e testáveis no módulo `src/funcoes.py`
- ✅ Use nomes descritivos para funções de teste
- ✅ Adicione docstrings para descrever o que está sendo testado
- ✅ Teste casos limite (bordas, auto-colisão, posições extremas)
