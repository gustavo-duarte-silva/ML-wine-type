# Previsão do tipo de Vinho" 🍷

## Objetivo: 
> Realizar previsão no tipo de vinho se tinto ou branco e realizar o deploy do modelo na WEB .</br>
> Este Dataset foi obtido no Kaggle</br>
> Link do Dataset: https://www.kaggle.com/dell4010/wine-dataset
> 
## Estudo:
> Este estudo consiste num modelo de classificação, logo foi utilizado o modelo de machine learning ExtraTreesClassification : </br>

## Variaveis de Estudo
>* Variavel Target: ** Style: Red ou White ** </br>
>* Variaveis independentes (Features): fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
            chlorides, free_sulfur_dioxide, total_suldur_dioxide, 
            density, ph, sulphates e alcohol


## Conclusão: 
> Foi Observado que a variavel feature (Quality) é um Data leakage, sendo removido do nosso estudo </br>
> Foi obtido uma acuracia de 0.99, logo podemos observar que nosso modelo esta acertando todas as respostas.
> 
### Link do App: https://share.streamlit.io/gustavo-duarte-silva/ml-wine-type/main/app.py
