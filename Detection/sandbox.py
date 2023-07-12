import time
from selenium import webdriver

url = input("Enter URL: ")

# Set up the Selenium WebDriver
options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without UI)
driver = webdriver.Firefox(options=options)

# Capture multiple snapshots
num_snapshots = 5
interval_seconds = 2

time.sleep(10)
for i in range(num_snapshots):
    # Fetch the website snapshot
    driver.get(url)
    screenshot_path = "Detection\Snapshots"+f"\website_snapshot_{i+1}.png"
    #driver.save_screenshot(screenshot_path)

    driver.save_full_page_screenshot(screenshot_path)

    # Wait for the specified interval
    time.sleep(interval_seconds)

# Close the browser
driver.quit()





