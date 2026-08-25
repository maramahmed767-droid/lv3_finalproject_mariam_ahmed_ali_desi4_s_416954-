
import requests

import pandas as pd

# import request & pandas libraries to collect data from the GitHub API and create a dataset

url = "https://api.github.com/search/repositories?q=machine+learning&sort=stars&order=desc&per_page=100"

#get the top 100 most starred machine learning repositories from GitHub API

response = requests.get(url)
 # send a GET request to the GitHub API to retrieve the data

response.raise_for_status() 
 # stop early with a clear error if the request failed

data = response.json()
# Extract the list of repository objects

items = data["items"]  
# the list of repository objects

print(f"Retrieved {len(items)} repositories from the API")
# 

df = pd.DataFrame(items) 
# create a DataFrame from the list of repository objects

print("\nInitial shape:", df.shape) 
# Display the initial shape of the DataFrame

print(df.info()) 
 # Display the DataFrame information to understand its structure and data types

columns_needed = [
    "name", "owner", "language", "stargazers_count", "forks_count",
    "watchers_count", "open_issues_count", "created_at", "updated_at", "license"
] # list of columns that are needed for the analysis

df = df[columns_needed]
 # Select only the required columns from the DataFrame


df["owner"] = df["owner"].apply(lambda x: x["login"] if isinstance(x, dict) else None) 
# Extract the login name from the owner object

df["license"] = df["license"].apply(lambda x: x["name"] if isinstance(x, dict) else None) 
# Extract the license name from the license object


print("\nMissing values before handling:")

print(df.isna().sum()) 
# Display the number of missing values in each column

df["language"] = df["language"].fillna("Unknown")
# Fill missing values in the "language" column with "Unknown"

df["license"] = df["license"].fillna("No license")
#  Fill missing values in the "license" column with "No license"


print("\nDuplicate rows found:", df.duplicated().sum())
# Display the number of duplicate rows

df = df.drop_duplicates()
# Drop duplicate rows from the DataFrame



df["created_at"] = pd.to_datetime(df["created_at"])
# Convert the "created_at" column to datetime format

df["updated_at"] = pd.to_datetime(df["updated_at"])
# Convert the "updated_at" column to datetime format

df = df.rename(columns={
    "stargazers_count": "stars",
    "forks_count": "forks",
    "watchers_count": "watchers",
    "open_issues_count": "open_issues",
    "created_at": "created_date",
    "updated_at": "updated_date",
})# Rename columns for better readability and consistency

df = df.reset_index(drop=True)
# Reset the index of the DataFrame after dropping duplicates

df.to_csv("github_projects.csv", index=False)
# Save the cleaned DataFrame to a CSV file without the index

print("\nSaved github_projects.csv")

check = pd.read_csv("github_projects.csv")
# Reload the DataFrame from the CSV file

print("\nReloaded shape:", check.shape)
# Display the shape of the reloaded DataFrame

print(check.head())
# Display the first few rows of the reloaded DataFrame