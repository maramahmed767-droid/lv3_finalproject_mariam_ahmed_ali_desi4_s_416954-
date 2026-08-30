# GitHub Machine Learning Repositories — Data Analytics Project

End-to-end analysis of popular Machine Learning repositories on GitHub:
popularity, programming languages, and activity.

## How to Run

```bash
pip install -r requirements.txt
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
| `requirements.txt` | Python dependencies |

## Data Scope / Limitation

The GitHub Search API returns at most 100 results per page. This dataset
is the **top 100 most-starred repositories matching "machine learning"**
at the time of collection - not every ML repository on GitHub. It is a
sample biased toward large, already-popular projects, so findings below
describe this sample, not the full ML ecosystem on GitHub.

## Task 2, Step 8: Interpretation of Results

**Most popular repositories:** `tensorflow` (197,616 stars) and
`transformers` (164,423 stars) lead by a wide margin over the rest of
the top 10 (the third-place `ML-For-Beginners` has under 90,000). Both
are backed by major organizations (Google and Hugging Face), which
explains their scale - large corporate backing, long project history,
and being foundational infrastructure that thousands of other projects
depend on all drive sustained star growth. Several other top-10 entries
(`awesome-machine-learning`, `500-AI-Machine-learning-...`) are
curated "awesome list" repositories rather than actual code frameworks,
showing that popularity in this sample reflects both usefulness as a
tool and usefulness as a learning/reference resource.

**Language trends:** Python dominates with 30 of the 100 repositories,
followed by "Unknown" (23 - repos with no primary language detected,
often documentation-only or awesome-list repos) and Jupyter Notebook
(19). Together Python and Jupyter Notebook account for about half the
dataset, which matches the expectation that Python is the de facto
standard language for machine learning tooling and experimentation.
C++ (12) appears mostly in performance-critical libraries (e.g. core
ML frameworks with C++ backends).

**Creation trend over time:** Repository creation rises steadily from
2009, accelerates sharply from 2014 onward, and peaks in 2018 (18 new
repos in this sample), coinciding with the height of the deep-learning
boom and mainstream adoption of frameworks like TensorFlow and PyTorch.
Creation counts drop off after 2018 and continue declining through 2024.
This does not necessarily mean ML repository creation is slowing down
overall - it more likely reflects that this sample only contains
repositories that have already accumulated enough stars to rank in the
top 100, and newer repositories haven't had time to accumulate as many
stars yet (a form of survivorship/recency bias in star-sorted data).

**Surprising finding:** Almost a quarter of the top 100 repositories
have no detected primary language ("Unknown"). This is a reminder that
"top starred" does not mean "actively maintained code" - a meaningful
share of highly-starred ML repositories are curated lists, datasets, or
documentation rather than software projects.

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
git remote add origin https://github.com/maramahmed767-droid/lv3_finalproject_mariam_ahmed_ali_desi4_s_416954-.git
git branch -M main
git push -u origin main
```

Take a screenshot after each of these commands (init, status, add, commit,
remote add, push) — these are the required evidence for Step 6, and they
cannot be generated for you; they must show your own terminal and your
own GitHub repository.

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

## Step 8 (Task 2): Interpretation of Results

    Most popular repositories:
    The top-starred repository in the dataset is tensorflow by tensorflow with 197,616 stars, followed by transformers by huggingface (164,423 stars). Frameworks, deep learning libraries, and comprehensive learning repositories (like ML-For-Beginners) dominate the highest star counts because they serve as essential foundational tools for the global developer community.

    Language trends:
    Python is the undisputed dominant programming language in Machine Learning, representing the majority of primary repositories (30 repos), followed by Jupyter Notebooks (19 repos) and C++ (12 repos). C++ is typically chosen for high-performance low-level implementations and inference engines (such as TensorFlow core), while Python and Jupyter Notebooks lead in accessibility, experimentation, and rapid prototyping.

    Creation trend over time:
    Machine Learning repository creation experienced massive growth starting around 2014, reaching its historical peak between 2016 and 2018 (with 18 repositories created in 2018 alone). After 2018, the creation rate of new top-starred repos slowed down, indicating that the core ML ecosystem became consolidated around established, long-standing open-source projects.

    Surprising finding:
Several of the top-starred repositories are not tools or libraries at all, but curated educational/reference lists — such as ML-For-Beginners, awesome-machine-learning, and funNLP. This shows that a large part of what developers search for and star in the ML space is learning material and curated resources, not just production-ready code.
