import streamlit as st
from openai import OpenAI

import pickle
from pathlib import Path
import streamlit_authenticator as stauth


st.set_page_config(page_title="Dashboard1", 
                   page_icon=None, 
                   layout="wide", 
                   initial_sidebar_state="collapsed", 
                   menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

# Hide streamlit elements
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .styles_stateContainer__CelYF.parent {visibility: hidden;}
            .styles_stateContainer__CelYF {visibility: hidden;}
            .viewerBadge_text__fzr3E {visibility: hidden;}
            .viewerBadge_link__qRIco {visibility: hidden;}
            .viewerBadge_link__qRIco.parent {visibility: hidden;}
            .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N {visibility: hidden;}
            
            .block-container
                {
                    padding-top: 0;
                    padding-bottom: 0rem;
                    margin-top: 0rem;
                }

            #root > div:nth-child(1) > div.withScreencast > div > div > div > section:nth-child(2)
            {
                    height: 3rem !important;
                }

            iframe 
                {
                aspect-ratio: 4 / 3;
                width: 100%;
                }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

title = "📄 Yee haw Update 5"
# Show title and description.
st.title(title)

#User Authentication
names = ["Miki Alanam", "John Doe"]
usernames = ["malanam", "jdoe"]

#Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    title,
    "asdfsfd",
    cookie_expiry_days= "30"
)

name, authentication_status, username = authenticator.login("Login" , "main")

if authentication_status == False:
    st.error("Username / Password is incorrect")

if authentication_status == None:
    st.error("Please enter your Username and Password")

if authentication_status == True:
    #Embed PBI Code
    st.components.v1.iframe(
        "https://app.powerbi.com/view?r=eyJrIjoiNjM3ODcwOTAtOWU0Yy00NjI3LWEzZDctNjcxYzE4ZDY2NjU3IiwidCI6ImQxNTY2ZDQ0LTEyYjYtNDAyNy1iZDA0LWQyOTJmZWE3OWM5ZSJ9", 
        height=800, 

        scrolling=True)