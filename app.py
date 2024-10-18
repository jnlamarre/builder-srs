# pylint: disable=missing-module-docstring

import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect(database="data/exercises_tables.duckdb", read_only=False)

# ANSWER_STR = """
# SELECT * FROM beverages
# CROSS JOIN food_prices
# """

# solution_df = duckdb.sql(ANSWER_STR).df()


with st.sidebar:
    theme = st.selectbox(
        "What would you like to revise?",
        ("cross_joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Selected theme...",
    )

    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
    st.write(exercise)

st.header("Your Solution:")
query = st.text_area(label="Your Query was:", key="user_input")

# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)
#
#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Some columns are missing")
#
#     n_lines_difference = result.shape[0] - solution_df.shape[0]
#     if n_lines_difference != 0:
#         st.write(
#             f"Result has a {n_lines_difference} line differences with the solution"
#         )
#
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_prices")
#     st.dataframe(food_prices)
#     st.write("expected")
#     st.dataframe(solution_df)
#
# with tab3:
#     st.write(ANSWER_STR)
