from selenium.webdriver.common.by import By

class TextInput:
    def __init__(self, driver):
        self.driver = driver
    def open_url(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def input_text(self, name, email, phone, address):
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "phone").send_keys(phone)
        self.driver.find_element(By.ID, "textarea").send_keys(address)
        print("texts inputs are filled")