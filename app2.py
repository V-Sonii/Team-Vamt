import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

page_bg_img = '''
<style>
body {
background-image: url("C:/Users/HP/Desktop/court.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:court/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
set_png_as_page_bg('court.jpg')



st.title("E-COURT WEBSITE")
st.subheader("This model will retrieve similar judgements from the database using search keywords")
# page_bg_img = <style> .stApp{ background-image: url("C:\Users\HP\Desktop\court.jpg"); background-size: cover; }</style>


def part1():
    sex = st.selectbox("Sex",options=['Male' , 'Female'])
    age = st.slider("Age", 1, 100,1)
    p_class = st.selectbox("Crime Type",options=['Murder','Drink and Drive','Rape','Robbery','Aggravated assault','Property Crimes'])
    sex = 0 if sex == 'Male' else 1
    a,b,c,d,e,f = 0,0,0,0,0,0
    if p_class == 'Rape':
            a = 1
    elif p_class == 'Drink and Drive':
            b = 1
    elif p_class == 'Murder':
            c = 1
    elif p_class == 'Robbery':
            d = 1
    elif p_class == 'Aggravated assault':
            e = 1
    else:
            f = 1
    evidence = st.selectbox("Evidence",options=['Yes' , 'No'])
    if st.button('Output'):
       
        #add warning for image not selected
        # image = np.asarray(image)
        # pred = model.predict(image.reshape(1,28,28,1))



        import time
        my_bar = st.progress(0)
        with st.spinner('Processing'):
            time.sleep(2)
    return
def part2():
    image=Image.open('C:/Users/HP/Desktop/court.jpg')
    st.image(image , use_column_width=True)
    return "The Supreme Court of India (IAST: Bhāratīya Ucchatama Nyāyālaya) is the supreme judicial body of India and the highest court of India under the constitution. It is the most senior constitutional court, and has the power of judicial review ."


analysis = st.sidebar.selectbox('EXPLORE US',['Get Information About Us','JUDGEMENT ANALYSIS'])
if analysis=='JUDGEMENT ANALYSIS':
    part1()
    st.success("Working")
else:
    part2()

