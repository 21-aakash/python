import streamlit as st
import pandas as pd
import numpy as np

## title of the app

st.title("hello Aakash!!")

st.write("this is a simple text")

##create a dataframe

df = pd.DataFrame({

'grade':[101,102,1033],
'name':['aakash', 'tom', 'jake']

})

#displayb tyhis dataframe

st.write("here is the dataframe")
st.write(df)

#create a linechart 

chart = pd.DataFrame(
    np.random.randn(20,2), columns=['a','b']
)

st.line_chart(chart)



