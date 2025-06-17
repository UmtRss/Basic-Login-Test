import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")

    # Çerez uyarısını kapat (varsa)
    try:
        driver.find_element(By.ID, "L2AGLb").click()
    except:
        pass

    # Arama kutusunu bul ve arama yap
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium testing")
    search_box.submit()

    # Sayfa başlığının doğru yüklenmesini bekle
    WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))

    # Başlığın içinde "Selenium" geçtiğini doğrula
    assert "Selenium" in driver.title
