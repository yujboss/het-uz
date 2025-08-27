import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This line helps confirm that the correct file is being imported.
print("DEBUG: scraper.py module has been loaded.")

# Get the logger instance
logger = logging.getLogger(__name__)

def get_current_reading(config):
    """Logs into the website and scrapes the current electricity reading."""
    logger.info("Starting scraper to fetch new reading...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_argument("--user-data-dir=./chrome_profile")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(config.HET_URL)
        wait = WebDriverWait(driver, 20)

        # Login
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="login"]'))).send_keys(config.HET_USERNAME)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]'))).send_keys(config.HET_PASSWORD)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Kirish')]"))).click()
        logger.info("Login successful. Waiting for dashboard.")

        # Extract value
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.card-title")))
        value_xpath = "//card-info[.//div[contains(text(), 'Joriy oy boshidan hisoblangan kVt·s')]]//div[contains(@class, 'card-value')]/span"
        value_element = wait.until(EC.visibility_of_element_located((By.XPATH, value_xpath)))
        time.sleep(0.5)
        
        extracted_value = driver.execute_script("return arguments[0].innerText;", value_element)
        logger.info(f"Successfully extracted value: {extracted_value}")
        return extracted_value
    except Exception as e:
        logger.error(f"An error occurred during scraping: {e}")
        driver.save_screenshot("error_screenshot.png")
        return None
    finally:
        driver.quit()
