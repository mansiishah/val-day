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

st.title("💻🧀 The Mac & Cheese + Programming Era")

st.markdown("""
It started with mac and cheese?

You said he would make it for me.
Still pending.

Then came:
“I’ll teach you programming.”

C language sessions.
A programming book.
Very questionable progress.

Error 404: Mac and Cheese Not Found.
Status: Still Pending.

That 2.5-hour Baramati to Pune journey?
You yapped.
I laughed.

Some drama happened.
Timing wasn’t perfect.
But we didn’t vanish.

Good things take time.
""")



friends_path = "assets/friends"
cols = st.columns(3)
images = sorted(os.listdir(friends_path))

for i, img in enumerate(images):
    with cols[i % 3]:
        st.image(f"{friends_path}/{img}")



st.markdown("""
---

**Side Notes:**

• Student performance: Questionable.  
• Teacher patience: Legendary.  
• Mac & cheese status: Still pending.  

Error 404: Chef skills not found 🧀
""")






st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 2])

with col1:
    if st.button("💗 ⬅️ Previous", use_container_width=True):
        st.switch_page("app.py")

with col3:
    if st.button("Next ➡️ 💖", use_container_width=True):
        st.switch_page("pages/2_Dubai.py")
