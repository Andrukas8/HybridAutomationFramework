import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import XLUtils

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

#"https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
driver.get("https://cleartax.in/s/fd-calculator")
driver.maximize_window()

file = os.getcwd() + "\\CalcData.xlsx"
rows = XLUtils.getRowCount(file,"Data")

for r in range(2,rows + 1):
    totalInv = XLUtils.readData(file, "Data", r, 1)
    rateOfInt = XLUtils.readData(file, "Data", r, 2)
    tPerYear = XLUtils.readData(file, "Data", r, 3)
    tPerMonth = XLUtils.readData(file, "Data", r, 4)
    compPeriod = XLUtils.readData(file, "Data", r, 5)
    matAmount = XLUtils.readData(file, "Data", r, 6)

    totalInvUI = driver.find_element(By.XPATH, "//input[@id='input_Total Investment']")
    totalInvUI.clear()
    totalInvUI.send_keys(totalInv)

    rateOfIntUI = driver.find_element(By.XPATH, "//input[@id='input_Rate of interest (p.a)']")
    rateOfIntUI.clear()
    rateOfIntUI.send_keys(rateOfInt)

    tPerYearUI = driver.find_element(By.XPATH, "//input[@id='timeinput-years']")
    tPerYearUI.clear()
    tPerYearUI.send_keys(tPerYear)

    tPerMonthUI = driver.find_element(By.XPATH, "//input[@id='timeinput-months']")
    tPerMonthUI.clear()
    tPerMonthUI.send_keys(tPerMonth)

    compPeriodUI_ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[1]/div[1]/div[1]/div[4]/div/div[2]/select")
    compPeriodUI = Select(compPeriodUI_ele)
    compPeriodUI.select_by_visible_text(compPeriod)

    matAmountCalc = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]").text
    matAmountCalc = matAmountCalc[1:]

    res = "Failed"


    if matAmountCalc == matAmount:
        res = "Passed"
        XLUtils.fillGreenColor(file, "Data", r, 8)
    else:
        res = "Failed"
        XLUtils.fillRedColor(file, "Data", r, 8)


    XLUtils.writeData(file, "Data", r, 8, res)

    print(matAmountCalc, matAmount, res)











