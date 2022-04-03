from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driverz = webdriver.Chrome(ChromeDriverManager().install())



chrome="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
brave="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

driver = webdriver.Chrome("C:\\Users\\cools\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe")

driver.get("http://172.16.1.1:8090/httpclient.html?u=http://www.gstatic.com/generate_204")
print(driver.title)



