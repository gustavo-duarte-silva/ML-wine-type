import numpy as np
import streamlit as st
import joblib
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My Deploy", page_icon=":pager:")
model = open("modelo.pkl", 'rb')
model = joblib.load(model)

def load_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

wine_animation = load_animation('https://assets7.lottiefiles.com/packages/lf20_RFHPja.json')

def predict(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
            chlorides, free_sulfur_dioxide, total_suldur_dioxide, 
            density, ph, sulphates, alcohol):
            
            ypred = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                            chlorides, free_sulfur_dioxide, total_suldur_dioxide, 
                            density, ph, sulphates, alcohol])
            ypred = ypred.reshape(-1,11)
            ypred = ypred.astype(np.float64)

            model_predict = model.predict(ypred)
            return model_predict

with st.container():
    image, text = st.columns(2)
    with text:
        st.header("Previsão do Tipo de Vinho :wine_glass:")
        st.write("Este projeto tem o objetivo de prever qual é o tipo de vinho, de acordo com a suas caracteristicas, se é vinho tinto ou branco")
    with image:
        st_lottie(wine_animation, height=200, key='wine')

with st.container():
    st.header("Caracteristica do Vinho: ")
    col1, col2, col3 = st.columns(3)
    with col1:
        fixed_acidity=st.number_input("Acidez Fixa")
        volatile_acidity=st.number_input("Acidez Volatil")
        citric_acid=st.number_input("Acido citrico")
        residual_sugar=st.number_input("Açucar Residual")
    with col2:
        chlorides=st.number_input("Cloretos")
        free_sulfur_dioxide = st.number_input ("Dioxido de Enxofre livre")
        total_suldur_dioxide = st.number_input("Dioxido de Enxofre Total")
        density = st.number_input("Densidade")
    with col3:
        ph = st.number_input("pH")
        sulphates = st.number_input("Sulfatos")
        alcohol = st.number_input("álcool")

prediction = ""

if st.button("Previsão"):
    prediction = predict(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
                        total_suldur_dioxide, density, ph, sulphates, alcohol)
    if prediction == 0:
        st.success("O Vinho é Branco")
    if prediction == 1:
        st.success("O Vinho é Tinto")

st.subheader("Informações sobre as Caracteristica do Vinho")
with st.expander("Abra para mais informações: "):
    st.markdown("""
            - acidez fixa: a maioria dos ácidos envolvidos com o vinho ou fixos ou não voláteis (não evapora facilmente)

- acidez volátil: a quantidade de ácido acético no vinho, que em níveis muito altos pode levar a um gosto desagradável de vinagre

- ácido cítrico: encontrado em pequenas quantidades, o ácido cítrico pode adicionar 'frescor' e sabor aos vinhos

- açúcar residual: quantidade de açúcar que fica após a parada da fermentação, é raro encontrar vinhos com menos de 1 grama / litro e vinhos com mais de 45 gramas / litro são considerados doces

- cloretos: a quantidade de sal no vinho

- dióxido de enxofre livre: a forma livre de SO2 existe em equilíbrio entre o SO2 molecular (como um gás dissolvido) e o íon bissulfito; impede o crescimento microbiano e a oxidação do vinho

- dióxido de enxofre total: quantidade de formas livres e ligadas de S02; em baixas concentrações, o SO2 é principalmente indetectável no vinho, mas em concentrações de SO2 livre acima de 50 ppm, o SO2 torna-se evidente no nariz e no sabor do vinho

- densidade: a densidade da água é próxima à da água dependendo do teor de álcool e açúcar

- pH: descreve o quão ácido ou básico um vinho é na escala de 0 (muito ácido) a 14 (muito básico); a maioria dos vinhos está entre 3-4 na escala de pH

- sulfatos: aditivo do vinho que pode contribuir para os níveis de gás sulfuroso (S02), que atua como antimicrobiano e antioxidante

- álcool: o teor de álcool percentual do vinho

    
    """)
    st.write("Informações Obtidas nesse [Artigo](https://rstudio-pubs-static.s3.amazonaws.com/57835_c4ace81da9dc45438ad0c286bcbb4224.html)")