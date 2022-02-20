# API Automation Framework using Python
# Project Overview:
This is an api framework built on Python containing various sets of requests and mock responses.

## App package
The App package contains all request modules broken down per action.
The endpoint.py module serves as an url builder for the different requests

## Resources package
The Resources package contains all data for the different requests

## Tests package
The Tests package contains all tests for the different requests.
The tests are organized in two groups:
  - real
  - mocked

## Utilities package
The Utilities package contains a simple set of functions to return variations of the responses

# Installation Steps:
## From Github
  - Clone this repo
  - Go to https://github.com/zippote/automationPythonAPI
  - Click Code
  - Select HTTPS and copy the following url https://github.com/zippote/automationPythonAPI.git

- Steps on your local:
  - Create a destination folder in your local >> ie: myFolderExample in the C drive
  - Open cmd and move to that folder >> cd C:\myFolderExample
  - Type the following command: git clone https://github.com/zippote/automationPythonAPI.git
  - Hit enter and wait until the process is completed
  - Navigate to the project root folder cmd or IDE terminal
  - Create a new virtual env by running `py -m venv venv`
  - venv will be created under the root directory \venv\
  - To activate venv run `venv\Scripts\activate`
  - Run `pip install -r requirements.txt`

## From ZIP
  - Go to https://github.com/zippote/automationPythonAPI
  - Click Code
  - Select download zip
  - Extract the file to a folder of your choice, for example: C:\myFolder\automationPythonAPI
  - Open the repo with Pycharm or VS code (or any other IDE)

- Steps on your local:
  - Navigate to the project root folder cmd or IDE terminal, for example: C:\myFolder\automationPythonAPI
  - Create a new virtual env by running `py -m venv venv`
  - venv will be created under the root directory \venv\
  - To activate venv run `venv\Scripts\activate`
  - Run `pip install -r requirements.txt`

# RUNNING TESTS WITH PYTEST
## Run tests individually
`pytest -v -s`

## Run tests individually and add them to report
`pytest -v -s --alluredir=reports`


## To view allure report
1. Open cmd
2. `cd C:\path-to-repo-root\`
3. `allure serve reports`
4. Further reporting: Allure reports have Jenkins integration and can be included as part of any jenkins job.

### Happy testing.
