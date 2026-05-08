import time

from Pages.textInput import TextInput

def test_TextInput(setup):
    driver = setup
    ti = TextInput(driver)
    ti.open_url()
    ti.input_text("Jyoti","matt@gmail.com", "1234","bangalore")
    time.sleep(4)
