# Imports:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Steg 1: Logga in På Moon Bitcoins med inloggnings wallet addressen

# Steg 2: Leta reda på "Dashboard"

# Steg 3: Klicka på "Tim bonusen" om det går

# Steg 4: Klicka på "Start" button

# Eventuellt så behöver du lägga en hel del waiting steg i mellan för att få allt att köra

# Steg 5: Klicka på "Daily bonus" om det går

# Steg 6: Klicka "Logg out" och sedan stäng ner sidan

# wallet
Wallet = "Your wallet address!"

# Setup
PATH = "C:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.moonbitcoins.com/")
print(driver.title)

time.sleep(10)

search = driver.find_element_by_xpath("/html/body/section/div[1]/div/div[1]/div/form/div[1]/input")
time.sleep(2)
search.send_keys(Wallet)

search = driver.find_element_by_xpath("/html/body/section/div[1]/div/div[1]/div/form/div[2]/input").click()
time.sleep(3)
search = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()


start = True
wait = WebDriverWait(driver, 10)
while(start):
    time.sleep(10)

    driver.refresh()
    print("Refreshing!")
    # Hourly bonus
    try:
        search = driver.find_element_by_xpath('/html/body/main/section/div/div[2]/div[1]/a/button').click()
        print("Clicking on Hourly Bonus!")

    except NoSuchAttributeException:
        print("Element not found!")
        continue
    except:
        print("Cant find Hourly bonus this time!")
    # Every 15 min collection
    try:
        search = driver.find_element_by_xpath('//*[@id="start-mining"]').click()
        print("Clicking on Starting Miner script!")
    except NoSuchAttributeException:
        print("Element not found!")
        continue
    except:
        print("Cant find 15 Min miner right now!")


    time.sleep(1200)
    try:
        search = driver.find_element_by_css_selector('#header > div.container > nav > ul > li:nth-child(2) > a').click()
        print("Entering Daily bonus tab")
        time.sleep(20)
        search = driver.find_element_by_xpath('//*[@id="pricing"]/div/a').click()
        print("Clicking on daily bonus!")

        search = driver.find_element_by_css_selector('#header > div.container > nav > ul > li:nth-child(1) > a').click()
        print("Going back to Dashboard")

    except NoSuchAttributeException:
        print("Element not found!")
        continue
    except:
        print("Cant enter Daily bonus tab!")


    time.sleep(15)
    # refresh site
    try:
        driver.refresh()
        print("Refreshing!")

    except NoSuchAttributeException:
        print("Element not found!")
        continue
    except:
        print("Cant refresh!")






