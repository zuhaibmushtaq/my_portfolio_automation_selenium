from utils.driver_factory import get_driver
from pages.Homepage import HomePage

def test_home_page_loads():
    driver = get_driver()
    home = HomePage(driver)
    assert home.is_home_loaded(), "Home page did not load correctly"
    driver.quit()

def test_experience_page_loads():
    driver = get_driver()
    expr = HomePage(driver)
    assert expr.open_experience_page(), "Experience page did not load correctly"
    driver.quit()

def test_skills_page_loads():
    driver = get_driver()
    skills = HomePage(driver)
    assert skills.open_skills_page(), "Skills page did not load correctly"
    driver.quit()

def test_language_page_loads():
    driver = get_driver()
    language = HomePage(driver)
    assert language.open_language_page(), "Language page did not load correctly"
    driver.quit()

def test_contact_page_loads():
    driver = get_driver()
    contact = HomePage(driver)
    assert contact.open_contact_page(), "Contact page did not load correctly"
    driver.quit()

def test_download_reesume():
    driver = get_driver()
    resume = HomePage(driver)
    resume.click(HomePage.RESUME_LINK)
    assert resume.download_resume(), "Failed to download resume"
    driver.quit()

