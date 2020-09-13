# create_access_token.py

# Necessary Imports
from fyers_api import accessToken
# from fyers_api import fyersModel
from selenium import webdriver
import sys
from decouple import config
import time
import re
import pickle

# If you are using Firefox
driver = webdriver.Firefox()
# If you are using Chrome
# driver = webdriver.Chrome()

# Load all the credentials from .env file

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')
PANCARD = config('PANCARD')
APPID = config('APPID')
SECRETID = config('SECRETID')


def generate_token_url(app_id, secret_id):
    """ This function will generate the url which contains the Access Token

    Parameters:
    -----------
    app_id: string
        App Id is generated when we create an app in Fyers API. Saved in .env file as APPID
    secret_id: string
        Secret Id is generated when we create an app in Fyers API. Saved in .env file as SECRETID

    Returns:
    --------
    url_with_token: string
        It returns the url which contains the token of the kind
        https://127.0.0.1?access_token=gAAAAABc3Sh9QpE5mNx2mSz6vvvT29SAsELqkfbKQKa2977zHw3NdPBhe6jAZCBumHvYUum87j53-AzMEPXMjQw31wkRviZ1TdM5OimgTYWEEorWDmWuHnY=&user_id=FYXXXX
    """

    app_session = accessToken.SessionModel(app_id, secret_id)
    response = app_session.auth()
    # Check if we gets the response
    if response["code"] != 200:
        sys.exit()
        print('Error- Response Code != 200')
    # Get Authorization Code
    auth_code = response['data']['authorization_code']
    app_session.set_token(auth_code)
    # Get URL with the Authorization Code
    generate_token_url = app_session.generate_token()
    # Open the URL in browser
    driver.get(generate_token_url)
    # Get credentials elements from the html
    user_name = driver.find_element_by_id('fyers_id')
    password = driver.find_element_by_id('password')
    pan_card = driver.find_element_by_id('pancard')
    submit_button = driver.find_element_by_id('btn_id')
    # Fill in the credentials
    user_name.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    pan_card.send_keys(PANCARD)
    submit_button.click()
    # Wait for a while so that the url changes
    time.sleep(30)
    # Get the current URL (which contains access token)
    url_with_token = driver.current_url
    driver.quit() # Close the browser
    return url_with_token


def extract_token(full_url):
    """ This function extracts the Access Token from the complete url returned by generate_token_url() function using regex.

    Parameters:
    -----------
    full_url: str
        It is the complete url returned by generate_token_url
        https://127.0.0.1?access_token=gAAAAABc3Sh9QpE5mNx2mSz6vvvT29SAsELqkfbKQKa2977zHw3NdPBhe6jAZCBumHvYUum87j53-AzMEPXMjQw31wkRviZ1TdM5OimgTYWEEorWDmWuHnY=&user_id=FYXXXX

    Returns:
    access_token : sting > pickle
        It returns the access token in str format and later on saves it as a pickle in a file called fyers_token.pickle
        This access token is valid through 7-8 AM of the next day.
    """
    access_token = re.search(r'(?<=https://127.0.0.1/\?access_token=).*?(?=user_id=RP0015)', full_url).group(0)
    if access_token:
        with open('fyers_token.pickle', 'wb') as f:
            pickle.dump(access_token, f)
    else:
        print("No token generated")


def main():
    full_url = generate_token_url(APPID, SECRETID)
    extract_token(full_url)


if __name__ == '__main__':
    main()
