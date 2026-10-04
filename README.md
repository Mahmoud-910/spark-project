PySpark Data Cleaning Project

1. Project Description

This project implements a PySpark data cleaning function and tests it automatically using GitHub Actions.

2. Project Structure

Plain Text


spark-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyspark_job.py
├── test_pyspark_job.py
├── requirements.txt
└── README.md



3. Functionality

The clean_data function:

•
Removes rows where amount <= 0.

•
Removes rows where name is NULL.

•
Adds the amount_with_tax column.

•
Calculates amount_with_tax as amount * 1.20.

4. Requirements

The project uses:

Plain Text


pyspark==3.5.6
pytest==8.4.2



Java 17 and Python 3.11 are used in GitHub Actions.

5. Run the Project Locally

Create a virtual environment

Bash


python3 -m venv .venv
source .venv/bin/activate



Install the dependencies

Bash


python -m pip install --upgrade pip
python -m pip install -r requirements.txt



Run the tests

Bash


python -m pytest -v



6. Expected Test Result

Plain Text


4 passed



7. GitHub Actions

The GitHub Actions workflow is located at:

Plain Text


.github/workflows/ci.yml



The workflow runs automatically when a Pull Request is:

•
Opened.

•
Updated.

•
Reopened.

The workflow installs the dependencies and runs all PySpark tests.

8. Branches

The project uses these branches:

Plain Text


main
test-pyspark-ci



The Pull Request is created from test-pyspark-ci to main.

9. Final Result

The project is complete when the GitHub Actions workflow finishes successfully and the test output shows:

Plain Text


4 passed



