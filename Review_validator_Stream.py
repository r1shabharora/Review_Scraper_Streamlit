#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#NEW
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def scrape_reviews(review_links):
    # Configure Selenium options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    options.add_argument('--incognito')
    options.add_argument("--disable-plugins-discovery")
    # Start the Selenium WebDriver
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
    
    all_reviews = []

    for link in review_links:
        driver.get(link)

        try:
            # Wait for the reviews to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-section.review')))
            
            # Extract reviews
            reviews = driver.find_elements_by_class_name('a-section.review')

            for review in reviews:
                review_text = review.find_element_by_class_name('review-text').text
                all_reviews.append(review_text)
        
        except Exception as e:
            print(f"Error scraping reviews for {link}: {e}")

    driver.quit()  # Close the WebDriver after scraping is done
    return all_reviews

# Example usage:
review_links = [
    "https://www.amazon.com/product-review-link1",
    "https://www.amazon.com/product-review-link2",
    "https://www.amazon.com/product-review-link3"
]

reviews = scrape_reviews(review_links)
for review in reviews:
    print(review)
