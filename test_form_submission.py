import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_form_submission(driver):
    file_path = os.path.abspath("sample.png")
    assert os.path.exists(file_path), f"sample.png dosyası bulunamadı: {file_path}"

    driver.get("https://demoqa.com/automation-practice-form")

    # Modal ve reklamları temizle
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
    try:
        driver.execute_script("""
            document.querySelectorAll("#fixedban, [id^='google_ads'], .modal-backdrop, .modal")
                .forEach(el => el.style.display = 'none');
        """)
    except:
        pass

    # Form alanlarını doldur
    driver.find_element(By.ID, "firstName").send_keys("Umut")
    driver.find_element(By.ID, "lastName").send_keys("Reis")
    driver.find_element(By.ID, "userEmail").send_keys("umutreis@example.com")

    male_radio = driver.find_element(By.ID, "gender-radio-1")
    driver.execute_script("arguments[0].click();", male_radio)

    driver.find_element(By.ID, "userNumber").send_keys("5341234567")

    # Doğum tarihi seçimi
    dob_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))
    )
    driver.execute_script("arguments[0].click();", dob_input)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select"))
    ).send_keys("1997")
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("June")
    driver.find_element(By.XPATH, "//div[text()='9']").click()

    # Ders ve hobi seçimi
    subject_input = driver.find_element(By.ID, "subjectsInput")
    subject_input.send_keys("Maths\n")

    sports_checkbox = driver.find_element(By.ID, "hobbies-checkbox-1")
    driver.execute_script("arguments[0].click();", sports_checkbox)

    # Dosya yükleme
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    # Adres alanına yazı gir
    address_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "currentAddress"))
    )
    address_input.send_keys("Bolu, Türkiye")

    # Şehir ve eyalet seçimleri istersen buraya eklenebilir.
    # Submit'e kadar devam etmek istersen aşağıdaki satırı aç:
    # driver.find_element(By.ID, "submit").click()
