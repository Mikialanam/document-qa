import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Dashboard1", 
                   page_icon=None, 
                   layout="wide", 
                   initial_sidebar_state="collapsed", 
                   menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
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

# Show title and description.
st.title("📄 Yee haw Update 5")

st.components.v1.iframe(
    "https://app.powerbi.com/view?r=eyJrIjoiNjM3ODcwOTAtOWU0Yy00NjI3LWEzZDctNjcxYzE4ZDY2NjU3IiwidCI6ImQxNTY2ZDQ0LTEyYjYtNDAyNy1iZDA0LWQyOTJmZWE3OWM5ZSJ9", 
     height=800, 
  #  width = '90%',
    scrolling=True)