import pytest
from selenium import webdriver
from .common import CommonOps
from homeaglow_deals import HomeaglowDealsPage

 
@pytest.fixture

def test_page_load(browser):
    # Action
    browser.get("https://new-public-immwmazfl-homeaglow-eng.vercel.app/deal")

    # Expected Result
    assert "Homeaglow" in browser.title

def test_valid_zip_code(self):
    self.pages.valid_zip_code()
    assert self.wait_for(self.get_clean_btn)
    
    # Expected Result
    deals = self.find_elements_by_class_name("deal")
    assert len(deals) > 0

def test_credit_card(self):
    self.pages.valid_zip_code()
    



