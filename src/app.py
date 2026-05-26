#cria interface web
import streamlit as st
# trabalha com arrays/listas numericas
import numpy as np
#carrega modelo salvo
import joblib

#CARREGA MODELO TREINADO
model = joblib.load("notebooks/modelo_diabetes.pkl")

#TÍTULO DA INTERFACE
#título principal da página
st.title("Predição de Diabetes Tipo 2")
#pequeno texto abaixo do título
st.write("Preencha os dados abaixo para estimar o risco de diabetes.")

#BMI / IMC
#campo numérico para IMC
bmi = st.number_input(
    #texto exibido
    "IMC (Índice de Massa Corporal)",
    #valor mínimo
    min_value=10.0,
    #valor máximo
    max_value=60.0,
    #valor inicial
    value=25.0
)
#explicação do IMC
st.caption(
    "IMC abaixo de 18.5 = baixo peso | 18.5 a 24.9 = normal | acima de 30 = obesidade"
)



#PRESSÃO ALTA
#caixa de seleção
highbp = st.selectbox(
    #pergunta
    "Possui pressão alta?",
    #opções
    ["Não", "Sim"]
)
#transforma texto em número
highbp = 1 if highbp == "Sim" else 0


#COLESTEROL ALTO
highchol = st.selectbox(
    "Possui colesterol alto?",
    ["Não", "Sim"]
)
highchol = 1 if highchol == "Sim" else 0



#ATIVIDADE FÍSICA
phys = st.selectbox(
    "Pratica atividade física?",
    ["Sim", "Não"]
)
phys = 1 if phys == "Sim" else 0



#SEXO BIOLÓGICO
sex = st.selectbox(
    "Sexo biológico",
    ["Feminino", "Masculino"]
)
sex = 1 if sex == "Masculino" else 0


#FAIXA ETÁRIA
age = st.selectbox(
    "Faixa etária",
    [
        "18-24",
        "25-29",
        "30-34",
        "35-39",
        "40-44",
        "45-49",
        "50-54",
        "55-59",
        "60-64",
        "65-69",
        "70-74",
        "75-79",
        "80+"
    ]
)


#converte faixa etária em número
age_map = {
    "18-24": 1,
    "25-29": 2,
    "30-34": 3,
    "35-39": 4,
    "40-44": 5,
    "45-49": 6,
    "50-54": 7,
    "55-59": 8,
    "60-64": 9,
    "65-69": 10,
    "70-74": 11,
    "75-79": 12,
    "80+": 13
}
age = age_map[age]



#BOTÃO
# botão de previsão
if st.button("Prever risco"):
    #cria lista com dados do usuário
    dados = np.array([[
        highbp,
        highchol,
        bmi,
        phys,
        sex,
        age
    ]])


    #modelo faz previsão
    pred = model.predict(dados)
    #resultado positivo
    if pred[0] == 1:
        st.error("ALTO RISCO DE DIABETES")

    # resultado negativo
    else:
        st.success("BAIXO RISCO DE DIABETES")