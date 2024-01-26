Hybrid Automation Framework Based on Selenium with Python
as inspired by SDET-QA Youtube channel

### Technologies
* Selenium: Selenium Libraries
* PyTest: Python UnitTest framework
* pytest-html: PyTest HTML Reports
* pytest-xdist: Run Tests in Parallel
* Openpyxl: MS Excel Support
* Allure-pytest: to generate allure reports

### Folder Structure
* pageObjects (Package)
* testCases (Package)
* utilities (Package)
* TestData (Folder)
* Configurations (Folder)
* Logs (Folder)
* Screenshots (Folder)
* Reports (Folder)
* Run.bat

### Demo application
|            Frontend                 |                Backend                                          |
|-------------------------------------|-----------------------------------------------------------------|
| https://www.nopcommerce.com/en/demo | https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F  |


### Tips
```pytest -v -s testCases\test_login.py``` - launches tests in test_login.py file in default browser (Chrome);
```pytest -v -s testCases\test_login.py --browser firefox``` - in a selected browser (supported: Chrome, Firefox, Edge, Safari);
```pytest -v -s -n=3 testCases\test_login.py``` - "-n=3" allows to launch tests in parallel (keep it under 3 for);
```pytest -v -s --html=Reports\report.html testCases\test_login.py``` - generates the HTML report in "Reports\report.html";