from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# Setup: Her testten önce tarayıcıyı başlatır, sonra kapatır
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştırır (görünmez)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Test Case 1: Geçerli kullanıcı adı ve şifre ile başarılı giriş
def test_valid_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully"

# Test Case 2: Hatalı kullanıcı adı testi
def test_invalid_username(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    error = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error

# Test Case 3: Hatalı şifre testi
def test_invalid_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()
    error = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error
