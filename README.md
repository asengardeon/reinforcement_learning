FUNDAÇÃO UNIVERSIDADE REGIONAL DE BLUMENAU  
CENTRO DE CIÊNCIAS EXATAS E NATURAIS  
DEPARTAMENTO DE SISTEMAS E COMPUTAÇÃO  
Professor: Ricardo Grunitzki  
Disciplina: Reinforcement Learning  
Aluno: Leandro Vilson Battisti  


## Descrição
Considere o problema de mundo em grade ilustrado a seguir:

![Figura1](/imagens/figura1.jpg)

Neste cenário, um agente (em vermelho) deve percorrer a grade 7x6, encontrar o objeto e
transporta-lo até na base. Essa tarefa deve ser executada na menor quantidade de passos de
tempo possível. O agente n˜ao possui nenhum conhecimento prévio sobre o ambiente, o qual possui
paredes, representadas pelas células pintadas de cinza, as quais ele não transpor. O agente também
não possui conhecimento prévio sobre a localização do objeto.
A localização inicial do agente, disposição das paredes e objeto são sempre fixas, conforme
indicado na ilustração. A cada passo de tempo, o agente pode executar os seguintes movimentos
na grade:

- mover para cima;
- mover para baixo;
- mover para esquerda;
- mover para a direita;
- permanecer na mesma célula

Este cenário apresenta algumas restrições de movimentação:

- O agente pode realizar apenas uma movimentação por passo de tempo.
- Se o agente escolher se mover para uma célula que não está vazia, seja por conta de uma
parede ou objeto, ele não se move, i.e., permanece na mesma célula.
- Qualquer tentativa de locomoção para além da grade, resultará na não movimentação do
agente.
- O objeto só pode ser agarrado pela sua esquerda ou direita.
- Quando o agente é posicionado a direita ou esquerda do objeto, o objeto é agarrado automaticamente.
- Uma vez agarrado o objeto, o agente não pode solta-lo;
- O agente, quando agarrado ao objeto, só consegue se mover para uma nova célula desde que
não haja nenhuma restrição de movimentação para o agente e objeto


O episódio é concluído automaticamente quando o objeto entra na base ou se atingir um nímero
máximo de passos de tempo sem resolver a tarefa. Em ambos os casos, um novo episódio é reiniciado,
com o agente e objeto situados conforme Figura 1.

### Atividade
Implemente uma solução via reinforcement learning para o problema de transporte de objeto e
apresente um relatório endere¸cando os seguintes aspectos da solução:

#### 1. Modelagem do MDP:
(a) Apresente a modelagem de estados considerada, bem como a quantidade de estados
presentes no MDP. Inclua na contagem os estados não-válidos;  
(b) Apresente a modelagem das ações que o agente pode executar;  
(c) Apresente a modelagem da função de recompensa, com as situações em que o agente é
recompensado bem como a magnitude da recompensa. Justifique as suas escolhas.  

#### 2. Configuração dos Experimentos
(a) Apresente os valores de taxa de aprendizagem (alfa) e fator de desconto (gamma) do
algoritmo de aprendizagem Q-Learning;  
(b) Apresente as configurações do horizonte de aprendizagem, que é representado pela quantidade máxima de passos de tempo por episódios, quantidade máxima de episódios, e
política de exploração ao longo do tempo;

#### 3. Resultados Experimentais
(a) Apresente a curva de convergˆencia, representada pela quantidade de passos (timesteps)
necessários para resolver a tarefa ao longo do tempo (episódios).  
(b) Apresente o tempo de processamento necessário para resolver o problema.



## Solução adotada

A solução para o problema foi baseada na no Cliff Walking, disponivel no [GitHub](https://github.com/caburu/gym-cliffwalking/blob/master/gym_cliffwalking/envs/cliffwalking_env.py) usando o algoritmo Q-learning com gym. ALém disto foram utilziado tambe´ms alguns sites de apoio para entendimento de ambiente:
- o [Stable Baselines3 Tutorial - Creating a custom Gym environment](https://colab.research.google.com/github/araffin/rl-tutorial-jnrr19/blob/sb3/5_custom_gym_env.ipynb#scrollTo=PQfLBE28SNDr)


### Modelo MDP
O modelo adotado foram foi de quarto estados, sendo eles CIMA, BAIXO, ESQUEDA e DIREITA. 
Os estados não validos são os de colisões do agente, que são, Sair do mapa, colisão com parede, colisão com objeto e chegar na base sem o objeto. Este estados resetam o cenário ao estado inicial.
Os passos do modelo são que para cada estado valido ele recebe  uam recompensa de -1(menos um), e caso o estado seja invalido a recompensa é de -100. Caso atinda a base com o objetos em mãos a recompensa é de 1(um) e o estado vai para concluido.

hiperparametro|valor
-------------|---------
num_episodes | 200
alpha | 0.3
gamma | 0.9
epsilon | 1.0
decay_epsilon | 0.3

### Resultados

Com esta execução obteves-se os seguites resultados com 300 epocas, com grafico apresentdo na figura2:

Average reward (all episodes): -33.8  
Average reward (last 10 episodes): -6.0  
Time execution: 0:00:00.192502 (192 milisegundos)

![Figura2](/imagens/figura2.jpg)

#Ambiente
Pode ser visualizada a implementação no arquivo do colab disponivel aqui no repositório [Reinforcemente_Learning_carregar_objeto](Reinforcemente_Learning_carregar_objeto.ipynb)  

OU

Baixando o projeto, executando o comando abaixo:

```shell
pipenv install
```  
e em seguida

```shell
python main.py
```

## requisitos para execução local
- Python 3.8
- Pipenv

