import streamlit as st
#saída mensagem exibida na tela
st.write('Sou servidora pública!')

st.title('Este é o Título do app')
st.header('Este é o Subtítulo')
st.subheader('Este é o terceiro subtítulo')

resposta = st.slider('Informe o grau de satisfação:', min_value=0, max_value=100)
st.write(resposta)
