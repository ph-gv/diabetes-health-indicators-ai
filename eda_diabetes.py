
#ETAPA 2 — EDA: Predição de Diabetes Tipo 2
#Dataset: CDC Diabetes Health Indicators (Kaggle)

# pandas-usado pra trabalhar com tabelas/datasets
import pandas as pd
# numpy-usado pra operações matematicas
import numpy as np
# matplotlib-usado pra criar graficos
import matplotlib.pyplot as plt
# seaborn-usado pra graficos mais bonitos e estatisticos
import seaborn as sns


#CONFIGURAÇÕES VISUAIS
#define estilo padrao dos graficos
sns.set_theme(style="whitegrid", palette="muted")

#tamanho padrao das figuras
plt.rcParams["figure.figsize"] = (10, 5)


#CARREGANDO O DATASET

#le o csv e transforma em dataframe
df = pd.read_csv("diabetes_binary_health_indicators_BRFSS2015.csv")


#EXPLORANDO O DATASET CDC
#mostra quantidade de linhas e colunas
print("Shape:", df.shape)

#mostra as primeiras linhas do dataset
print("\n=== PRIMEIRAS LINHAS ===")
print(df.head())

#mostra os tipos das colunas
print("\n=== TIPOS DE DADOS ===")
print(df.dtypes)

#mostra estatisticas gerais
#media, desvio padrao, minimo, maximo etc
print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(df.describe())


#TRATAMENTO DE VALORES FALTANTES
print("\n=== VALORES FALTANTES ===")

#verifica quantos valores nulos existem em cada coluna
missing = df.isnull().sum()

#se existir valor faltante
if missing.sum() > 0:
    #mostra apenas colunas com valores faltantes
    print(missing[missing > 0])

else:
    #dataset veio limpo
    print("Nenhum valor faltante!")

#Obs:
#aqui estamos TRATANDO valores faltantes
#nesse caso não precisou preencher/remover nada
#porque o dataset ja veio sem valores nulos

#DISTRIBUIÇAO DA VARIAVEL-ALVO
#conta quantos diabeticos e não diabeticos existem
contagem = df["Diabetes_binary"].value_counts()

print("\n=== DISTRIBUIÇÃO DA VARIÁVEL-ALVO ===")
print(contagem)

#calcula porcentagem de cada grupo
print(
    f"\nProporção: "
    f"{contagem[0.0] / len(df):.1%} não diabético | "
    f"{contagem[1.0] / len(df):.1%} diabético"
)

#VISUALIZAÇÃO DE DISTRIBUIÇOES COM PANDAS
#cria grafico de barras
fig, ax = plt.subplots()

contagem.plot(
    kind="bar",
    ax=ax,
    color=["#5DCAA5", "#D85A30"],
    edgecolor="none",
    width=0.5
)

#configuraçoes do grafico
ax.set_title("Distribuição da variável-alvo (Diabetes_binary)")
ax.set_xlabel("")
ax.set_xticklabels(["Não diabético (0)", "Diabético (1)"], rotation=0)
ax.set_ylabel("Quantidade")

#organiza layout
plt.tight_layout()

#salva grafico
plt.savefig("fig1_balanceamento.png", dpi=150)

#mostra grafico
plt.show()

#Obs:
#aqui estamos VISUALIZANDO DISTRIBUIÇOES
#usando grafico de barras do pandas

#DISTRIBUIÇÃO DAS VARIAVEIS NUMÉRICAS
#lista das variaveis numéricas
variaveis_num = [
    "BMI",
    "GenHlth",
    "MentHlth",
    "PhysHlth",
    "Age"
]

#cria varios graficos lado a lado
fig, axes = plt.subplots(1, len(variaveis_num), figsize=(18, 4))

#percorre cada coluna
for i, col in enumerate(variaveis_num):

    #VISUALIZAÇAO DE DISTRIBUIÇÕES COM SEABORN
    #cria histogramas
    #um grafico usado pra mostrar a distribuiçao dos valores de uma variavel numérica - “Os valores estao mais concentrados onde?”
    sns.histplot(
        df[col],
        ax=axes[i],
        kde=True,
        color="#378ADD",
        bins=20
    )

    #titulo de cada grafico
    axes[i].set_title(col)

    #remove label eixo x
    axes[i].set_xlabel("")

#titulo geral
plt.suptitle("Distribuição das variáveis numéricas", y=1.02)

#organiza layout
plt.tight_layout()

#salva imagem
plt.savefig("fig2_distribuicoes.png", dpi=150)

#mostra
plt.show()

#Obs:
#aqui estamos analisando:
#distribuição
#concentração
#dispersão
#possiveis outliers (dados, valores ou comportamentos que se desviam drasticamente de um padrão esperado)

#VARIAVEIS BINARIAS
variaveis_bin = [
    "HighBP",
    "HighChol",
    "PhysActivity",
    "Smoker",
    "HvyAlcoholConsump",
    "HeartDiseaseorAttack",
    "Stroke",
    "DiffWalk"
]

#dicionario vazio
proporcoes = {}

#percorre colunas binarias
for col in variaveis_bin:

    #pega media de diabeticos
    #apenas onde a variavel vale 1
    p = df[df[col] == 1]["Diabetes_binary"].mean()

    #transforma em porcentagem
    proporcoes[col] = round(p * 100, 1)

#transforma em dataframe
prop_df = pd.DataFrame.from_dict(
    proporcoes,
    orient="index",
    columns=["% diabéticos"]
)

#ordena do menor pro maior
prop_df = prop_df.sort_values(
    "% diabéticos",
    ascending=True
)

#cria grafico
fig, ax = plt.subplots(figsize=(8, 5))

prop_df.plot(
    kind="barh",
    ax=ax,
    color="#534AB7",
    edgecolor="none",
    legend=False
)

#titulo
ax.set_title("% de diabéticos entre quem tem cada condição")

#eixo x
ax.set_xlabel("% diabéticos")

#organiza layout
plt.tight_layout()

#salva grafico
plt.savefig("fig3_variaveis_binarias.png", dpi=150)

#mostra grafico
plt.show()

#BOXPLOT BMI - grafico de caixa

fig, ax = plt.subplots()

#VISUALIZAÇÃO DE DISTRIBUIÇaO COM SEABORN
sns.boxplot(
    data=df,
    x="Diabetes_binary",
    y="BMI",
    hue="Diabetes_binary",
    palette={
        0.0: "#5DCAA5",
        1.0: "#D85A30"
    },
    legend=False,
    ax=ax
)

#muda labels
ax.set_xticklabels([
    "Não diabético",
    "Diabético"
])

#titulo
ax.set_title("Distribuição do IMC por grupo")

#organiza layout
plt.tight_layout()

#salva imagem
plt.savefig("fig4_bmi_grupos.png", dpi=150)

#mostra grafico
plt.show()

#Obs:
#boxplot ajuda a visualizar:
#mediana
#quartis
#dispersão
#outliers

#CORRELAÇÃO COM A VARIAVEL-ALVO
#calcula correlaçAo
correlacoes = (
    df.corr()["Diabetes_binary"]
    .drop("Diabetes_binary")
    .sort_values(ascending=False)
)

print("\n=== TOP 10 VARIÁVEIS MAIS CORRELACIONADAS ===")
print(correlacoes.head(10).to_string())

#cria grAfico
fig, ax = plt.subplots(figsize=(8, 6))

correlacoes.head(10).plot(
    kind="barh",
    ax=ax,
    color="#185FA5",
    edgecolor="none"
)

#titulo
ax.set_title("Correlação com Diabetes_binary (Top 10)")

#eixo x
ax.set_xlabel("Correlação de Pearson")

#organiza layout
plt.tight_layout()

#salva imagem
plt.savefig("fig5_correlacoes.png", dpi=150)

#mostra
plt.show()

#Obs:
#aqui estamos vendo quais variaveis
#possuem maior relação com diabetes

#HEATMAP DE CORRELAÇÃO
fig, ax = plt.subplots(figsize=(14, 10))

#calcula matriz de correlaçao
corr_matrix = df.corr()

#cria mascara triangular
mask = np.triu(
    np.ones_like(corr_matrix, dtype=bool)
)

#VISUALIZAÇaO DE DISTRIBUIÇÕES COM SEABORN
sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=False,
    cmap="coolwarm",
    center=0,
    linewidths=0.3,
    ax=ax
)

#titulo
ax.set_title("Mapa de correlação entre todas as variáveis")

#organiza layout
plt.tight_layout()

#salva imagem
plt.savefig("fig6_heatmap.png", dpi=150)

#mostra grafico
plt.show()

#RESUMO FINAL
print(f"""
RESUMO DA EDA

Dataset:
- {len(df):,} linhas
- {df.shape[1]} colunas

Valores faltantes:
- {"Nenhum" if df.isnull().sum().sum() == 0 else df.isnull().sum().sum()}

Balanceamento:
- {contagem[0.0] / len(df):.1%} não diabético
- {contagem[1.0] / len(df):.1%} diabético

Top 5 variáveis mais correlacionadas:
{correlacoes.head(5).to_string()}

Observ:
-Dataset desbalanceado
-Considerar SMOTE ou class_weight na modelagem
-BMI, HighBP e GenHlth possuem forte associaçãao
-Dataset limpo e pronto para modelagem
""")