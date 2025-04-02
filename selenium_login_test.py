from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class LoginFormTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://example.com/login")  # Replace with actual login URL
    
    def test_valid_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.ID, "loginButton").click()
        
        self.assertEqual(driver.current_url, "https://example.com/dashboard", "Login failed!")
    
    def test_invalid_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        driver.find_element(By.ID, "loginButton").click()
        
        error_msg = driver.find_element(By.ID, "error-message")
        self.assertTrue(error_msg.is_displayed(), "Error message not displayed")
    
    def test_mandatory_fields(self):
        driver = self.driver
        driver.find_element(By.ID, "loginButton").click()
        
        username_error = driver.find_element(By.ID, "username-error")
        password_error = driver.find_element(By.ID, "password-error")
        
        self.assertTrue(username_error.is_displayed(), "Username required message missing")
        self.assertTrue(password_error.is_displayed(), "Password required message missing")
    
    def test_invalid_email_format(self):
        driver = self.driver
        driver.get("https://example.com/register")
        driver.find_element(By.ID, "email").send_keys("invalidEmail")
        driver.find_element(By.ID, "submitButton").click()
        
        email_error = driver.find_element(By.ID, "email-error")
        self.assertTrue(email_error.is_displayed(), "Invalid email error not shown")
    
    def test_captcha_handling(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.ID, "captchaField").send_keys("captchaSolution")  # Replace with actual CAPTCHA handling
        driver.find_element(By.ID, "loginButton").click()
        
        self.assertEqual(driver.current_url, "https://example.com/dashboard", "Login failed due to CAPTCHA!")
    
    def test_password_reset(self):
        driver = self.driver
        driver.get("https://example.com/forgot-password")
        driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "resetButton").click()
        
        confirmation_msg = driver.find_element(By.ID, "confirmation-message")
        self.assertTrue(confirmation_msg.is_displayed(), "Password reset confirmation message not shown")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
