import base_file
def valid_zip_code(browser):

    self.wait_for(self.zip_code_input).send_keys("90210")  # Assuming 90210 is a valid zip code
    self.find(self.Go_button).click()