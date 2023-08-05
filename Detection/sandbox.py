import time
from selenium import webdriver
from PIL import Image
import matplotlib.pyplot as plt

url = input("Enter URL: ")

# Set up the Selenium WebDriver
options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without UI)
driver = webdriver.Firefox(options=options)

print("\n\nSandboxing Started!!!\n")
# Capture multiple snapshots
num_snapshots = 4
interval_seconds = 2

time.sleep(4)
for i in range(num_snapshots):
    # Fetch the website snapshot
    driver.get(url)
    screenshot_path = "Detection\Snapshots"+f"\website_snapshot_{i+1}.png"
    print(f"website_snapshot_{i+1}.png saved.")
    #driver.save_screenshot(screenshot_path)

    driver.save_full_page_screenshot(screenshot_path)
    # Wait for the specified interval
    time.sleep(interval_seconds)

# Close the browser
driver.quit()

print("\n\nSnapshots are ready!!!")


# List of screenshot file paths
screenshot_paths = []
for i in range(4):
    screenshot_paths.append("E:\Malicious-URL-detection\Detection\Snapshots"+f"\website_snapshot_{i+1}.png")
# Create a figure and axis using matplotlib
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Loop through each screenshot path and display it
for ax, path in zip(axes.ravel(), screenshot_paths):
    # Open the image using PIL
    img = Image.open(path)
    
    # Display the image on the axis
    ax.imshow(img)
    
    # Remove axis ticks and labels
    ax.axis('off')
plt.suptitle("Snapshot Viewer",fontsize=16, fontweight='bold')
# Adjust layout and display the images
plt.tight_layout()
plt.show()





