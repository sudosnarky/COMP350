Do `uv sync`.

Then `uv run python`.

When you `import ipl`, you'll get `ipl.matches` and `ipl.deliveries` 
as lists of structures. You're expected to implement the functions
for deriving some data out of these lists as given in the
`ipl_queries.py` file.

Subsequently, import the CSV data into a SQLite3 db using

`sqlite3 ipl.db < ipl.sql`

and write SQL queries to do the same tasks in `ipl_queries.py`.
