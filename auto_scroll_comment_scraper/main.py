from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scroll_and_collect_comments(url, comment_selector, scroll_times=5, delay=2):
    options = Options()
    driver = webdriver.Chrome

    driver.get(url)
    time.sleep(5)

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    comments = driver.find_elements(By.CSS_SELECTOR, comment_selector)
    texts = [c.text for c in comments if c.text.strip()]

    driver.quit()

    print(f"\nComments taken: {len(texts)}\n")
    for idx, comment in enumerate(texts[:10], start=1):
        print(f"{idx}. {comment}")

if __name__ == "__main__":
    url = input("Put page URL here: ").strip()
    selector = input("Input comment CSS-selector: ").strip()
    
    scroll_and_collect_comments(url, selector)