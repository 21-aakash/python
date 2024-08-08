import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to dashbord !")

name = st.text_input("Enter your name :")

options= ['Python', 'C++' , 'Java', 'C#', 'Ruby']
choice = st.selectbox("Choose your language :" , options)
st.write(f"Your language is: {choice}")



age =st.slider('select your age: ' , 0, 100 , 25)

st.write(f"your age is : {age}")


if name:
    st.write(f"Hi {name}")

df = pd.DataFrame({

'grade':[101,102,1033],
'name':['aakash', 'tom', 'jake']

})


st.write(df)

df.to_csv('sample.csv')

upload_file = st.file_uploader("choose files ",type='csv')

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)