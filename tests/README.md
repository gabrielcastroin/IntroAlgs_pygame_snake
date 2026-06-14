# Testes

Esta pasta contém testes automatizados do projeto do Jogo da Cobra.

## Arquivos

- `test_logica.py`: valida funções pures de lógica em `src/funcoes.py`.

## Testes Implementados

### Testes Básicos
- `test_calcular_pontos()` - Soma de pontos
- `test_calcular_pontos_zero()` - Soma com zero
- `test_limitar_valor_*()` - Limites de valores

### Testes da Cobra
- `test_mover_cobra_*()` - Movimento em 4 direções
- `test_cobra_perde_segmento()` - Comprimento mantido
- `test_cobra_colidiu_com_borda_*()` - Colisões com bordas (4 lados)
- `test_cobra_nao_colidiu_com_borda()` - Posição válida
- `test_cobra_colidiu_consigo_mesma()` - Auto-colisão
- `test_cobra_nao_colidiu_consigo_mesma()` - Sem auto-colisão
- `test_cobra_comeu_comida()` - Detecção de comida
- `test_cobra_nao_comeu_comida()` - Comida distante

**Total: 20 testes**

## Como Executar

Instale pytest (se ainda não instalou):
```bash
pip install pytest
```

Execute todos os testes:
```bash
pytest
```

Execute com verbosidade:
```bash
pytest -v
```

Execute um arquivo específico:
```bash
pytest tests/test_logica.py
```

Execute um teste específico:
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
