from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    HOME_LINK = (By.LINK_TEXT, "Home") 
    EXP_LINK = (By.LINK_TEXT, "Experience")
    SKILLS_LINK = (By.LINK_TEXT, "Skills")
    LANG_LINK = (By.LINK_TEXT, "Languages") # example, adjust locator
    CONTACT_LINK = (By.LINK_TEXT, "Contact")

    def is_home_loaded(self):
        return self.is_visible(self.HOME_LINK)
    
    def open_experience_page(self):
        self.click(self.EXP_LINK)
        return self.is_visible(self.EXP_LINK)

    def open_skills_page(self):
        self.click(self.SKILLS_LINK)
        return self.is_visible(self.SKILLS_LINK)

    def open_language_page(self):
        self.click(self.LANG_LINK)
        return self.is_visible(self.LANG_LINK)

    def open_contact_page(self):
        self.click(self.CONTACT_LINK)
        return self.is_visible(self.CONTACT_LINK)





