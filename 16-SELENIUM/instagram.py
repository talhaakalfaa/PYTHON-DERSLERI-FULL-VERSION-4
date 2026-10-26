from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")

        wait = WebDriverWait(self.browser, 15)

        usernameInput = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        passwordInput = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")

        wait = WebDriverWait(self.browser, 10)

        followersLink = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href,'/followers/')]")
            )
        )

        followersLink.click()


İnstgrm = Instagram(username, password)
İnstgrm.signIn()
İnstgrm.getFollowers()

input("Tarayıcı açık kalsın mı? Enter'a bas...")
