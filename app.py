import streamlit as st
import pandas as pd
import duckdb
import io


csv1 = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(csv1))

csv2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
"""
food_prices = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_prices
"""

solution = duckdb.sql(answer).df()

st.header("Enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_prices")
    st.dataframe(food_prices)
    st.write("expected")
    st.dataframe(solution)

with tab3:
    st.write(answer)