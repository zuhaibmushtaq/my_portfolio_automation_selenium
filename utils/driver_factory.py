from selenium import webdriver
import yaml

def get_config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)
    
def get_driver():
    config = get_config()
    browser = config['browser'].lower()
   
    if config["browser"] == "chrome":
        driver = webdriver.Chrome()
    elif config["browser"] == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {config['browser']}")
    
    driver.maximize_window()
    driver.implicitly_wait(config["timeout"])
    driver.get(config["base_url"])
    return driver