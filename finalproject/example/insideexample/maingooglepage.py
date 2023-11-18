def __init__(self, driver):
    self.driver = driver
    self.search = self.driver.find_element(By.NAME, "q")

    print('into init')


def search_for_text(self, text_for_search):
    print(f"Try to serach for{text_for_search}")
    self.search.click()
    self.search.send_keys(text_for_search)
    self.search.send_keys(Keys.ENTER)


def get_text_from_search_menu(self):
    text = self.search.text()
    return text