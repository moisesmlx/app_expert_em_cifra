# _*_ coding:utf-8 _*_
import streamlit as st
import pandas as pd
from trans_A import *
from trans_Am import *
from trans_Astm import *
from trans_Ast import *
from trans_B import *
from trans_Bm import *
from trans_C import *
from trans_Cm import *
from trans_Cst import *
from trans_Cstm import *
from trans_D import *
from trans_Dm import *
from trans_Dst import *
from trans_Dstm import *
from trans_E import *
from trans_Em import *
from trans_F import *
from trans_Fm import *
from trans_Fst import *
from trans_Fstm import *
from trans_G import *
from trans_Gm import *
from trans_Gst import *
from trans_Gstm import *
from enviar_file import *
from pdf import *
from escala import *
import random
import zipp
import os


# Armazenar dados descartavel

def clear():

    # limpando
    temporario = os.listdir('temporarios')
    if int(len(temporario)) > 1000:
        for linha in temporario:
            os.system(fr'del /s /q temporarios\{linha}')
            st.info('Os arquivo temporarios foram lipados')

# logica de cifra automatica


@st.cache_resource
class Expert_Em_Cifras():
    def __init__(self, n_cifra, original, mudado, text_area, id):
        clear()
        def translate(self):
                if str(n_cifra) != '':
                    try:
                        if original.upper() == 'A':
                            Trans_A(n_cifra, original, mudado, text_area, id)
                        if original == 'Am':
                            Trans_Am(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'A#':
                            Trans_Ast(n_cifra, original, mudado, text_area, id)
                        if original == 'A#m':
                            Trans_Astm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'B':
                            Trans_B(n_cifra, original, mudado, text_area, id)
                        if original == 'Bm':
                            Trans_Bm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'C':
                            Trans_C(n_cifra, original, mudado, text_area, id)                  
                        if original == 'Cm':
                            Trans_Cm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'C#':
                            Trans_Cst(n_cifra, original, mudado, text_area, id)
                        if original == 'C#m':
                            Trans_Cstm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'D':
                            Trans_D(n_cifra, original, mudado, text_area, id)
                        if original == 'Dm':
                            Trans_Dm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'D#':
                            Trans_Dst(n_cifra, original, mudado, text_area, id)
                        if original == 'D#m':
                            Trans_Dstm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'E':
                            Trans_E(n_cifra, original, mudado, text_area, id)
                        if original == 'Em':
                            Trans_Em(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'F':
                            Trans_F(n_cifra, original, mudado, text_area, id)
                        if original == 'Fm':
                            Trans_Fm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'F#':
                            Trans_Fst(n_cifra, original, mudado, text_area, id)
                        if original == 'F#m':
                            Trans_Fstm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'G':
                            Trans_G(n_cifra, original, mudado, text_area, id)
                        if original == 'Gm':
                            Trans_Gm(n_cifra, original, mudado, text_area, id)
                        if original.upper() == 'G#':
                            Trans_Gst(n_cifra, original, mudado, text_area, id)
                        if original == 'G#m':
                            Trans_Gstm(n_cifra, original, mudado, text_area, id)
                      
                        with open(fr'Minhas_cifras/{n_cifra}.txt', 'r', encoding='utf-8') as texto:
                            self.nova_cifra = str(texto.read())
                            create_pdf(fr'Minhas_cifras/{n_cifra}', f'Minhas_cifras/{n_cifra}')
                        
                        st.success(f'Sucesso, a troca de escala foi concluída de "{original}" para "{mudado}"')
                    except Exception as error:
                        st.warning(f'Ouve um erro!\n Por favor cheque as informações!\n{error} main')

                else:
                    st.warning(f'Ouve um erro!\n Por favor cheque as informações!\n{error}')

        translate(self)
#fim da logica

cor_de_fundo = "#d4eae8c5"  # Exemplo: cor cinza escuro

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {cor_de_fundo};
        color: 'blue'
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.set_page_config(page_title='🎵Expert em Cifras', layout='centered')
st.title('🎵:blue[Expert Em Cifras]')

col1, col2, col3 = st.columns([1,2,3])
with col2:
    st.image('static/logo.png')
st.markdown('''
            <h2 style="color: blue; text_align: center;">Bem vindo ao Expert Em Cifras.</h2>
            <p style="color: blue;">Aqui você pode mudar o tom de sua cifra de forma automática,
            para qualquer tom.</p>''',
            unsafe_allow_html=True
            )


# Criando o contêiner do formulário
tons = [
    'A', 'Am', 'A#', 'A#m',
    'B', 'Bm',
    'C', 'Cm', 'C#', 'C#m',
    'D', 'Dm', 'D#', 'D#m',
    'E', 'Em',
    'F', 'Fm', 'F#', 'F#m',
    'G', 'Gm', 'G#', 'G#m'
        ]

list_codigos_letras = ['owiwbh', 'fghgvfwrp', 'wrwr', 'rewrw', 'oyy', 'ngf', 'gyoh']
cripto_id = f'''{str(random.choice(list_codigos_letras))}{str(random.choice(list_codigos_letras))}{str(random.choice(list_codigos_letras))}{str(random.randint(1000, 50000000))}''' 

with st.form(key="meu_formulario", width=500):
    
    nome = st.text_input(':blue[Digite um nome para sua cifra:]', placeholder='Nome da Cifra')
    tom_original = st.selectbox("Escolha tom original:", tons)
    novo_tom = st.selectbox("Escolha novo tom:", tons)

    # Widget para upload do arquivo
    uploaded_file = st.file_uploader("Escolha um arquivo tipo txt", type='txt')
    cifra = st.text_area("Ou cole sua cifra aqui com ctrl+v:")
    # Verifica se um arquivo foi carregado

    
    # Botão de envio obrigatório dentro do formulário
    botao_enviar = st.form_submit_button(label="Enviar Dados")
<<<<<<< Updated upstream
    
=======


>>>>>>> Stashed changes
# Processando as informações após o clique
if botao_enviar:
    if nome == '':
        st.warning('Por favor, Digite um nome.')
    else:
        if uploaded_file is not None:
            # Lê o arquivo utilizando o pandas
            conteudo = uploaded_file.read().decode('utf-8')
    
            Expert_Em_Cifras(nome, tom_original, novo_tom, conteudo, cripto_id)
        else:
            Expert_Em_Cifras(nome, tom_original, novo_tom, cifra, cripto_id)

        st.write(f'**Nome da Cifra:** {nome}')
        st.write(f"**Tom Original:** {tom_original}")
        st.write(f"**Novo Tom:** {novo_tom}")
        with open(fr'Minhas_cifras/{nome}.txt', 'r', encoding='utf-8') as texto:
            n_cifra = texto.read()
        zipp.zipp(nome, fr'Minhas_cifras/{nome}.txt')
        zipp.zipp(nome, fr'Minhas_cifras/{nome}.pdf')


        # Download de um arquivo existente (ex: PDF ou ZIP)
        # Abra o arquivo em modo de leitura binária ("rb")
        with open(fr'Minhas_cifras/{nome}.zip', "rb") as arquivo_zip:
            st.download_button(
                
                label=f"Baixar sua cifra {nome} em zip",
                data=arquivo_zip,
                file_name=fr'Minhas_cifras/{nome}.zip',
                mime="application/pdf"
            )
