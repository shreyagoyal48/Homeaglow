from selenium.webdriver.common.by import By
from .common import CommonOps

class HomeaglowDealsPage(CommonOps):
    zip_code_input = (By.ID, "Zipcode")
    Go_button = (By.ID, "zip-hero-go-button")
    get_clean_btn = (By.ID, "Get Clean!")
    email_text = (By.ID, "email-input")
    select_discount_voucher = (By.ID, "-headlessui-label-:r28:")
    discount_voucher_btn = (By.ID, "GET MY DISCOUNT VOUCHER")
    voucher_details = (By.ID, "Discount Voucher and Membership Details")
    continue_button = (By.ID, "CONTINUE")
    payment_page = (By.ID, "headlessui-label-:r15:")
    credit_card_option = (By.ID, "headlessui-label-:rd:")
    card_number_input = (By.ID, "cc-input")
    expiry_input = (By.ID, "exp-input")
    cvv_input = (By.ID, "cvc-input")
    purchase = (By.ID, "PURCHASE & SCHEDULE")
    thank_you_page = (By.ID, "headlessui-dialog-title-:r1m:")
    select_an_option = (By.label, "How did you hear about us?")
    select_influencer = (By.ID, "Influencer")
    submit_btn = (By.ID, "Submit")

    
    
    def valid_zip_code(self):
        self.wait_for(self.zip_code_input).send_keys("90210")  # Assuming 90210 is a valid zip code

    def select_voucher_deals(self):
        self.scroll_down_to_element(id, "headlessui-radiogroup-:r24:")
        self.click(self.select_discount_voucher) #selecting 3 hours of cleaning voucher
        self.click(self.get)
        self.wait_for(self.email_text).send_keys("test1@test.com")
        self.find(self.discount_voucher_btn).click()
        self.wait_for(self.continue_button).click()

    def is_voucher_displayed(self):
        self.wait_for(self.voucher_details)

    def use_credit_card(self):
        self.wait_for(self.payment_page)
        self.wait_for(self.credit_card_option).click()
        self.wait_for(self.card_number_input).send_keys("4242424242424242")
        self.wait_for(self.expiry_input).send_keys("1234")
        self.wait_for(self.cvv_input).send_keys("578")
        self.click(self.purchase)

    def check_out(self):
        self.wait_for(self.thank_you_page)
        self.click(self.select_an_option)
        self.click(self.select_influencer)
        self.click(self.submit_btn)


