import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

class MyTestCase(unittest.TestCase):

# test01_Login_to_app_using_correct_credentials and test02_Login_to_app_using_incorrect_credentials selectors
    account_button = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[5]/android.view.ViewGroup/android.widget.ImageView")
    signin_register_button = (AppiumBy.ID, "com.zaful:id/llLoginGuide")
    sign_in_tab_button = (AppiumBy.ACCESSIBILITY_ID, "Sign in")
    enter_email_field = (AppiumBy.ID, "com.zaful:id/etLoginEmail")
    enter_password_field = (AppiumBy.ID, "com.zaful:id/etLoginPassword")
    sign_in_button = (AppiumBy.ID, "com.zaful:id/btnEmailLogin")
    welcome_back_popup = (AppiumBy.ID, "com.zaful:id/tvTitle")

    incorrect_credentials_msg = (AppiumBy.ID, "com.zaful:id/textinput_error")

# test03_Add_three_of_the_same_products_to_the_cat_and_check_correctness_of_total_price and test04_Add_and_remove_product_to_from_the_cart selectors
    swimwear_section = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout[1]/android.widget.ImageView")
    add_product = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[2]")
    add_to_bag = (AppiumBy.ID, "com.zaful:id/btn_add_cart")
    cart_in_button = (AppiumBy.ID, "com.zaful:id/iv_cart")
    close_popup = (AppiumBy.ID, "com.zaful:id/iv_cart_guid")
    plus_button = (AppiumBy.ID, "com.zaful:id/iv_number_right")
    item_number = (AppiumBy.ID, "com.zaful:id/et_number_center")
    estimated_total = (AppiumBy.ID, "com.zaful:id/tv_estimated_total_price")
    total = (AppiumBy.ID, "com.zaful:id/tvTotalPricePay")


    delete_product = (AppiumBy.ID, "com.zaful:id/iv_number_left")
    accept_button = (AppiumBy.ID, "android:id/button1")
    empty_cart_image = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")


    def setUp(self):
        desired_caps = {

            "platformName": "Android",
            "platformVersion": "12.0",
            "deviceName": "samsung SM-A528B",
            "appium:appPackage": "com.zaful",
            "appium:appActivity": "com.zaful.framework.module.system.activity.MainActivity"

        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.start_recording_screen()

    def tearDown(self):
        self.driver.quit()

    def test01_Login_to_app_using_correct_credentials(self):
        email = "michkol85@wp.pl"
        password = "Aaaa1111"
        #1. Click "Account" in the lower right corner.
        self.driver.find_element(*self.account_button).click()
        #2. Click "Sign in/Register" button.
        self.driver.find_element(*self.signin_register_button).click()
        time.sleep(3)
        #3. Select "Sign in" tab.
        self.driver.find_element(*self.sign_in_tab_button).click()
        #4. Enter a valid email address in the email address input field.
        self.driver.find_element(*self.enter_email_field).click()
        self.driver.find_element(*self.enter_email_field).send_keys(email)
        #5. Enter a valid password in the password input field.
        self.driver.find_element(*self.enter_password_field).click()
        self.driver.find_element(*self.enter_password_field).send_keys(password)
        #6. Click "Sign in" button.
        self.driver.find_element(*self.sign_in_button).click()
        time.sleep(5)
        # #7. Check if "Welcome back!" popup is visible.
        self.driver.find_element(*self.welcome_back_popup)
        print("\n", "Login success!")

    def test02_Login_to_app_using_incorrect_credentials(self):
        email = "michkol85@wp.pl"
        wrong_password = "asdasd"
        #1. Click "Account" in the lower right corner.
        self.driver.find_element(*self.account_button).click()
        #2. Click "Sign in/Register" button.
        self.driver.find_element(*self.signin_register_button).click()
        time.sleep(3)
        #3. Select "Sign in" tab.
        self.driver.find_element(*self.sign_in_tab_button).click()
        #4. Enter a valid email address in the email address input field.
        self.driver.find_element(*self.enter_email_field).click()
        self.driver.find_element(*self.enter_email_field).send_keys(email)
        #5. Enter wrong password in the password input field.
        self.driver.find_element(*self.enter_password_field).click()
        self.driver.find_element(*self.enter_password_field).send_keys(wrong_password)
        #6. Click "Sign in" button.
        self.driver.find_element(*self.sign_in_button).click()
        time.sleep(5)
        #7. Check if incorrect credential error is visible.
        self.driver.find_element(*self.incorrect_credentials_msg)
        print("\n", "Wrong credentials.")

    def test03_Add_three_of_the_same_products_to_the_cat_and_check_correctness_of_total_price(self):
            # 1. Go to "Swimwear" section on home page.
        self.driver.find_element(*self.swimwear_section).click()
        time.sleep(5)
            # 2. Add one product to the cart.
        self.driver.find_element(*self.add_product).click()
        time.sleep(3)
        self.driver.find_element(*self.add_to_bag).click()
        time.sleep(3)
            # 3. Go to "Cart".
        self.driver.find_element(*self.cart_in_button).click()
        time.sleep(3)
        self.driver.find_element(*self.close_popup).click()
            #4. Add two more of the same products.
        self.driver.find_element(*self.plus_button).click()
        time.sleep(3)
        self.driver.find_element(*self.plus_button).click()
        time.sleep(3)
            #5. Check if three of the same products were added to the cart.
        item_quantity = self.driver.find_element(*self.item_number).get_attribute('text')
        item_quantity_amount = item_quantity
        self.assertEqual(item_quantity_amount, '3')
        print("\n", "There are", item_quantity, "items in the cart.")
            #6. Check if Estimated Total amount is equal to Total amount.
        products_estimated_total = self.driver.find_element(*self.estimated_total).get_attribute('text')
        products_estimated_total_amount = products_estimated_total[3:]
        products_total = self.driver.find_element(*self.total).get_attribute('text')
        products_total_amount = products_total[3:]
        self.assertEqual(products_estimated_total_amount, products_total_amount)
        print("Correct total price.")

    def test04_Add_and_remove_product_to_from_the_cart(self):
            # 1. Go to "Swimwear" section on home page.
        self.driver.find_element(*self.swimwear_section).click()
        time.sleep(5)
            # 2. Add one product to the cart.
        self.driver.find_element(*self.add_product).click()
        time.sleep(3)
        self.driver.find_element(*self.add_to_bag).click()
        time.sleep(3)
            # 3. Go to "Cart".
        self.driver.find_element(*self.cart_in_button).click()
        time.sleep(3)
        self.driver.find_element(*self.close_popup).click()
            # 4. Remove previously added product to the cart.
        self.driver.find_element(*self.delete_product).click()
        self.driver.find_element(*self.accept_button).click()
        time.sleep(3)
            # 5. Check if cart is empty.
        self.driver.find_element(*self.empty_cart_image).click()
        print("\n", "Cart is empty!")


if __name__ == '__main__':
    unittest.main()