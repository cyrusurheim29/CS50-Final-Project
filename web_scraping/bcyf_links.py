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


# Example usage
if __name__ == "__main__":
    file_path = 'community_centers.csv'
    df = pd.read_csv(file_path)
    print(df)
    column_name = 'SITE'
    column_values = df[column_name].tolist()
    search_queries = [x + " Boston Community Center" for x in column_values]
    results = get_first_result_urls(search_queries)
    a = open("bcyf_links.txt", "a")
    for query, url in results:
        print(f"{query} -> {url}")
        a.write(url + "\n")
    a.close()