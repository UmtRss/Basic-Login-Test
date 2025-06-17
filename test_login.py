from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_form():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")  # Demo login sayfası
    time.sleep(2)

    # Kullanıcı adı ve şifre alanlarını bulup veri giriyoruz
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("student")  # Doğru kullanıcı adı

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Password123")  # Doğru şifre

    # Login butonuna tıklıyoruz
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()
    time.sleep(3)

    # Başarıyla giriş yapıldı mı kontrol ediyoruz
    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully", "Login başarısız!"

    driver.quit()
