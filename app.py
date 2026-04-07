import streamlit as st

st.set_page_config(page_title="Mi juego", page_icon="🎮")

st.title("🌌 Elige tu destino")
st.write("Una historia donde tus decisiones cambian todo... 👀")

if "escena" not in st.session_state:
    st.session_state.escena = "inicio"

if st.session_state.escena == "inicio":
    st.write("Despiertas en un bosque oscuro 🌲🌙")
    if st.button("✨ Seguir la luz"):
        st.session_state.escena = "luz"
    if st.button("🌑 Ir al bosque profundo"):
        st.session_state.escena = "bosque"

elif st.session_state.escena == "luz":
    st.write("Encuentras una cabaña misteriosa 🏠")
    if st.button("🚪 Entrar"):
        st.session_state.escena = "cabaña"
    if st.button("🏃 Huir"):
        st.session_state.escena = "inicio"

elif st.session_state.escena == "bosque":
    st.write("Sientes que algo te observa... 👁️")
    if st.button("🏃 Correr"):
        st.session_state.escena = "perdiste"
    if st.button("🫣 Esconderte"):
        st.session_state.escena = "ganaste"

elif st.session_state.escena == "cabaña":
    st.write("Encuentras un tesoro brillante 💰✨")
    st.success("🎉 GANASTE")
    if st.button("🔄 Jugar otra vez"):
        st.session_state.escena = "inicio"

elif st.session_state.escena == "perdiste":
    st.error("💀 PERDISTE")
    if st.button("🔄 Intentar otra vez"):
        st.session_state.escena = "inicio"

elif st.session_state.escena == "ganaste":
    st.success("🎉 ESCAPASTE Y GANASTE")
    if st.button("🔄 Jugar otra vez"):
        st.session_state.escena = "inicio"
