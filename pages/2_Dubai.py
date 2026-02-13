import streamlit as st
import os
from music import autoplay_music

st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none !important;}
button[kind="header"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

autoplay_music()

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.title("🌍 Dubai – The Catalyst")

st.markdown("""
Three weeks of talking.
One impulsive plan.

We met again.

We fought.
We laughed.
We were dramatic.
We were sensitive.

But somehow…
it felt right.

Dubai was the catalyst.
""")

dubai_path = "assets/dubai"
cols = st.columns(3)
images = sorted(os.listdir(dubai_path))

for i, img in enumerate(images):
    with cols[i % 3]:
        st.image(f"{dubai_path}/{img}")

st.markdown("""
---

Official Traits of Chaitanya:

• Smile: Dangerous.  
• Voice: The original reason.  
• Sensitivity level: High.  
• Drama level: Nautaki boii certified.
""")

love = st.slider("How much do you love me? 💖", 0, 100, 0)
if love < 100 and love>0 :
    st.warning("Hmm… interesting choice. We don’t do partial love here 😌")
elif love == 100:
    st.success("We go all in haha 💖🔥")


st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 2])

with col1:
    if st.button("💗 ⬅️ Previous", use_container_width=True):
        st.switch_page("pages/1_Story.py")

with col3:
    if st.button("Next ➡️ 💖", use_container_width=True,disabled=(love < 100)):
        st.switch_page("pages/3_Engagement.py")
