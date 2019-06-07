from selenium import webdriver
import getpass
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)
driver.get('https://people.zoho.com/visualbisolutions/zp#reimbursement/form/add-formLinkName:Reimbursement_Form')
invoice_amount = driver.find_element_by_id("zp_field_249048000002801079")
invoice_amount = driver.find_element_by_name("Currency_11")
invoice_amount.clear()
invoice_amount.send_keys("1000")
from_date = driver.find_element_by_id("zp_field_249048000003005331")
from_date = driver.find_element_by_name("Claim_From")
from_date.clear()
from_date.send_keys("01-Jun-2019")
to_date = driver.find_element_by_name("Claim_To")
to_date.clear()
to_date.send_keys("30-Jun-2019")
invoice_date = driver.find_element_by_name("Date1")
invoice_date.clear()
invoice_date("5-Jun-2019")
// expense_type = driver.find_element_by_id("s2id_zp_field_249048000002801091")
expense_type = driver.find_element_by_name("Expense_Type")
driver.find_element_by_xpath("//select[@name='Expense_Type']/option[text()='Phone & Internet']").click()
description = driver.find_element_by_name("Description")
description.send_keys("Dummy")
final_amount = driver.find_element_by_name("Currency_1")
final_amount.clear()
final_amount.send_keys("1000")
upload_file = driver.find_element_by_name("filename")
click_upload = driver.find_element_by_name("Proof_Attachement_zip")
click_upload.send_keys("C:/Users/ramgopalanv/Desktop/iOS_Developer_Guide.pdf")

//proof_attached = driver.find_element_by_name("Proof_Attached")

driver.find_element_by_xpath("//select[@name='Expense_Type']/option[text()='Phone & Internet']").click()
driver.find_element_by_xpath("//select[@name='Proof_Attached']/option[text()='No']").click()

from pywinauto.application import Application
app = Application.start("notepad.exe")
app.UntitledNotepad.TypeKeys("%FX")
app.UntitledNotepad.type_keys("%FX")





driver.get("https://www.gmail.com")


driver = webdriver.Chrome("C:/Users/ramgopalanv/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome("C:/Users/ramgopalanv/Downloads/chromedriver_win32/chromedriver.exe")




driver.get(https://people.zoho.com/visualbisolutions/zp)


from selenium import webdriver
import getpass
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)
driver.get(https://people.zoho.com/visualbisolutions/zp#reimbursement/form/listview-formId:249048000002801059/viewId:249048000002801061)
driver.get('https://people.zoho.com/visualbisolutions/zp#reimbursement/form/add-formLinkName:Reimbursement_Form')

<input fieldtype="6" onchange="ZPForm.Field.closeconfmsg(true)" id="zp_field_249048000002801079" type="text" 
caltype="popup" name="Currency_11" class="form-control zptxt-edit" value="1000.00">

driver.FindElement(By.Id("zp_field_249048000002801079")).SendKeys("1000");




6th June Modifications:
installed : pip install pywinauto==0.5.4
app = pywinauto.application.Application()
    mainWindow = app['Open'] # main windows' title
    ctrl=mainWindow['Edit'] 
	 ctrl.ClickInput()
    ctrl.TypeKeys('dummy.txt')
    ctrlBis = mainWindow['Open'] # open file button
    ctrlBis.ClickInput()