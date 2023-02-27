import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class loginpage(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        driver = self.driver
        driver.get("https://10.4.4.11")
        driver.find_element("id", "username").send_keys("superadmin")
        driver.find_element('id', "password").send_keys("aviz@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

    def testsearch1(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Users Icon']").click()
        driver.find_element(By.XPATH, "//button//span[text()='Add']").click()
        time.sleep(2)
        driver.find_element("name", "username").send_keys("vishveksre")
        driver.find_element("name", "password").send_keys("aviz@123")
        driver.find_element("name", "confirmPassword").send_keys("aviz@123")
        driver.find_element("name", "firstName").send_keys("sre")
        driver.find_element("name", "lastName").send_keys("sre")
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@tabindex='-1']").click()
        time.sleep(2)
        

    def testsearch2(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Users Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Suspend']").click()
        driver.find_element(By.XPATH, "//button[text()='Yes']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='/static/media/refresh.d8d17dec.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Restore']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/span/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Remove']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@tabindex='-1']").click()
        time.sleep(3)

    def testsearch3(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Settings Icon']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Application']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='demo-multiple-name']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[text()='60 Seconds']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/button/div/p").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//p[text()='Reset']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='number']").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@type='number']").send_keys(3)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button/div/p").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@tabindex='-1']").click()
        time.sleep(2)

# reset password

    def testsearch4(self): 
        driver = self.driver
        driver.find_element(By.XPATH, "//img[@alt='Users Icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div[8]/div/div/button/div/div").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Reset Password']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Admin@123")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("Admin@123")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@tabindex='-1']").click()
        time.sleep(2)

# reset and confirm password   
    def testsearch5(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("aviz@123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='confirmpassword']").send_keys("aviz@123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Reset password']").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
