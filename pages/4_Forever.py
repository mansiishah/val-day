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

st.title("🌸 Chaitanya & Mansi – The Forever Arc")

st.markdown("""
You still owe me mac and cheese.
You still don’t know coding lol.
You still can’t stay serious for more than 30 seconds.
You still yap endlessly.

You are my nautaki boii.

Drama queen.
Main character energy.
Zero chill.

And somehow…
you are still my favorite person. ❤️
""")

forever_path = "assets/forever"

if os.path.exists(forever_path):
    cols = st.columns(2)
    images = sorted(os.listdir(forever_path))
    for i, img in enumerate(images[:2]):
        with cols[i]:
            st.image(f"{forever_path}/{img}")

st.markdown("""
Long distance isn’t easy.
But so far and so forth… it’s working.

And here’s something I don’t always say out loud:

I love your smile.
I love your voice.
I love how sensitive you are.

And most of all —
I love you.
To the core.

Even when I don’t say it dramatically.
Even when I pretend to be chill about it.

I really do.

And I do see a future with you.
Not just for a season.
But properly.
Seriously.
Forever.

Even if I made you delete the first proposal during the retrograde, (yes, it was on 20 March in case you are wondering),
I'm grateful that this happened.

If 2019 us could see this,
they would probably laugh.

Because all of this started
with some nautanki
and a little C programming.

Good things take time.
And I’m glad we waited.

Happy Valentine’s Day, Chaitanya 💖

I’m really glad it’s you.
""")

st.balloons()


col1, col2, col3 = st.columns([2, 4, 2])

with col1:
    if st.button("💗 ⬅️ Previous", use_container_width=True):
        st.switch_page("pages/3_Engagement.py")

with col3:
    if st.button("Play Again💖", use_container_width=True):
        st.switch_page("app.py")