import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def join_kahoot(pin):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()  # You'll need to have Chrome WebDriver installed and in PATH
    driver.get("https://kahoot.it")

    # Wait for page to load
    time.sleep(3)

    # Enter PIN
    pin_input = driver.find_element_by_css_selector("input[placeholder='Enter game PIN']")
    pin_input.send_keys(pin)
    pin_input.send_keys(Keys.RETURN)

    # Wait for joining screen
    time.sleep(3)

    # Click on "Enter" button
    join_button = driver.find_element_by_css_selector(".enter-button__EnterButton-sc-1s2xb6-0")
    join_button.click()

    # Close browser after joining
    # Comment out the below line if you want to keep the browser open after joining
    driver.quit()

def main():
    st.title("Kahoot Auto Joiner")
    st.write("Enter the Kahoot PIN below and click 'Join' to automatically join the game.")

    # Input field for Kahoot PIN
    pin = st.text_input("Enter Kahoot PIN:")

    # Join button
    if st.button("Join"):
        if pin:
            join_kahoot(pin)
        else:
            st.warning("Please enter a PIN to join Kahoot.")

if __name__ == "__main__":
    main()
