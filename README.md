# UI & API automation tests with Python

Simple UI and API automation tests with Python

## Getting Started

Import the project in your IDE, resolve the dependencies by downloading the necessary libraries and you should be good to go.
I used PyCharm as IDE. Make sure to install Gherkin, Cucumber and Selenium plugins.

## Running the tests

### UI Tests

For the UI tests you will need to install `behave` and `allure-behave` packages (allure is a tool for reporting).
To run the ui tests you can either right-click the feature file or a specific scenarion from the
feature file and then press Run.

If you want to get a report of the run with screenshots then run the below from the IDE terminal:

behave -f allure_behave.formatter:AllureFormatter -o reports/ .\uitests\features\LoginPageScenarios.feature
For single scenario add `-n '<Scenario name>'` at the end of the above command

After that run: allure serve reports/. You should be redirected to the browser and you should be seeing
the ALlure report along with screenshots attached. Feel free to modify any locators to a test and observe
the screenshot being taken.

###API tests

For the API tests make sure to install `nose` package. After that, just right click on any of the py files
under /apitests and then Run.

## Authors

* **Angelos Ladopoulos**

## Licence

This project is not licenced
