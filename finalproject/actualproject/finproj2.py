from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.booking.com/")

search = driver.find_element(By.NAME, "ss")
search.send_keys("Toronto")
search.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sr-hoteltitle")))

scores = driver.find_elements(By.CSS_SELECTOR, "div.bui-review-scorebadge")
hotel_names = driver.find_elements(By.CLASS_NAME, "sr-hotel__title")

hotel_scores = {}
for i in range(len(hotel_names)):
    name = hotel_names[i].text
    score = scores[i].text
    if score:  # Check if score exists
        hotel_scores[name] = float(score)


if hotel_scores:
    highest_score_hotel = max(hotel_scores, key=hotel_scores.get)
    highest_score = hotel_scores[highest_score_hotel]

    print(f"The hotel with the highest score is '{highest_score_hotel}' with a score of {highest_score}")
else:
    print("No scores found.")
driver.quit()