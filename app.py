# pylint: disable=missing-module-docstring
import logging
import os
import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercises_tables.duckdb", read_only=False)

if "data" not in os.listdir():
    print("create folder data")
    logging.error(os.listdir())
    logging.error("create folder data")
    os.mkdir("data")

if "exercises_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

with st.sidebar:
    theme = st.selectbox(
        "What would you like to revise?",
        ("cross_joins", "GroupBy", "window_functions"),
        index=None,
        placeholder="Selected theme...",
    )

    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df().sort_values("last_reviewed")
    st.write(exercise)

    exercise_name = exercise.iloc[0]["exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("Your Solution:")
query = st.text_area(label="Your Query was:", key="user_input")

if query:
    result = con.execute(query).df()
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
    exercise_tables = exercise.iloc[0]["tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    st.text(answer)
