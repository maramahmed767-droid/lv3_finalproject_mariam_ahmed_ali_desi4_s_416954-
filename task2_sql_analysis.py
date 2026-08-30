
import pandas as pd

import sqlite3

# import sqlite3 & pandas libraries to create a SQLite database and perform SQL queries on the dataset

df = pd.read_csv("github_projects.csv", parse_dates=["created_date", "updated_date"])
# Load the cleaned dataset from the CSV file into a DataFrame and parse the date columns

conn = sqlite3.connect("github_projects.db")
# Create a connection to a SQLite database named "github_projects.db"

df.to_sql("Repositories", conn, if_exists="replace", index=False)
# Save the DataFrame to a table named "Repositories" in the SQLite database, replacing it if it already exists, and without including the index

print("Loaded", len(df), "rows into the Repositories table\n")
# Print the number of rows loaded into the Repositories table


def run(title, sql):
    print("=" * 70) # Print a separator line for better readability

    print(title) # Print the title of the SQL query being executed

    print("=" * 70) # Print another separator line

    result = pd.read_sql(sql, conn) # Execute the SQL query on the SQLite database and store the result in a DataFrame

    print(result.to_string(index=False)) # Print the result of the SQL query in a formatted manner without the index

    print() # Print an empty line for better readability

    return result # Return the result of the SQL query as a DataFrame

# Define a function named "run" that takes a title and an SQL query as arguments,
# executes the query on the SQLite database, and prints the results in a formatted manner


run(
    "Repositories with more than 10,000 stars",
    "SELECT name, owner, stars FROM Repositories WHERE stars > 10000 ORDER BY stars DESC;"
)# Execute the "run" function with a title and an SQL query to retrieve repositories with more than 10,000 stars,
#  ordered by stars in descending order

run(
    'Repositories whose name contains the word "Machine"',
    "SELECT name, owner, stars FROM Repositories WHERE name LIKE '%Machine%';"
)# Execute the "run" function with a title and an SQL query to retrieve
#  repositories whose name contains the word "Machine"


run(
    "AND example: Python repos with more than 5,000 stars",
    "SELECT name, language, stars FROM Repositories "
    "WHERE language = 'Python' AND stars > 5000 ORDER BY stars DESC;"
)# Execute the "run" function with a title and an SQL query to retrieve 
#  Python repositories with more than 5,000 stars,

run(
    "OR example: repos written in Python OR Jupyter Notebook",
    "SELECT name, language, stars FROM Repositories "
    "WHERE language = 'Python' OR language = 'Jupyter Notebook' ORDER BY stars DESC;"
)# Execute the "run" function with a title and an SQL query to retrieve
#  repositories written in Python or Jupyter Notebook, ordered by stars in descending order

run(
    "NOT example: repos that are NOT written in Python",
    "SELECT name, language, stars FROM Repositories WHERE NOT language = 'Python' ORDER BY stars DESC;"
)# Execute the "run" function with a title and an SQL query to retrieve
#  repositories that are not written in Python, ordered by stars in descending order


run(
    "Top 10 repositories by stars",
    "SELECT name, owner, language, stars FROM Repositories ORDER BY stars DESC LIMIT 10;"
)# Execute the "run" function with a title and an SQL query to retrieve
#  the top 10 repositories by stars, ordered in descending order


run(
    "Total number of repositories and average stars",
    "SELECT COUNT(*) AS total_repos, ROUND(AVG(stars), 0) AS avg_stars FROM Repositories;"
)# Execute the "run" function with a title and an SQL query to retrieve 


run(
    "Languages with more than 5 repositories",
    "SELECT language, COUNT(*) AS repo_count FROM Repositories "
    "GROUP BY language HAVING COUNT(*) > 5 ORDER BY repo_count DESC;"
)# Execute the "run" function with a title and an SQL query to retrieve
#  languages with more than 5 repositories, grouped by language and ordered by repository count in

conn.close() 
# Close the connection to the SQLite database after executing all queries
