# IA Aplicada à Saúde: Predição de Diabetes Tipo 2

Projeto com foco no desenvolvimento de um protótipo para prevenção de doenças.

## Objetivo

Desenvolver um modelo de Machine Learning capaz de estimar o risco de Diabetes Tipo 2 a partir de indicadores clínicos, demográficos e comportamentais.

## Tema

**Diabetes Tipo 2**

## Pergunta de pesquisa

**É possível predizer o risco de Diabetes Tipo 2 em adultos a partir de indicadores clínicos e comportamentais, e quais fatores têm maior peso nessa predição?**

## Dataset

O dataset principal utilizado no treinamento do modelo será proveniente do **Kaggle**, por oferecer volume suficiente de dados para treinamento intensivo e melhor adequação ao processo de Machine Learning.

Como complemento, serão utilizados dados do **DATASUS / OpenDataSUS** para contextualização epidemiológica e reforço da relevância social do estudo no cenário brasileiro.

### Dataset principal

* **CDC Diabetes Health Indicators**
* Fonte: Kaggle
* Contém registros reais da pesquisa BRFSS
* Variável-alvo binária já definida: presença ou ausência de diabetes

### Dataset complementar

* **DATASUS / OpenDataSUS**
* Uso contextual e analítico
* Apoio na discussão sobre relevância social e saúde pública no Brasil

## Variáveis consideradas

### Variável-alvo

* `Diabetes_binary` — 0: não diabético, 1: diabético

### Variáveis clínicas

* `BMI` — Índice de Massa Corporal
* `HighBP` — Hipertensão arterial
* `HighChol` — Colesterol alto
* `GenHlth` — Saúde geral autorrelatada

### Variáveis comportamentais

* `PhysActivity` — Atividade física recente
* `Smoker` — Tabagismo
* `HvyAlcoholConsump` — Consumo pesado de álcool
* `Fruits` / `Veggies` — Consumo de frutas e vegetais

### Variáveis demográficas

* `Age` — Faixa etária
* `Sex` — Sexo biológico
* `Education` — Escolaridade
* `Income` — Renda

### Variáveis de saúde

* `MentHlth` — Dias com saúde mental ruim
* `PhysHlth` — Dias com saúde física ruim
* `DiffWalk` — Dificuldade de locomoção
* `HeartDiseaseorAttack` — Doença cardíaca
* `Stroke` — AVC prévio

## Tecnologias previstas

* Python
* pandas
* numpy
* scikit-learn
* matplotlib / seaborn

## Escopo do repositório

Este repositório contém a documentação inicial do projeto, servindo como base para a disciplina e para a organização do desenvolvimento.

## Etapa 2 - EDA/Análise exploratória
## Explorando o dataset CDC, tratando valores faltantes, visualizando distribuições com pandas/seaborn.

Etapa 2 — Análise Exploratória de Dados (EDA)

A EDA foi realizada sobre o dataset CDC Diabetes Health Indicators com o objetivo de entender a estrutura dos dados, identificar padrões e levantar hipóteses para a etapa de modelagem.

O que foi feito:

Carga e inspeção inicial — shape, tipos de dados e estatísticas descritivas básicas
Verificação de valores faltantes — dataset confirmado como completo (sem nulos)
Análise de balanceamento — identificação da proporção diabético/não diabético; o dataset é desbalanceado, o que será tratado na Etapa 3
Distribuições — histogramas de BMI, faixa etária, saúde geral e outras variáveis contínuas/ordinais
Variáveis binárias — comparação do percentual de hipertensão, colesterol alto e outros fatores entre os dois grupos
BMI por grupo — boxplot comparando distribuição de IMC entre diabéticos e não diabéticos
Análise de correlações — ranking das variáveis com maior associação à variável-alvo
Heatmap de correlações — visão completa das correlações entre todas as variáveis
Resumo automático — impressão das principais conclusões no console ao final da execução

Principais achados:

O dataset não possui valores faltantes, dispensando etapas de imputação
O dataset é desbalanceado: a classe não diabética é majoritária — estratégias como SMOTE ou ajuste de pesos serão consideradas na modelagem
BMI, HighBP, GenHlth e HighChol apresentam as maiores correlações com a variável-alvo
Diabéticos tendem a concentrar valores mais altos de BMI e pior percepção de saúde geral


## Licença

Este projeto está licenciado sob a licença MIT.
