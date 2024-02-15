import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def add_player_to_kahoot(game_pin, player_name):
    # Start webdriver (gebruik de juiste pad naar jouw webdriver)
    driver = webdriver.Chrome('/pad/naar/chromedriver')

    # Navigeer naar de Kahoot-website
    driver.get("https://kahoot.it")

    # Wacht tot de pagina is geladen
    time.sleep(2)

    # Vind het invoerveld voor de spelcode en voer de code in
    code_input = driver.find_element_by_css_selector(".input")
    code_input.send_keys(game_pin)
    code_input.send_keys(Keys.RETURN)

    # Wacht tot de volgende pagina is geladen
    time.sleep(2)

    # Vind het invoerveld voor de spelersnaam en voer de naam in
    name_input = driver.find_element_by_css_selector(".nickname-input")
    name_input.send_keys(player_name)
    name_input.send_keys(Keys.RETURN)

    # Sluit de webdriver af
    driver.quit()

# Voer de game pin en de naam van de speler in
game_pin = st.text_input("Pin:")
player_name = st.text_input("Name:")

# Roep de functie aan om de speler toe te voegen
add_player_to_kahoot(game_pin, player_name)
