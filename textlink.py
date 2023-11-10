import streamlit as st
import re
import pandas as pd
import numpy as np

st.title('generate a link for people to text/email you')
platform = st.radio("choose your platform", ['sms', 'email'])

if platform == 'sms':
    number = st.text_input("input your phone number here with area code:")
    pattern = re.compile(r'^\d{11}$')
    if pattern.match(number):
        message = st.text_input("input your message")
        if len(message) > 1:
            message = message.replace(' ', '%20')
            st.subheader('copy this link')
            linktocopy = f'sms://+{number};?&body={message}'
            st.code(linktocopy, language="css")
            st.balloons()

if platform == 'email':
    email = st.text_input("input your email")
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if pattern.match(email):
        subject = st.text_input("input your email subject")
        subject = subject.replace(' ', '%20')
        if len(subject) > 1:
            body = st.text_area("input your email body")
            body = body.replace(' ', '%20')
            body = body.replace('\n', '%20%0A')
            if len(body) > 1:
                st.subheader('copy this link')
                linktocopy = f"mailto:{email}?subject={subject}&body={body}"
                st.code(linktocopy, language="css")
                st.balloons()
st.write("built by [ishan deshpande](https://twitter.com/_ishand_)")