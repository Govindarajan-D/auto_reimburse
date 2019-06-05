from selenium import webdriver
import getpass
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://www.gmail.com")