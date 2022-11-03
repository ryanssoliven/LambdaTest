"https://www.youtube.com/watch?v=UzkuOACmBpA"
from pylenium.driver import Pylenium
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_google(py: Pylenium):
    py.visit('https://google.com')
    py.get('[name="q"]').type('puppies')
    py.get('[name="btnK"]').submit()
    assert py.should().contain_title('puppies')


def test_lambdatest_google(py: Pylenium):
    py.visit('https://google.com')
    py.get('[name="q"]').type('LambdaTest')
    py.get('[name="btnK"]').submit()
    title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"
    lt_link = py.getx("//h3[.='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")
    lt_link.click()
    assert title == py.title()

def test_lambdatest_google_sample(py: Pylenium):
    py.visit('https://google.com')
    py.get('[name="q"]').type('lambdatest github sample app')
    py.get('[name="btnK"]').submit()
    lt_link = py.getx("//h3[.='LambdaTest Sample App - GitHub Pages']")
    lt_link.click()
    checkbox = py.getx("//*[text()='First Item']").parent().get('input')
    checkbox.click()
    assert checkbox.should().be_checked()


'''
def test_lambdatest_google():
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_driver.get('https://www.google.com')
    chrome_driver.maximize_window()
    if not "Google" in chrome_driver.title:
        raise Exception("Could not load page")
    element = chrome_driver.find_element("name","q")
    element.send_keys("LambdaTest")
    element.submit()
    # Check if the LambdaTest Home Page is open
    title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"
    lt_link = chrome_driver.find_element("xpath","//h3[.='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")
    lt_link.click()
    sleep(5)
    assert title == chrome_driver.title
    sleep(2)
    chrome_driver.quit()
'''
