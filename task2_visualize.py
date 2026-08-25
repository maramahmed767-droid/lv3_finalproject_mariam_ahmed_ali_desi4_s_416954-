"""
Task 2 - Step 7: Create Python Visualizations
================================================
Two required charts:
1. Most popular repositories (bar chart)
2. Repository creation trends over time (line chart)
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("github_projects.db")
df = pd.read_sql("SELECT * FROM Repositories", conn, parse_dates=["created_date", "updated_date"])
conn.close()

# 1. Most popular repositories (Top 10 by stars)
top10 = df.nlargest(10, "stars").sort_values("stars")
plt.figure(figsize=(10, 6))
plt.barh(top10["name"], top10["stars"], color="steelblue")
plt.xlabel("Stars")
plt.ylabel("Repository")
plt.title("Top 10 Most Popular ML Repositories")
plt.tight_layout()
plt.savefig("top10_repos.png", dpi=150)
plt.close()

# 2. Repository creation trends over time
df["created_year"] = df["created_date"].dt.year
by_year = df.groupby("created_year").size()

plt.figure(figsize=(10, 6))
plt.plot(by_year.index, by_year.values, marker="o", color="darkorange")
plt.xlabel("Year")
plt.ylabel("Number of Repositories Created")
plt.title("ML Repository Creation Trend Over Time")
plt.tight_layout()
plt.savefig("creation_trend.png", dpi=150)
plt.close()

print("Saved top10_repos.png and creation_trend.png")
