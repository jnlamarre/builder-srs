import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": ["cross_joins","cross_joins"],
    "exercise_name": ["beverages_and_food","sizes_and_trademarks"],
    "tables": [["beverages", "food_items"],["sizes", "trademarks"]],
    "last_reviewed": ["1980-01-01","1970-01-01"]
}
memory_state_df = pd.DataFrame(data)
con.execute("DROP TABLE IF EXISTS memory_state")
con.execute("CREATE TABLE memory_state AS SELECT * FROM memory_state_df")


# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------

CSV1 = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV1))
con.execute("DROP TABLE IF EXISTS beverages")
con.execute("CREATE TABLE beverages AS SELECT * FROM beverages")

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("DROP TABLE IF EXISTS food_items")
con.execute("CREATE TABLE food_items AS SELECT * FROM food_items")

CSV3 = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(CSV3))
con.execute("DROP TABLE IF EXISTS sizes")
con.execute("CREATE TABLE sizes AS SELECT * FROM sizes")

CSV4 = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(CSV4))
con.execute("DROP TABLE IF EXISTS trademarks")
con.execute("CREATE TABLE trademarks AS SELECT * FROM trademarks")

con.close()
