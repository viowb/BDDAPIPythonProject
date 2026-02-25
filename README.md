# BDD API Python Project

This repository demonstrates a Behavior-Driven Development (BDD) test automation setup for APIs using **Python** and the **behave** framework.

📘 BDD (Behavior-Driven Development) lets you write tests in **natural language** using the **Gherkin** syntax (`Given`, `When`, `Then`), improving readability and collaboration between technical and non-technical team members.:contentReference[oaicite:1]{index=1}

---

## 🚀 Project Overview

This BDD project is structured to:

- Organize executable specifications using Gherkin `.feature` files
- Implement step definitions in Python
- Run API tests using behave
- Be easy to extend for larger API test suites

Features included:

✔ Example feature file for an API  
✔ Corresponding step definition file  
✔ Standard Python project layout

---

## 📁 Project Structure

BDDAPIPythonProject/
├── features/ # All BDD features live here
│ ├── steps/ # Step definition modules
│ │ └── book_steps.py
│ └── BookAPI.feature
├── .venv/ # Virtual environment
├── requirements.txt # Python dependencies
└── README.md # This documentation



---

## 💡 Prerequisites

Before running tests, make sure you have:

✅ Python 3.8+ installed  
✅ A terminal or IDE (e.g., PyCharm) with Python support

---

## 🛠 Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/viowb/BDDAPIPythonProject.git
   cd BDDAPIPythonProject

   Create a Python virtual environment (Windows example):

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install behave


🧪 Running the Tests
🔹 From the Command Line

Simply run:

behave


This will execute all feature files under the features/ directory.

🔹 From PyCharm

If you’re using PyCharm Professional:

Right-click the features/ folder → Mark Directory As → Test Sources Root

Go to Run → Edit Configurations

Click the + icon and choose Behave

Set Feature files/folder to features/

Run the configuration

🧬 Example Feature & Steps

Here’s a sample Gherkin feature:

Feature: Add books to the library

  Scenario: Add a book successfully
    Given the Book details which needs to be added to library
    When the Book details are sent to the API
    Then the book should be added to the library


And its step definitions:

from behave import given, when, then

@given('the Book details which needs to be added to library')
def given_book_details(context):
    context.book = {"title":"Sample Book", "author":"Author Name"}

@when('the Book details are sent to the API')
def when_send_book_details(context):
    # TODO: send API request
    context.response = {"status":"success"}

@then('the book should be added to the library')
def then_book_added(context):
    assert context.response.get("status") == "success"

    🛠 Customizing For Your API

To adapt this project to your API:

Update the .feature scenarios to match your endpoints

Modify the step definitions with real HTTP requests (e.g., using requests)

Add more feature files for additional workflows

📘 Learn More

behave official docs: https://behave.readthedocs.io/en/latest/

Gherkin syntax guide

BDD best practices

📄 License

This project is open source and available for learning and extension.
