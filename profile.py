import streamlit as st
import os
import base64
from PIL import Image


st.set_page_config(page_title='My Profile Highlight')

image = Image.open("picture kshiti.jpeg")
col1,col2= st.columns(2)
with col1:
    st.title("Kshiti Raj Bhardwaj")
    st.write("Delhi university graduate")
    st.write("Intern at Innomatic research since feb'23")
    st.header('Contact Info: ')
    st.write('Email: kshitiraj.kr@gmaiil.com')
    st.write('LinkedIn: https://www.linkedin.com/mwlite/in/kshiti-r-25001b221')
with col2:
    st.image(image, caption='Kshiti Raj Bhardwaj')

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



st.header('Resume')

show_pdf("Kshiti Raj.pdf")