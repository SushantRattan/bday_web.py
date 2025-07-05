import streamlit as st
from PIL import Image
import base64
import os
st.write("Current directory:", os.getcwd())
st.write("Files in dir:", os.listdir())


st.set_page_config(page_title="🎀 Sabbyyy's Birthday Surprise", layout="centered")

# 🎵 Background music
def play_music(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

# 🖼️ Show image
def show_image(img_path, width):
    img = Image.open(img_path)
    st.image(img, use_column_width=False, width=width)

# 💌 Birthday message
def show_message():
    st.markdown("## 💌 From Tatan to Sabbyyy")
    st.markdown("""
    > **Hey Sabbyyy! 🎉**  
    > Happy Birthday to the girl who makes online friendship magical! ✨  
    > You’re like a sunny sky with sparkles — always bright, always beautiful. 🌈  
    > Semoga harimu dipenuhi dengan cinta dan tawa. 💖  
    > Never stop being the cute, chaotic, amazing you!  
    >  
    > With virtual hugs,  
    > **Tatan 🧃🫶🏼**
    """)
    st.markdown("🎂✨💐💝🌸💖")

# 🎀 Main layout
st.title("🎈 Happy Birthday Sabbyyy 🎈")

# 🌸 Emojis header
st.markdown("❤️ ✨ 💖 🌸 💐 🌷 ✨ 💝")

# 🎵 Play background music
play_music("happy.mp3")

# 🖼️ Show all 4 images
st.subheader("📸 Some Memories")
cols = st.columns(2)

with cols[0]:
    show_image("1.jpg", width=300)
    show_image("sabbyyy_beach.jpg", width=300)

with cols[1]:
    show_image("2.jpg", width=300)
    show_image("sabbyyy_portrait.jpg", width=300)

# 💌 Message button
if st.button("Open My Message 💌"):
    show_message()
