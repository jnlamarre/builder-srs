# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

CSV1 = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV1))

CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
"""
food_prices = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_prices
"""

solution_df = duckdb.sql(ANSWER_STR).df()


with st.sidebar:
    option = st.selectbox(
        "What would you like to revise?",
        ("Joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Selected theme...",
    )

    st.write("You selected:", option)


st.header("Your Solution:")
query = st.text_area(label="Your Query was:", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"Result has a {n_lines_difference} line differences with the solution"
        )


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_prices")
    st.dataframe(food_prices)
    st.write("expected")
    st.dataframe(solution_df)

with tab3:
    st.write(ANSWER_STR)
