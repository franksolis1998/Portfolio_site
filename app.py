import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_kh4qi0dn.json")
img_contact_form = Image.open("images/bar_star.jpg")
img_Lottie_animation = Image.open("images/Kitten_True_For.jpg")
img_contact_form2 = Image.open("images/harmonica_shop.jpg")

with st.container():
    st.subheader("Hello there, I'm Francisco Solis :wave:")
    st.title('I am a fledgeling Programmer from Houston, Texas')
    st.write("I am a Classically Minded Person who is passionate about efficient and productive code.")
    st.write("I was rasied by my Father who was a hardworking and industrius man in his humble field of Janitorial Services but he instilled hard working values that I strive to achive, as a young professiaonal i have a 125lb Scooby-Doo lookalike dog named Waffles who brings joy to my life.")
    st.write("The hobbies I enjoy are camping, walking my dog, eating all the good food with my friends and i like attempting to solve algoithims.  ")
    st.write("[My GitHub >](https://github.com/franksolis1998)")
    st.write("[My Linkdln >](https://www.linkedin.com/in/francisco-solis-573707122/)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education")
        st.write("##")
        st.write(
            """
            My Technical education includes:
            - The Nucamp Web Development Fundementals course
            - The Nucamp Backend with Python Course
            - I am currently enrolled in the Fullstack Course at Nucamp

            There will be published programs, and webpages as my education proceeds.
            """
        )
        with right_column:
            st_lottie(lottie_coding, height=350, key="coding ")

    
with st.container():
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: black;'>The Images shown are placeholders and belong to thier repective owners, this app was created to see if i could make one</h1>", unsafe_allow_html=True)
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Lottie_animation)

        with text_column:
            st.subheader("Modernized Wizards101 clone called Wizards102!")
            st.write(
                """
                Wizards102!
                A more fluid landing, registering and logging in page(s) a more streamlined example of the famous MMO clone
                """
            )

with st.container():
    image_colmun, text_column = st.columns((1,2))
    with image_colmun:
        st.image(img_contact_form)
    with text_column:
        st.write("---")
        st.subheader("Bar Star")
        st.write(
            """
            A interactive mobile app for the user to find the best drink with anything immediately at hand! 
            """
        )

with st.container():
    image_colmun, text_column = st.columns((1,2))
    with image_colmun:
        st.image(img_contact_form2)
    with text_column:
        st.write("---")
        st.subheader("Harmonic Shop")
        st.write(
            """
            The next Generation of buying harmonicas from the ever elusive Tombo No. 1521 G#Nm Band Deluxe Harmonica
            to the most popular and powerful Hohner Marine Band, these and much more are available from independet dealers
            to the very creators of this historic instrument
            """
        )

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")


    contact_form ="""
    <form action="https://formsubmit.co/Aztecruss762@gmail.com" method="POST">
        <input type="hidden" name"_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()