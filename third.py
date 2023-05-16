import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

img0 = Image.open('images/0.png')
img1 = Image.open('images/1.png')
img2 = Image.open('images/2.png')
img3 = Image.open('images/3.png')
def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

nytv = load_lottiefile('lottiefiles/nytv.json')
icon = load_lottiefile('lottiefiles/icon.json')


st.set_page_config(page_title="Youtube Shorts Viewer", page_icon="🔻", layout='wide')

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css('style/style.css')

with st.container():
    st.subheader("Wanna skyrocket your Youtube channel views?")
    st.title("We're here for you!")

st.write("---")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(nytv, height=400, width=500)
    with right_column:
        st.header("What it Youtube Shorts Viewer?")
        st.write("##")
        st.write("""
        Youtube Shorts Viewer is a Web Automation tool that will take your Youtube channel URL
        goes to your shorts, play them for X seconds then goes to next short and so forth.
        It's 100% GENUINE. Youtube wont know that this is a BOT playing videos.
        Simply because this bot has it own ip and Youtube sees it as if it was a normal person watching your youtube shorts.
        I've been using it for quite a long time now and it is working as a charm.
        """)
        st.write("##")
        st.write("What are you waiting For?")
st.write("---")
st.subheader('Here are the performance from a newly created channel')
clm1, clm2 = st.columns(2)
with clm1:
    st.image(img0)
with clm2:
    st.image(img1)
st.write("---")
clm3, clm4 = st.columns(2)
with clm3:
    st.image(img2)
with clm4:
    st.image(img3)

st.write("---")
col_1, col_2 = st.columns([2, 1])
with col_1:
    st.title("What are you waiting for?")
    st.write("##")
    st.title("Fire up your Youtube NOW!!!")
    st.write("##")
    st.title("$19.99 FOR LIMITED TIME ONLY!")
    st.write("##")
    st.title("GET YOUR COPY NOW!!!")

with col_2:
    st_lottie(icon, height=500, width=500)

st.write("---")
st.header("CONTACT FOR MORE INFO!")
cf = """
<form action="https://formsubmit.co/n0nyf0xy@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name here" required>
     <input type="email" name="email" placeholder="Your e-mail here" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(cf, unsafe_allow_html=True)
with right_column:
    st.empty()