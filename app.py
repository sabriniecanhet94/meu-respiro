import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

# ------------------------------------------------
# Configuração da Página
# ------------------------------------------------
st.set_page_config(
    page_title="Meu Respiro | Guia Prático",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------
# Estilo Avançado (CSS) - UI/UX Acolhedora
# ------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #FAF6F0;
        color: #333333;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h1, h2, h3 {
        color: #3A4635 !important;
        font-family: 'Georgia', serif;
        font-weight: normal;
    }
    section[data-testid="stSidebar"] {
        background-color: #EFECE6;
        border-right: 1px solid #D2D7CD;
    }
    section[data-testid="stSidebar"] .stMarkdown, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #3A4635 !important;
    }
    section[data-testid="stSidebar"] div[data-baseweb="radio"] label div p {
        color: #3A4635 !important;
        font-weight: 500;
        font-size: 11pt;
    }
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #D2D7CD;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    .stButton>button {
        background-color: #76856F !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 20px;
        font-weight: 600;
        width: 100%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #5B6854 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    input, textarea, select, div[data-baseweb="select"] {
        color: #2C2C2C !important;
        background-color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 1px solid #B8C0B2 !important;
    }
    label, .stTextInput label, .stTextArea label, .stSlider label {
        color: #3A4635 !important;
        font-weight: 600 !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# Inicialização do Estado Seguro (Sessão do Usuário)
# ------------------------------------------------
if 'gargalos' not in st.session_state:
    st.session_state['gargalos'] = pd.DataFrame(columns=['Data', 'Causa', 'Impacto', 'Sentimento'])
if 'respiros' not in st.session_state:
    st.session_state['respiros'] = 0
if 'vitorias' not in st.session_state:
    st.session_state['vitorias'] = []

# ------------------------------------------------
# Menu Lateral de Navegação
# ------------------------------------------------
st.sidebar.title("🌿 Meu Respiro")
st.sidebar.markdown("*O seu refúgio diário de paz e privacidade.*")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navegação:",
    ["Início", "Limpar a Mente", "Minhas Pausas", "Diário de Gratidão"]
)

st.sidebar.markdown("---")
st.sidebar.info("🔒 **Sigilo Absoluto:** Suas reflexões pertencem apenas a você. Nenhum dado sensível é armazenado em servidores externos.")

# ------------------------------------------------
# Tela 1: Início (Visão Geral)
# ------------------------------------------------
if menu == "Início":
    st.title("O Seu Jardim Interior")
    st.write("Um espaço 100% seguro e privado para olhar para dentro, medir o seu bem-estar e celebrar a sua constância de forma leve.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin:0; font-size: 26pt; color: #5B6854 !important;">{st.session_state['respiros']}</h3>
                <p style="margin:5px 0 0 0; font-size: 10pt; color: #666; font-weight: bold;">Respiros Feitos</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin:0; font-size: 26pt; color: #5B6854 !important;">{len(st.session_state['gargalos'])}</h3>
                <p style="margin:5px 0 0 0; font-size: 10pt; color: #666; font-weight: bold;">Gargalos Mapeados</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin:0; font-size: 26pt; color: #5B6854 !important;">0 🔥</h3>
                <p style="margin:5px 0 0 0; font-size: 10pt; color: #666; font-weight: bold;">Dias de Ofensiva</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.subheader("Para onde a sua energia está indo?")
    if not st.session_state['gargalos'].empty:
        df_chart = st.session_state['gargalos'].groupby('Causa')['Impacto'].sum().reset_index()
        fig = px.bar(df_chart, x='Causa', y='Impacto', title="")
        fig.update_traces(marker_color='#76856F')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Helvetica", color="#333333"),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='#D2D7CD')
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("🌱 Seu painel de gráficos está aguardando os primeiros registros. Vá até a aba 'Limpar a Mente' para começar.")

# ------------------------------------------------
# Tela 2: Limpar a Mente (Mapeamento de Gargalos)
# ------------------------------------------------
elif menu == "Limpar a Mente":
    st.title("Tampando os Furinhos do Jarro")
    st.write("Identifique o que sugou a sua paz hoje de forma gentil e confidencial.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("form_gargalos", clear_on_submit=True):
        causa = st.text_input("O que drenou a sua energia hoje? (máx. 80 caracteres)", max_chars=80, placeholder="Ex: Excesso de notificações...")
        impacto = st.slider("Qual foi o nível de impacto disso?", 1, 10, 5)
        sentimento = st.text_area("Como você se sentiu? (máx. 200 caracteres)", max_chars=200, placeholder="Ex: Senti um aperto no peito...")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submit = st.form_submit_button("Salvar Registro")
        
        if submit:
            if causa:
                novo_dado = pd.DataFrame({
                    'Data': [datetime.date.today().strftime('%d/%m/%Y')],
                    'Causa': [causa],
                    'Impacto': [impacto],
                    'Sentimento': [sentimento]
                })
                st.session_state['gargalos'] = pd.concat([st.session_state['gargalos'], novo_dado], ignore_index=True)
                st.success("✨ Registro salvo com segurança na sua sessão privada!")
            else:
                st.warning("Por favor, preencha o que drenou a sua energia.")

    if not st.session_state['gargalos'].empty:
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("O seu histórico recente")
        st.dataframe(st.session_state['gargalos'], use_container_width=True)

# ------------------------------------------------
# Tela 3: Minhas Pausas (Agenda Leve)
# ------------------------------------------------
elif menu == "Minhas Pausas":
    st.title("O Meu Novo Respiro")
    st.write("Reserve 5 minutinhos para si mesmo. Clique no botão abaixo sempre que realizar a sua pausa.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🌅 Manhã")
        st.write("Um instante de silêncio antes de começar o dia.")
        if st.button("Registrar Respiro (Manhã)"):
            st.session_state['respiros'] += 1
            st.toast("🌿 Pausa matinal registrada! Seu jarro agradece.", icon="✨")
            
    with col2:
        st.markdown("### ☀️ Tarde")
        st.write("Uma pausa para realinhar o foco e relaxar os ombros.")
        if st.button("Registrar Respiro (Tarde)"):
            st.session_state['respiros'] += 1
            st.toast("☀️ Pausa da tarde registrada! Energia recarregada.", icon="✨")
            
    with col3:
        st.markdown("### 🌙 Noite")
        st.write("Soltar as tensões para garantir um sono tranquilo.")
        if st.button("Registrar Respiro (Noite)"):
            st.session_state['respiros'] += 1
            st.toast("🌙 Pausa noturna registrada! Descanse em paz.", icon="✨")

# ------------------------------------------------
# Tela 4: Diário de Gratidão (Pequenas Vitórias)
# ------------------------------------------------
elif menu == "Diário de Gratidão":
    st.title("O Seu Diário de Coisas Boas")
    st.write("Toda vitória conta! Anote um motivo simples de gratidão para guardar no coração.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    nova_vitoria = st.text_input("Qual foi a sua pequena vitória de hoje? (máx. 120 caracteres)", max_chars=120, placeholder="Ex: Consegui dizer 'não' a algo que me faria mal...")
    if st.button("Salvar no Diário"):
        if nova_vitoria:
            st.session_state['vitorias'].insert(0, f"✨ {datetime.date.today().strftime('%d/%m/%Y')} — {nova_vitoria}")
            st.success("Vitória guardada com carinho no seu diário privado!")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("A sua linha do tempo de gratidão:")
    
    if st.session_state['vitorias']:
        for vitoria in st.session_state['vitorias']:
            st.info(vitoria)
    else:
        st.write("🌿 O seu diário ainda está vazio. Que tal celebrar algo simples que aconteceu hoje?")