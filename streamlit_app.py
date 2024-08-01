import streamlit as st
from openai import OpenAI


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .styles_stateContainer__CelYF {visibility: hidden;}
            .viewerBadge_text__fzr3E {visibility: hidden;}
            .viewerBadge_link__qRIco {visibility: hidden;}
            .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Show title and description.
st.title("📄 Yee haw Update 5")

st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNjM3ODcwOTAtOWU0Yy00NjI3LWEzZDctNjcxYzE4ZDY2NjU3IiwidCI6ImQxNTY2ZDQ0LTEyYjYtNDAyNy1iZDA0LWQyOTJmZWE3OWM5ZSJ9", height=700, width = 1000, scrolling=True)