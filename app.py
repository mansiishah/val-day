import streamlit as st
import base64
import time
from music import autoplay_music
st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none !important;}
button[kind="header"] {display: none !important;}
</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Happy Valentine’s Day 💖", page_icon="💘")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



autoplay_music()

import streamlit.components.v1 as components

components.html("""
<style>
.sakura-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: -1;
}

.petal {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #ffc1e3, #ff69b4);
    animation: fall linear infinite;
}

/* Depth variations */
.petal.small {
    width: 6px;
    height: 6px;
    opacity: 0.5;
    filter: blur(1px);
}

.petal.medium {
    width: 10px;
    height: 10px;
    opacity: 0.7;
}

.petal.large {
    width: 14px;
    height: 14px;
    opacity: 0.9;
    filter: blur(0.5px);
}

/* Floating motion */
@keyframes fall {
    0% {
        transform: translateY(-10vh) translateX(0);
    }
    100% {
        transform: translateY(110vh) translateX(40px);
    }
}
</style>

<div class="sakura-container">
    <div class="petal small" style="left:5%; animation-duration:8s;"></div>
    <div class="petal medium" style="left:15%; animation-duration:7s;"></div>
    <div class="petal large" style="left:25%; animation-duration:9s;"></div>
    <div class="petal small" style="left:35%; animation-duration:6s;"></div>
    <div class="petal medium" style="left:45%; animation-duration:8s;"></div>
    <div class="petal large" style="left:55%; animation-duration:7s;"></div>
    <div class="petal small" style="left:65%; animation-duration:9s;"></div>
    <div class="petal medium" style="left:75%; animation-duration:6s;"></div>
    <div class="petal large" style="left:85%; animation-duration:8s;"></div>
    <div class="petal small" style="left:95%; animation-duration:7s;"></div>
</div>
""", height=300)




st.markdown("<h1 class='fade-in'>Chaitanya… 💖</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='fade-in'>Would you be my Valentine?</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="valentine-text">
Happy Valentine’s Day, nautanki boii 💕
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])

with col2:
    col_yes, col_no = st.columns(2)

    with col_yes:
        yes_clicked = st.button("🥹 Yes", use_container_width=True)

    with col_no:
        no_clicked = st.button("😏 No", use_container_width=True)

if no_clicked:
    st.warning("HAHA. That was a trap. No backsies now. You’re stuck with me.")

if yes_clicked:
   st.session_state.start_music = True
   with st.spinner("Loading your destiny..."):
       time.sleep(2)
   st.switch_page("pages/1_Story.py")

