"""
Task 2 - Store & Analyze the Data (Steps 1-6)
================================================
Loads github_projects.csv into a SQLite database (table: Repositories)
and runs the required SQL queries.
"""

import pandas as pd
import sqlite3

# ---------------------------------------------------------------
# Step 1: Create the SQLite Database
# ---------------------------------------------------------------
df = pd.read_csv("github_projects.csv", parse_dates=["created_date", "updated_date"])

conn = sqlite3.connect("github_projects.db")
df.to_sql("Repositories", conn, if_exists="replace", index=False)
print("Loaded", len(df), "rows into the Repositories table\n")


def run(title, sql):
    print("=" * 70)
    print(title)
    print("=" * 70)
    result = pd.read_sql(sql, conn)
    print(result.to_string(index=False))
    print()
    return result


# ---------------------------------------------------------------
# Step 2: Filtering & Searching Queries
# ---------------------------------------------------------------
run(
    "Repositories with more than 10,000 stars",
    "SELECT name, owner, stars FROM Repositories WHERE stars > 10000 ORDER BY stars DESC;"
)

run(
    'Repositories whose name contains the word "Machine"',
    "SELECT name, owner, stars FROM Repositories WHERE name LIKE '%Machine%';"
)

# ---------------------------------------------------------------
# Step 3: Logical Operators (AND, OR, NOT)
# ---------------------------------------------------------------
run(
    "AND example: Python repos with more than 5,000 stars",
    "SELECT name, language, stars FROM Repositories "
    "WHERE language = 'Python' AND stars > 5000 ORDER BY stars DESC;"
)

run(
    "OR example: repos written in Python OR Jupyter Notebook",
    "SELECT name, language, stars FROM Repositories "
    "WHERE language = 'Python' OR language = 'Jupyter Notebook' ORDER BY stars DESC;"
)

run(
    "NOT example: repos that are NOT written in Python",
    "SELECT name, language, stars FROM Repositories WHERE NOT language = 'Python' ORDER BY stars DESC;"
)

# ---------------------------------------------------------------
# Step 4: Sorting & Limiting Queries
# ---------------------------------------------------------------
run(
    "Top 10 repositories by stars",
    "SELECT name, owner, language, stars FROM Repositories ORDER BY stars DESC LIMIT 10;"
)

# ---------------------------------------------------------------
# Step 5: Aggregate Functions
# ---------------------------------------------------------------
run(
    "Total number of repositories and average stars",
    "SELECT COUNT(*) AS total_repos, ROUND(AVG(stars), 0) AS avg_stars FROM Repositories;"
)

# ---------------------------------------------------------------
# Step 6: Grouping Analysis
# ---------------------------------------------------------------
run(
    "Languages with more than 5 repositories",
    "SELECT language, COUNT(*) AS repo_count FROM Repositories "
    "GROUP BY language HAVING COUNT(*) > 5 ORDER BY repo_count DESC;"
)

conn.close()
