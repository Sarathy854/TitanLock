from selenium import webdriver
import time

# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening a browser window
driver = webdriver.Chrome(options=options)

url = "https://github.com/Vimal007Vimal"
refresh_count = 1000  # Change this number as needed

for i in range(refresh_count):
    driver.get(url)
    print(f"Refreshed {i+1} times")
    time.sleep(2)  # Wait before refreshing again

driver.quit()
