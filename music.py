import base64
import streamlit as st

def autoplay_music():
    with open("assets/music/theme.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    st.markdown(f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)
