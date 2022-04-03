from selenium import webdriver
import time

brave="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

web = webdriver.Chrome()
web.get("http://172.16.1.1:8090/httpclient.html?u=http://www.gstatic.com/generate_204")

time.sleep(2)
user='username'
user_path=web.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
user_path.send_keys(user)

passwd='pwd'
passwd_path=web.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/input[2]')
passwd_path.send_keys(passwd)

login = web.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]")
login.click()

