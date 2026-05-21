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

## Licença

Este projeto está licenciado sob a licença MIT.
