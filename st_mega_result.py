#IMPORTANDO BIBLIOTECAS
#manipulação de dados
import pandas as pd

#visualização de dados dinâmicos
import streamlit as st

#Título do aplicativo
st.write("""
### Conferência dos Resultados da Mega Da Virada\n
                
         """)

#dataset utilizado para treinamento do modelo
df = pd.read_html('data_base/Jogos1.html')
df = pd.DataFrame(df[0])
df.drop('n1',axis=1, inplace=True)
df.columns = ['n1','n2','n3','n4','n5','n6']
df['Acertos'] = 0

def confereJogo(resultado,jogos):
    resultado = resultado.split(',')
    for i, jogo in jogos.iterrows():
        acertos = 0
        for r in resultado:
            r = int(r)
            for j in jogo:
                if r == j:
                    acertos +=1
                    break
                else:
                    pass
        jogos['Acertos'].loc[i] = acertos 
    return jogos
            


#CABEÇALHO
st.subheader('Jogos Do Acamp')

#Nome do usuário
result_input = st.sidebar.text_input('Digite o resultado da Mega Da Virada:')
st.write('Mega: ', result_input)
if st.sidebar.button('Calcular Acertos'):
    df = confereJogo(result_input, df)

st.table(df)
