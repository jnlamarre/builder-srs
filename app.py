import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World!")
data = {"a": [1,2,3], "b": [4,5,6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.write("df")
    st.dataframe(df)

    sql_input = st.text_area(label="Query")
    st.write(f"Your answer: {sql_input}")
    result = duckdb.query(sql_input).df()

    st.dataframe(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)