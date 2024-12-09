import pdfplumber
import csv
import time
def extract_text_pdfplumber(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text

# Example usage
file_path = "food_banks.pdf"  # Replace with your PDF file path
extracted_text = extract_text_pdfplumber(file_path).replace("Your Location: 1 Oxford St, Cambridge, MA 02138, USA", "").replace("Radius: 90 miles", "").replace("\n", " ")
#print(extracted_text)
text_list = extracted_text.split("PROGRAMS")
#print(text_list)
kitchen_dict_list = []
counter = 0
names = []
for kitchen in text_list:
    kitchen_dict = {}
    counter += 1
    kitchen_list = kitchen.split("Address")
    if len(kitchen_list) == 1:
        break
    print(kitchen_list)
    names.append(kitchen_list[0])
    address_long = kitchen_list[1]
    index = address_long.index("MA0")
    address = address_long[:index+6]
    kitchen_dict["name"] = kitchen_list[0].split('PM')[-1]
    kitchen_dict["address"] = address
    kitchen_dict["web page"] = ""
    kitchen_dict["classification"] = "Food Kitchen"
    kitchen_dict_list.append(kitchen_dict)

print(kitchen_dict_list)
with open('kitchens.csv', 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = ["name", "address", "web page", "classification"]) 
    writer.writeheader() 
    writer.writerows(kitchen_dict_list) 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def get_first_result_urls(search_queries):
    # Configure the WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Path to your ChromeDriver
    driver_path = "/path/to/chromedriver"  # Replace with the path to your ChromeDriver
    service = Service(driver_path)

    # Start the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    base_url = "https://www.google.com"

    results = []

    try:
        # Open Google
        driver.get(base_url)

        for query in search_queries:
            print(f"Searching for: {query}")
            
            # Find the search box
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

            # Wait for results to load
            time.sleep(2)

            # Find the first result URL
            try:
                first_result = driver.find_element(By.CSS_SELECTOR, "a h3")
                first_result_url = first_result.find_element(By.XPATH, "..").get_attribute("href")
                print(f"First result URL for '{query}': {first_result_url}")
                results.append((query, first_result_url))
            except Exception as e:
                print(f"Error fetching results for '{query}': {e}")
                results.append((query, None))
    finally:
        driver.quit()

    return results

results = get_first_result_urls(names)
links = []
a = open("kitchen_links.txt", "a")
for query, url in results:
    print(f"{query} -> {url}")
    a.write(url + "\n")
    links.append(url)
a.close()

for item1, item2 in zip(kitchen_dict, links):
    item1[2] = item2

with open('kitchens.csv', 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = ["name", "address", "web page", "classification"]) 
    writer.writeheader() 
    writer.writerows(kitchen_dict_list) 
