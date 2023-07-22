Python 3.10.8 (v3.10.8:aaaf517424, Oct 11 2022, 10:14:40) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
... from selenium.webdriver.chrome.service import Service
... from selenium.webdriver.common.by import By
... 
... 
... # 2 lines below is to use Google Chrome with selenium 4
... service = Service(executable_path='drivers/chromedriver')
... driver = webdriver.Chrome(service=service)
... 
... # to start Firefox use 2 lines below. Uncomment them and delete the previous code for Chrome
... #service = Service(executable_path='drivers/geckodriver')
... #driver = webdriver.Firefox(service=service)
... 
... 
... driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
... 
... driver.maximize_window()
... 
... logo = driver.find_element(by=By.XPATH, value="//img[@title='Brainbucket']")
... 
... new_registrant_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
... new_registrant_btn.click()
... 
... #Register Account
... #Personal Details
... firstname_field = driver.find_element(By.XPATH, "//fieldset/div[2]")
... firstname_field_class = firstname_field.get_attribute("class")
... assert "required" in firstname_field_class
... 
... firstname_input = driver.find_element(By.ID, "input-firstname")
... firstname_input.clear()
... firstname_input.send_keys("Iryna")
... 
... lastname_field = driver.find_element(By.XPATH, "//fieldset/div[3]")
... lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element(By.ID, "input-lastname")
lastname_input.clear()
lastname_input.send_keys("Zharkova")

email_field = driver.find_element(By.XPATH, "//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

email_input = driver.find_element(By.ID, "input-email")
email_input.clear()
email_input.send_keys("gorbatyk83@gmail.com")

telephone_field = driver.find_element(By.XPATH, "//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element(By.ID, "input-telephone")
telephone_input.clear()
telephone_input.send_keys("2246054057")

address_1_field = driver.find_element(By.XPATH, "//fieldset[2]/div[2]")
address_1_field_class = address_1_field.get_attribute("class")
assert "required" in address_1_field_class

address_1_input = driver.find_element(By.ID, "input-address-1")
address_1_input.clear()
address_1_input.send_keys("11 Oak Creek Dr")

city_field = driver.find_element(By.XPATH, "//fieldset[2]/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class

city_input = driver.find_element(By.ID, "input-city")
city_input.clear()
city_input.send_keys("Buffalo Grove")

country_field = driver.find_element(By.XPATH, "//fieldset[2]/div[6]")
country_field_class = country_field.get_attribute("class")
assert "required" in country_field_class

country_input = driver.find_element(By.ID, "input-country")
country_input.send_keys("United States")

zone_id_field = driver.find_element(By.XPATH, "//fieldset[2]/div[7]")
zone_id_field_class = zone_id_field.get_attribute("class")
assert "required" in zone_id_field_class

zone_id_input = driver.find_element(By.ID, "input-zone")
zone_id_input.send_keys("---None---")

password_field = driver.find_element(By.XPATH, "//fieldset[3]/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class

password_iput = driver.find_element(By.ID, "input-password")
password_iput.clear()
password_iput.send_keys("12345")

confirm_field = driver.find_element(By.XPATH, "//fieldset[3]/div[2]")
confirm_field_class = confirm_field.get_attribute("class")
assert "required" in confirm_field_class

confirm_input = driver.find_element(By.ID, "input-confirm")
confirm_input.clear()
confirm_input.send_keys("12345")

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 2 lines below is to use Google Chrome with selenium 4
service = Service(executable_path='drivers/chromedriver')
driver = webdriver.Chrome(service=service)

# to start Firefox use 2 lines below. Uncomment them and delete the previous code for Chrome
#service = Service(executable_path='drivers/geckodriver')
#driver = webdriver.Firefox(service=service)


driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

#Returning customers
email_field = driver.find_element(By.XPATH, "//form/div/input")
email_field_class = email_field.get_attribute("class")

email_input = driver.find_element(By.ID, "input-email")
email_input.clear()
email_input.send_keys("gorbatyk83@gmail.com")

password_field = driver.find_element(By.XPATH, "//form/div[2]/input")
password_field_class = password_field.get_attribute("class")

password_iput = driver.find_element(By.ID, "input-password")
password_iput.clear()
password_iput.send_keys("12345")

