import streamlit as st
import os
from music import autoplay_music
import streamlit.components.v1 as components

st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none !important;}
button[kind="header"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

autoplay_music()

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.title("💍 Engagement – Sum = 9 Energy")

st.markdown("""
26 October.
Because 2 + 6 + 1 + 0 + 2 + 0 + 2 + 5 = 9.

It didn’t happen the day that I had in mind.

Because someone said:
“I’m not good at proposing, so you do it.”🫣

But then a family dinner happened.

Two days later…
Mehendi.
Outfits.
Rings.
Decor.
Photographer.
Everything.

From lets meet soon promises
to forever plans.
""")
eng_path = "assets/engagement"

images = sorted(os.listdir(eng_path))

cols = st.columns(3)

for i, img in enumerate(images):
    with cols[i % 3]:
        st.image(f"{eng_path}/{img}")
        
st.divider()

st.markdown("### 💖 Officially Engaged 💖")

st.success("Status Updated → Forever plans 💍✨")

if st.checkbox("Click only if you are curious 👀"):
    st.write("I love you <3")


st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 2])

with col1:
    if st.button("💗 ⬅️ Previous", use_container_width=True):
        st.switch_page("pages/2_Meet.py")

with col3:
    if st.button("Next ➡️ 💖", use_container_width=True):
        st.switch_page("pages/4_Forever.py")


