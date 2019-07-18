import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CoreTestCases(unittest.TestCase):
	@classmethod
	
	def teardown_method(self, method):
		self.driver.quit()
		
	def test_ShoppingCart(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(15)
		
		#Open W&S webpage
		self.driver.get("https://www.williams-sonoma.com/")
		self.driver.maximize_window()
		
		#Close pop-up
		self.driver.find_element(By.LINK_TEXT, "minimize").click()
		 
		#Open shopping cart, verify empty
		self.driver.find_element(By.CSS_SELECTOR, ".view-cart > span").click()
		assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Your shopping cart is currently empty"
		 
		#Browse to item and add to cart, close pop-up
		self.driver.find_element(By.CSS_SELECTOR, ".topnav-cookware").click()
		self.driver.find_element(By.CSS_SELECTOR, ".shop-list:nth-child(3) > li:nth-child(2) .product-thumb").click()
		self.driver.find_element(By.CSS_SELECTOR, ".product-cell:nth-child(4) > .product-thumb .product-thumb").click()
		self.driver.find_element(By.ID, "primaryGroup_addToCart_0").click()
		self.driver.find_element(By.ID, "overlayCloseButton").click() 
		time.sleep(2) #Sleep needed to allow popup to fully load
		self.driver.find_element(By.CSS_SELECTOR, ".view-cart > span:nth-child(1)").click()
		
		#Remove item from cart and check that cart is empty
		self.driver.find_element(By.CSS_SELECTOR, ".delete-item").click()
		assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Your shopping cart is currently empty"	 

		#Close browser
		self.driver.quit()
		
	def test_Purchase(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(15)
		
		#Open W&S webpage
		self.driver.get("https://www.williams-sonoma.com/")
		self.driver.maximize_window()
		
		#Close pop-up
		self.driver.find_element(By.LINK_TEXT, "minimize").click()
		
		#Add item to cart and checkout
		self.driver.find_element(By.CSS_SELECTOR, ".topnav-cookware").click()
		self.driver.find_element(By.CSS_SELECTOR, ".shop-list:nth-child(3) > li:nth-child(6) .product-thumb").click()
		self.driver.find_element(By.CSS_SELECTOR, ".product-cell:nth-child(5) > .product-thumb .product-thumb").click()
		self.driver.find_element(By.CSS_SELECTOR, ".qty").click()
		self.driver.find_element(By.CSS_SELECTOR, ".qty").send_keys("1")
		self.driver.find_element(By.CSS_SELECTOR, ".active > .swatchThumb").click()
		self.driver.find_element(By.ID, "primaryGroup_addToCart_0").click()
		time.sleep(3) #allow enough time for pop-up to appear
		self.driver.find_element(By.ID, "anchor-btn-checkout").click()
		self.driver.find_element(By.XPATH, "//div[@id=\'cartButtons\']/button").click()
		self.driver.find_element(By.CSS_SELECTOR, ".button-group:nth-child(1) > .btn").click()
		
		#Input address
		self.driver.find_element(By.ID, "shipTo.address.fullName").click()
		self.driver.find_element(By.ID, "shipTo.address.fullName").send_keys("John Smith")
		self.driver.find_element(By.ID, "shipTo.address.addrLine1").send_keys("123 Main St")
		self.driver.find_element(By.ID, "shipTo.address.city").send_keys("Boston")
		dropdown = self.driver.find_element(By.ID, "shipTo.address.state")
		dropdown.find_element(By.XPATH, "//option[. = 'Massachusetts']").click()
		self.driver.find_element(By.ID, "shipTo.address.zip").send_keys("02130")
		self.driver.find_element(By.ID, "shipTo.address.dayPhone").send_keys("5555555555")
		self.driver.find_element(By.ID, "shipTo.billingAddressUpdate").click()
		
		#Click to check abd verify Payment page was reached
		self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
		self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
		self.driver.find_element(By.CSS_SELECTOR, ".checkout-page-header").click()
		assert self.driver.find_element(By.CSS_SELECTOR, ".checkout-page-header").text == "Payment & Review"


		#Close browser
		self.driver.quit()		

	def test_Login(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(15)
		
		#Open W&S webpage
		self.driver.get("https://www.williams-sonoma.com/")
		self.driver.maximize_window()
		
		#Close pop-up
		self.driver.find_element(By.LINK_TEXT, "minimize").click()
		
		#Login to account page and verify landing page
		self.driver.find_element(By.CSS_SELECTOR, ".user-account-link").click()
		self.driver.find_element(By.ID, "login-email").click()
		self.driver.find_element(By.ID, "login-email").send_keys("buoy@mail-group.net")
		self.driver.find_element(By.ID, "login-password").click()
		self.driver.find_element(By.ID, "login-password").send_keys("1EmYouBuoyMe1")
		self.driver.find_element(By.CSS_SELECTOR, ".button-group > #btn-sign-in").click()
		self.driver.find_element(By.CSS_SELECTOR, ".account-page-header").click()
		assert self.driver.find_element(By.CSS_SELECTOR, ".account-page-header").text == "Hello, John Smith"

		#Close browser
		self.driver.quit()	

	def test_Track(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(15)
		
		#Open W&S webpage
		self.driver.get("https://www.williams-sonoma.com/")
		self.driver.maximize_window()
		
		#Close pop-up
		self.driver.find_element(By.LINK_TEXT, "minimize").click()
		
		#Login to account page and verify landing page
		self.driver.find_element(By.CSS_SELECTOR, ".track-order-link > a").click()
		self.driver.find_element(By.ID, "ordernum").click()
		self.driver.find_element(By.ID, "ordernum").send_keys("043289560862")
		self.driver.find_element(By.ID, "z0").click()
		self.driver.find_element(By.ID, "z0").send_keys("02144")
		self.driver.find_element(By.ID, "orderStatusButton").click()
		self.driver.find_element(By.CSS_SELECTOR, ".order-header-title").click()
		
		#Verify order detail page
		assert self.driver.find_element(By.CSS_SELECTOR, ".order-header-title").text == "Order Details"

		#Close browser
		self.driver.quit()		
		
	def test_CreateAccount(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(15)
		
		#Open W&S webpage
		self.driver.get("https://www.williams-sonoma.com/")
		self.driver.maximize_window()
		
		#Close pop-up
		self.driver.find_element(By.LINK_TEXT, "minimize").click()
		
		#Create account
		self.driver.find_element(By.CSS_SELECTOR, ".user-account-link").click()
		self.driver.find_element(By.ID, "fullName").click()
		self.driver.find_element(By.ID, "fullName").send_keys("John Smith")
		self.driver.find_element(By.ID, "createAccountForm").click()
		self.driver.find_element(By.ID, "email").click()
		self.driver.find_element(By.CSS_SELECTOR, ".main-content").click()
		
		#Generate random email address
		email = str(random.random())+"@website.com"
		self.driver.find_element(By.ID, "email").send_keys(email)
		self.driver.find_element(By.ID, "confirmEmail").click()
		self.driver.find_element(By.ID, "confirmEmail").send_keys(email)
		self.driver.find_element(By.ID, "password").click()
		self.driver.find_element(By.ID, "password").click()
		self.driver.find_element(By.ID, "password").send_keys("1EmYouBuoyMe1")
		self.driver.find_element(By.ID, "confirmPassword").click()
		self.driver.find_element(By.ID, "confirmPassword").send_keys("1EmYouBuoyMe1")
		self.driver.find_element(By.CSS_SELECTOR, ".button-group:nth-child(10) > .btn").click()
		#self.driver.find_element(By.CSS_SELECTOR, ".small-sidebar-page").click()
		
		#Verify account creation
		assert self.driver.find_element(By.CSS_SELECTOR, ".instructions > h2").text == "Thank You! Please Confirm Your Account."

		#Close browser
		self.driver.quit()		

if __name__ == '__main__':
	unittest.main()