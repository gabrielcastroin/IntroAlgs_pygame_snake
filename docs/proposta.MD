# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Snake Clássico

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Gabriel Castro Inacio
- Nome 2: Daniel Guerra Costa
- Nome 3: Nathalia Ramalho Abranches de Araujo
- Nome 4: Rafael de Alcantara Aguiar Cruz

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo estilo Snake — o jogador controla uma cobra que cresce ao coletar itens e deve evitar colidir com as paredes ou com o próprio corpo.

## 4. Descrição geral do jogo

Descrição:

> Na tela aparece uma grade retangular representando o campo de jogo. O jogador controla uma cobra formada por segmentos que se move continuamente em uma direção. A cada turno, a cobra avança automaticamente e o jogador pode alterar sua direção usando as setas do teclado. Alimentos aparecem em posições aleatórias na grade; ao coletar um alimento, a cobra cresce um segmento e a pontuação aumenta. O principal desafio é evitar que a cabeça da cobra colida com as bordas da tela ou com o próprio corpo. Com o tempo, a velocidade de movimentação da cobra aumenta progressivamente, tornando o jogo mais difícil.

## 5. Objetivo do jogador

Objetivo:

> Coletar o maior número possível de alimentos sem colidir com as paredes ou com o próprio corpo da cobra, acumulando a maior pontuação possível e, se possível, superando o recorde salvo em arquivo.

## 6. Regras principais

Regras do grupo:

- Regra 1: A cobra se move automaticamente; bater nas bordas faz a cobra reaparecer no lado oposto (Cenário Infinito).
- Regra 2: O jogador pode alterar a direção (exceto inversão 180°), a menos que sob efeito de "Pimenta" (controles invertidos).
- Regra 3: Alimentos especiais dão bônus: Maçã de Ouro (+pontos/velocidade), Pimenta (inversão), Cogumelo (reduz tamanho).
- Regra 4: A partida termina apenas se as vidas acabarem (auto-colisão ou tempo expirado).
- Regra 5: Velocidade aumenta com o nível e pode ser temporariamente boostada por itens.

## 7. Condição de vitória

Condição de vitória:

> Sobreviver até o tempo esgotar (5 minutos) ou superar o recorde visual na tela de High Scores.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> Perda de todas as vidas (colisão com o próprio corpo) ou encerramento manual.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

Descrição:

> Cobra com 7 variações de cores dinâmicas baseadas no nível e HUD com status de efeitos ativos.

### Obstáculos, inimigos ou desafios

Descrição:

> O próprio corpo da cobra é o maior desafio, agravado pela inversão de controles e aumentos súbitos de velocidade.

### Itens, alvos ou objetos de interação

Descrição:

> 4 tipos de itens: Normal (Vermelho), Ouro (Amarelo), Pimenta (Vermelho Claro) e Cogumelo (Roxo).

### Pontuação, vidas, tempo ou progresso

Descrição:

> O jogo utiliza um sistema de pontuação baseado na quantidade de alimentos coletados (10 pontos por item). A pontuação atual é exibida na tela durante a partida. O recorde máximo é lido de um arquivo ao iniciar e atualizado ao final da partida, caso seja superado. Não há sistema de vidas — uma única colisão encerra o jogo.

## 10. Controles previstos

Controles do grupo:

- Seta para cima: mover a cobra para cima
- Seta para baixo: mover a cobra para baixo
- Seta para esquerda: mover a cobra para a esquerda
- Seta para direita: mover a cobra para a direita
- ESC: pausar o jogo ou retornar ao menu principal
- R (na tela de game over): reiniciar a partida

## 11. Organização inicial do código

Organização planejada:

- `main.py`: ponto de entrada do jogo; inicializa o Pygame e chama o loop principal;
- `src/jogo.py`: contém o loop principal do jogo, controle de eventos e atualização de estado;
- `src/cobra.py`: define a estrutura e o comportamento da cobra (movimentação, crescimento, colisão);
- `src/config.py`: armazena constantes globais como tamanho da tela, tamanho da célula da grade, cores e velocidade inicial;
- `src/pontuacao.py`: funções de leitura e escrita do recorde em arquivo;
- `src/utils.py`: funções auxiliares, como geração de posição aleatória para o alimento e verificação de colisões;
- `tests/test_logica.py`: testes unitários para as funções de lógica do jogo.

## 12. Recursos externos previstos

Recursos previstos:

> O jogo será desenvolvido utilizando apenas primitivas gráficas do Pygame (retângulos, textos e cores), sem imagens externas ou sprites. Caso haja tempo disponível, poderão ser adicionados sons simples obtidos de bancos de áudio gratuitos (ex.: freesound.org) e uma fonte personalizada livre de direitos. Tutorial do Pygame será usado apenas como referência de documentação oficial.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Implementar corretamente a lógica de movimentação da cobra, garantindo que o corpo siga a cabeça segmento a segmento sem bugs visuais.
- Dificuldade 2: Tratar adequadamente a colisão da cabeça com o próprio corpo, especialmente em cobras longas.
- Dificuldade 3: Organizar o código em módulos de forma coesa e garantir que os testes cubram as principais funções de lógica sem depender do Pygame.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá: uma cobra controlável pelas setas do teclado, movimentação automática com velocidade crescente, geração de alimentos em posições aleatórias, sistema de pontuação exibido na tela, leitura e escrita do recorde em arquivo, detecção de colisão com paredes e com o próprio corpo, e tela de game over com opção de reiniciar.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Tela inicial com menu (Jogar, Recordes, Sair).
- Melhoria 2: Ranking dos 5 maiores recordes salvos em arquivo com nome do jogador.
- Melhoria 3: Efeitos sonoros para coleta de alimento, colisão e início de jogo.
- Melhoria 4: Aumento visual de dificuldade com mudança de cor da cobra conforme o nível.
- Melhoria 5: Tela de pausa ativada pela tecla ESC.
