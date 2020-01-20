from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'https://cufs.vulcan.net.pl/wierzbicapowiatradomski/Account/LogOn?ReturnUrl=%2Fwierzbicapowiatradomski%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fwierzbicapowiatradomski%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fwierzbicapowiatradomski%252fLoginEndpoint.aspx'

with open(r'C:\Users\Kamil\Desktop\chrome\login.txt', 'r') as f:
    file_text = f.read().split(',')
    EMAIL = file_text[0]
    PASSWORD = file_text[1]

browser = webdriver.Chrome(executable_path=r'C:\Users\Kamil\Desktop\chrome\chromedriver.exe')
browser.get(URL)

email_input = browser.find_element_by_id('LoginName')
email_input.send_keys(EMAIL)

password_input = browser.find_element_by_id('Password')
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

grade_btn = browser.find_element_by_css_selector("a[href*='https://uonetplus-opiekun.vulcan.net.pl/wierzbicapowiatradomski/020784/Start/Index/']")
grade_btn.click()