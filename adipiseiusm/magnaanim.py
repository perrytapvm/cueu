from selenium.webdriver.common.by import By


def click_Xpath(driver, index, xpath):
    """Clicks on the element at the given index using the given xpath.

    Args:
        driver: The WebDriver instance.
        index: The index of the element to click on.
        xpath: The xpath of the element to click on.
    """
    elements = driver.find_elements(By.XPATH, xpath)
    if index < len(elements):
        elements[index].click()
    else:
        raise Exception("Element not found at index: {}".format(index))

