from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
#1 
#2
#3
#4 
#5
class HomePage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()
    
    def login(self, username, password):
        #login_link_locator = (By.ID, "user-name")
       # wait_login_link = self.wait.until(EC.element_to_be_clickable(login_link_locator))
       # wait_login_link.click()

        username_field_locator = (By.ID, "user_name")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()

#6       
    def verification(self):
        verification_products_loc=(By.XPATH, "//span[@class='title' and text()='Products']")
        wait_verification_products= self.wait.until(EC.presence_of_element_located(verification_products_loc))

        verification_products_loc = wait_verification_products.text
        assert verification_products_loc == "Products"
    
 #7
    def add_two_products(self):
        prod1= self.selenium_driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light") 
        prod2=self.selenium_driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        prod1.click()
        prod2.click()
#8
    def click_icon(self):

        cart= self.selenium_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart.click()
#9  
    def verification_your_cart(self):
        cart_loc=(By.XPATH, "//span[@class='title' and text()='Your Cart']")
        wait_cart= self.wait.until(EC.presence_of_element_located(cart_loc))
        cart_loc = wait_cart.text
        assert cart_loc == "Your Cart"
#10  
    def products_chart(self):
        name1= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div[@class='inventory_item_name']")
        name2= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']")
        assert name1.text=="Sauce Labs Backpack" 
        assert name2.text=="Sauce Labs Bike Light" 

#11 
 
    def click_checkout(self):
        check_out=self.selenium_driver.find_element(By.ID, "checkout")
        check_out.click()
#12
    def your_information_title(self):
        information_locator = (By.XPATH, "//span[@class='title' and contains(text(),'Checkout: Your Information')]")
        wait_information = self.wait.until(EC.presence_of_element_located(information_locator))
        your_information_text = wait_information.text
        assert your_information_text == "Checkout: Your Information"

#13 

def the_fields_filling(self,first_name,last_name, zip_code):
        first_name_loc = (By.ID, "first-name")
        wait_name1 = self.wait.until(EC.element_to_be_clickable(first_name_loc))
        wait_name1.click()
        wait_name1.clear()
        wait_name1.send_keys(first_name)

        last_name_loc = (By.ID, "last-name")
        wait_last_name = self.wait.until(EC.element_to_be_clickable(last_name_loc))
        wait_last_name.click()
        wait_last_name.clear()
        wait_last_name.send_keys(last_name)

        zip_code_loc = (By.ID, "postal-code")
        wait_zip_code = self.wait.until(EC.element_to_be_clickable(zip_code_loc))
        wait_zip_code.click()
        wait_zip_code.clear()
        wait_zip_code.send_keys(zip_code)
#14
        continue_button=self.selenium_driver.find_element(By.ID, "continue")
        continue_button.click()
    
#15
def verification_overview(self):
        overview_loc=(By.XPATH, "//span[@class='title']")
        wait_checkout_overview= self.wait.until(EC.presence_of_element_located(overview_loc))
        overview_loc=wait_checkout_overview.text
        assert overview_loc== "Checkout: Overview"
#16
 
def verification_products_overview(self):
        name_prod1= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div[@class='inventory_item_name']")
        name_prod2=self.selenium_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']")
        assert name_prod1.text=="Sauce Labs Bike Light"
        assert name_prod2.text=="Sauce Labs Backpack"
#17

def finish_button(self):
       button_finish= self.selenium_driver.find_element(By.ID, "finish")  #locator u html
       button_finish.click()

#18

def complete(self):
        complete_loc = (By.XPATH, "//span[@class='title' and text()='Checkout: Complete!']")
        complete_wait = self.wait.until(EC.presence_of_element_located(complete_loc))
        complete_text_checkout = complete_wait.text
        title = "Checkout: Complete!"
        assert complete_text_checkout == title


#19

def menu_button(self):
        menu_loc= (By.ID, "react-burger-menu-btn")
        wait_loc=self.wait.until(EC.element_to_be_clickable(menu_loc))
        wait_loc.click()

#20   

def logout_button(self):
        logout_locator=(By.ID, "logout_sidebar_link")
        wait_logout_locator=self.wait.until(EC.element_to_be_clickable(logout_locator))
        wait_logout_locator.click()

#21  

def verification_login_page(self):
        title = "Swag Labs"
        actual_title = self.selenium_driver.title
        assert actual_title == title
        


 
 
   #  def is_login_and_signup_invisible(self):
   #     login_link_locator = (By.ID, "login2")
   #     self.wait.until(EC.invisibility_of_element_located(login_link_locator))
        
    #    self.wait.until(EC.invisibility_of_element_located(signup_link_locator))
    
   # def get_welcome_text(self):
     #   welcome_text_tuple = (By.ID, "nameofuser")
     #   wait_welcome_text = self.wait.until(EC.element_to_be_clickable(welcome_text_tuple))

      #  welcome_text = wait_welcome_text.text
       # return welcome_text
    
   # def get_alert_text(self):
    #    alert = self.wait.until(EC.alert_is_present())
     #   alert_text = alert.text
      #  alert.accept()
       # return alert_text
