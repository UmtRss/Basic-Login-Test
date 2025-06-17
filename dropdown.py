from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time

def test_dropdown_selection():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = driver.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)

    dropdown.select_by_visible_text("Option 2")
    selected_option = dropdown.first_selected_option

    assert selected_option.text == "Option 2"

    time.sleep(2)
    driver.quit()
