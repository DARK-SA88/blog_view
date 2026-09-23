import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# ===== এখানে তোর ব্লগার পোস্টের লিংক বসা =====
URL = "https://rifat-mahmud-org-bct.blogspot.com/2021/01/this-is-my-own-captured-photo.html"
# =============================================

COUNT = 15   # প্রতি রানে কতবার ভিজিট করবে

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
]

success = 0
for i in range(COUNT):
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument(f"user-agent={random.choice(user_agents)}")
    opts.binary_location = "/usr/bin/chromium-browser"
    
    driver = None
    try:
        driver = webdriver.Chrome(options=opts, service=Service("/usr/bin/chromedriver"))
        driver.set_page_load_timeout(30)
        driver.get(URL)
        time.sleep(random.randint(8, 25))
        h = driver.execute_script("return document.body.scrollHeight")
        for _ in range(random.randint(1, 3)):
            driver.execute_script(f"window.scrollTo(0, {random.randint(0, h)});")
            time.sleep(random.uniform(1.5, 4))
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(random.uniform(1, 3))
        success += 1
        print(f"[{i+1}/{COUNT}] OK")
    except Exception as e:
        print(f"[{i+1}/{COUNT}] ERR: {str(e)[:100]}")
    finally:
        if driver:
            driver.quit()
    if i < COUNT - 1:
        time.sleep(random.randint(10, 30))

print(f"\nমোট সফল: {success}/{COUNT}")
