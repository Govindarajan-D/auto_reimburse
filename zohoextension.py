from selenium import webdriver
import getpass
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)
driver.get('https://people.zoho.com/visualbisolutions/zp#reimbursement/form/add-formLinkName:Reimbursement_Form')

/** Fixed Values **/
invoice_amount = driver.find_element_by_name("Currency_11")
invoice_amount.clear()
invoice_amount.send_keys("1000")
from_date = driver.find_element_by_name("Claim_From")
from_date.clear()
from_date.send_keys("01-Jun-2019")
to_date = driver.find_element_by_name("Claim_To")
to_date.clear()
to_date.send_keys("30-Jun-2019")
invoice_date = driver.find_element_by_name("Date1")
invoice_date.clear()
invoice_date("5-Jun-2019")
description = driver.find_element_by_name("Description")
description.send_keys("Dummy")
final_amount = driver.find_element_by_name("Currency_1")
final_amount.clear()
final_amount.send_keys("1000")

/** Selectors **/
driver.find_element_by_xpath("//select[@name='Expense_Type']/option[text()='Phone & Internet']").click()
driver.find_element_by_xpath("//select[@name='Proof_Attached']/option[text()='No']").click()


