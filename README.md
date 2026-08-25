# GitHub Machine Learning Repositories — Data Analytics Project

End-to-end analysis of popular Machine Learning repositories on GitHub:
popularity, programming languages, and activity.

## How to Run

```bash
pip install requests pandas matplotlib
python task1_data_collection.py      # -> github_projects.csv
python task2_sql_analysis.py         # -> github_projects.db + printed SQL results
python task2_visualize.py            # -> top10_repos.png, creation_trend.png
```

## Files

| File | Purpose |
|---|---|
| `task1_data_collection.py` | Collects, cleans, and saves data → `github_projects.csv` |
| `task2_sql_analysis.py` | Loads data into SQLite (`Repositories` table) and runs all required SQL queries |
| `task2_visualize.py` | Creates the two required charts |

## Step 8 (Task 2): Interpretation of Results

*(Fill this in after running the scripts — a few sentences per point)*

- **Most popular repositories:** which repos/owners dominate, and why they might be popular (framework vs. course vs. dataset repo, etc.)
- **Language trends:** which languages have the most ML repos, and whether that matches expectations (e.g. Python's dominance in ML)
- **Creation trend over time:** is repo creation increasing, peaking in a certain year, slowing down recently?
- **Any surprising finding** worth calling out.

## Task 3: Git & GitHub Publishing Steps

```bash
# Step 1: Initialize the repository
git init
git status

# Step 2: Stage the files
git add .
git status

# Step 3: First commit
git commit -m "Initial commit: GitHub ML repos data analytics project"

# Step 4: Create a new (empty) repository on GitHub via the web UI first,
# then copy its URL, e.g. https://github.com/<your-username>/<repo-name>.git

# Step 5: Connect and push
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

Take screenshots after each of these commands (init, status, add, commit,
remote add, push) as required evidence for Step 6.

## Task 3, Step 7: Ethics Reflection

**Why is it important to verify data collected from public APIs?**
Public APIs return data exactly as stored on the platform at that moment,
which can include errors, outdated fields, or incomplete records (for
example, a missing license or language). Verifying the data — checking
for nulls, duplicates, and unreasonable values — ensures that any
analysis or decision built on top of it reflects reality rather than
an artifact of bad data.

**Why should data analysts document the source of their data?**
Documenting the source (the exact API endpoint, query parameters, and
date of collection) makes the analysis reproducible and auditable.
Anyone reviewing the work can trace conclusions back to where the
numbers came from, understand what was and wasn't included (e.g. only
the top 100 repos sorted by stars), and judge whether the data is still
relevant if it's queried again later, since GitHub data changes
constantly.

**How can missing or inaccurate data affect data analysis and
decision-making?**
Missing or inaccurate data can silently bias results — for example, if
repositories without a listed language are dropped instead of labeled
"Unknown," the language-popularity analysis would understate diversity.
Decisions made on flawed data (like a company assuming a certain
language dominates the ML ecosystem when the analysis simply failed to
capture some repos) can misdirect resources, strategy, or product
decisions built on that assumption.

## Responsible Use of Public Data

This project only collects public, non-personal repository metadata
available through GitHub's official API (stars, forks, language,
license, dates). No private repository content or personal user data is
collected. This work is for educational purposes as part of a data
analytics course.
