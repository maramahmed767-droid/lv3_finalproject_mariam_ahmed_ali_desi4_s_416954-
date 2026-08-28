
import pandas as pd

import sqlite3

import matplotlib.pyplot as plt

# import sqlite3, pandas, and matplotlib.pyplot libraries to create a SQLite database,
#  perform SQL queries on the dataset, and visualize the results

conn = sqlite3.connect("github_projects.db")
# Create a connection to the SQLite database named "github_projects.db"

df = pd.read_sql("SELECT * FROM Repositories", conn, parse_dates=["created_date", "updated_date"])
# Load the data from the "Repositories" table in the SQLite database into a DataFrame

conn.close()
# Close the connection to the SQLite database after loading the data into the DataFrame

# 1. Most popular repositories (Top 10 by stars)

top10 = df.nlargest(10, "stars").sort_values("stars")
# Create a DataFrame containing the top 10 repositories by stars, sorted in ascending order for better visualization

plt.figure(figsize=(10, 6))
# Create a new figure for the bar chart with specified dimensions

plt.barh(top10["name"], top10["stars"], color="steelblue")
# Create a horizontal bar chart with repository names on the y-axis and star counts on the x-axis,
#  using a steel blue color for the bars

plt.xlabel("Stars")
# Set the label for the x-axis to "Stars"

plt.ylabel("Repository")
# Set the label for the y-axis to "Repository"

plt.title("Top 10 Most Popular ML Repositories")
# Set the title of the bar chart to "Top 10 Most Popular ML Repositories"

plt.tight_layout()
# Adjust the layout of the plot to ensure that all elements fit within the figure area

plt.savefig("top10_repos.png", dpi=150)
# Save the bar chart as a PNG file named "top10_repos.png" with a resolution of 150 dots per inch (DPI)

plt.close()
# Close the current figure to free up memory and avoid displaying it in an interactive environment

# 2. Repository creation trends over time

df["created_year"] = df["created_date"].dt.year
# Extract the year from the "created_date" column and create a new column "created_year" in the DataFrame

by_year = df.groupby("created_year").size()
# Group the DataFrame by "created_year" and count the number of repositories created each year, 
# storing the result in a new Series called "by_year"

plt.figure(figsize=(10, 6))
# Create a new figure for the line plot with specified dimensions

plt.plot(by_year.index, by_year.values, marker="o", color="darkorange")
# Create a line plot with years on the x-axis and the number of repositories created on the y-axis,
#  using circular markers and a dark orange color for the line

plt.xlabel("Year")
# Set the label for the x-axis to "Year"

plt.ylabel("Number of Repositories Created")
# Set the label for the y-axis to "Number of Repositories Created"

plt.title("ML Repository Creation Trend Over Time")
# Set the title of the line plot to "ML Repository Creation Trend Over Time"

plt.tight_layout()
# Adjust the layout of the plot to ensure that all elements fit within the figure area

plt.savefig("creation_trend.png", dpi=150)
# Save the line plot as a PNG file named "creation_trend.png" with a resolution of 150 dots per inch (DPI)

plt.close()
# Close the current figure to free up memory and avoid displaying it in an interactive environment

print("Saved top10_repos.png and creation_trend.png")
# Print a message indicating that the visualizations have been saved as PNG files