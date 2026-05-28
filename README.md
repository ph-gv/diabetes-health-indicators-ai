# IA Aplicada à Saúde: Predição de Diabetes Tipo 2
Protótipo de Machine Learning para estimativa de risco de Diabetes Tipo 2 em adultos, com base em dados clínicos, demográficos e comportamentais.

A pergunta central do projeto: "É possível predizer o risco de Diabetes Tipo 2 em adultos a partir de indicadores clínicos e comportamentais e quais fatores têm maior peso nessa predição?"

## Dataset
CDC Diabetes Health Indicators, disponível no Kaggle. Gerado a partir de uma pesquisa real de saúde do governo americano com mais de 250.000 registros. As variáveis cobrem aspectos clínicos (IMC, hipertensão, colesterol), comportamentais (atividade física, tabagismo, alimentação), demográficos (idade, renda, escolaridade) e de saúde geral (mobilidade, histórico cardíaco, AVC).

## Como executar
**1. Preparar o ambiente**
Clone o repositório e instale as bibliotecas necessárias:
```
* git clone https://github.com/ph-gv/diabetes-health-indicators-ai.git
* cd diabetes-health-indicators-ai
* pip install -r requirements.txt
```

**1.2 Verificar se a pasta notebooks existe**
No terminal, rode dir. Tem que aparecer algo tipo:
```
* notebooks
* src
* requirements.txt
* README.md
```

**1.3 Entrar na pasta notebooks**
```
* cd notebooks
* dir
```
(Agora precisa aparecer: modelo_diabetes.pkl)

**1.4 Se o arquivo NÃO aparecer**
Isso é esperado - ele está no .gitignore e não sobe com o repositório. Volte para a raiz e rode o notebook de treinamento:

```
* cd ..
* python diabetes_model.ipynb
```
Depois feche o terminal e rode novamente:
```
* streamlit run src/app.py
```

## Etapas do desenvolvimento
**Etapa 1 — Planejamento:** definição do tema, escolha do dataset e estruturação do repositório.
**Etapa 2 — Análise Exploratória:** investigação dos dados. Dataset desbalanceado; IMC, pressão alta e colesterol são os maiores fatores de correlação com a doença.
**Etapa 3 — Modelagem e Interface:** treinamento de Regressão Logística e Random Forest. Interface desenvolvida com Streamlit.
**Etapa 4 — Avaliação e Ética:** métricas, análise de overfitting e reflexão sobre uso responsável da solução.

## Reflexão ética
A IA aqui é um apoio à decisão, não um diagnóstico. O modelo foi treinado com dados americanos, validação com dados da população brasileira é necessária para garantir equidade. Dados clínicos são sensíveis e exigem proteção rigorosa. Quem decide é o profissional de saúde.

## Tecnologias
Python 3 · Scikit-learn · Pandas · NumPy · Seaborn · Matplotlib · Streamlit · Licença MIT
