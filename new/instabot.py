import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

def report_and_exit(message):
    print(message)
    sys.exit(1)

if len(sys.argv) < 2:
    report_and_exit("Usage: python InstaBot.py <image_path>")

image_path = sys.argv[1]

# Define your credentials
username = 'risheek_r_'
password = '$Rr01010010'

# Set up Firefox options
firefox_options = Options()
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Create a new Firefox service using GeckoDriverManager
firefox_service = Service(GeckoDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

# Wait for the username and password fields to be present
try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'username')))
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
except Exception as e:
    report_and_exit(f"Error during login: {e}")

# Handle the "Save Login Info" option
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x9f619") and contains(text(), "Save your login info?")]'))
    )
    not_now_save_info_button = driver.find_element(By.XPATH, '//div[contains(@class, "x9f619") and contains(text(), "Not now")]')
    not_now_save_info_button.click()
except Exception as e:
    report_and_exit(f"No 'Save Login Info' option found or handled: {e}")

# Handle the "Turn on Notifications" popup
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]'))
    )
    not_now_notifications_button = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
    not_now_notifications_button.click()
except Exception as e:
    report_and_exit(f"No 'Turn on Notifications' popup found or handled: {e}")

# Wait for Instagram home page to load
time.sleep(5)  # Increase wait time if necessary

# Click on the "Create" button in the navbar
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Create"]'))
    )
    create_button = driver.find_element(By.XPATH, '//span[text()="Create"]')
    create_button.click()
    print("Clicked 'Create' button in the navbar")
except Exception as e:
    report_and_exit(f"No 'Create' button found or handled: {e}")

# Wait for the file input to be present
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    upload_button = driver.find_element(By.XPATH, '//input[@type="file"]')
    upload_button.send_keys(image_path)
except Exception as e:
    report_and_exit(f"Error finding or interacting with file input element: {e}")

# Wait for the caption field to be present
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Write a caption…"]'))
    )
    caption_field = driver.find_element(By.XPATH, '//textarea[@aria-label="Write a caption…"]')
    caption_field.send_keys('Your caption here')
except Exception as e:
    report_and_exit(f"Error finding or interacting with the caption field: {e}")


# Click the "Next" button to proceed
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(text(), "Next")]'))
    )
    next_button = driver.find_element(By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(text(), "Next")]')
    next_button.click()
except Exception as e:
    report_and_exit(f"Error finding or interacting with the 'Next' button: {e}")


# Click the "Next" button on the next page
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(text(), "Next")]'))
    )
    next_button = driver.find_element(By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(text(), "Next")]')
    next_button.click()
except Exception as e:
    report_and_exit(f"Error finding or interacting with the second 'Next' button: {e}")


# Click the "Share" button to post the image
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(text(), "Share")]'))
    )
    share_button = driver.find_element(By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(text(), "Share")]')
    share_button.click()
except Exception as e:
    report_and_exit(f"Error finding or interacting with the 'Share' button: {e}")

# Wait for the "Your post has been shared" message to appear
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Your post has been shared")]'))
    )
    print("Post has been shared successfully!")
except Exception as e:
    report_and_exit(f"Error waiting for the post confirmation message: {e}")

# Close the browser
driver.quit()
