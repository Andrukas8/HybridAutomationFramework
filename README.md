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
```pytest -v -s testCases\test_login.py --browser chrome``` - launches tests in test_login.py file. Supported browsers are Chrome, Firefox, Edge, Safari