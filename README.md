# SaralGyaan - Automatically Generate Access Token for your FYERS API

A Python Script to automatically generate Access Token for your [FYERS API](https://fyers.in?id=RP0015)

## Pre-requisites
* An account with FYERS. If you don't have an account, you can open the same using this [link](https://open-an-account.fyers.in/?id=RP0015)
* Chromium Driver (Chrome) or Gecko Driver (Mozilla) for Selenium. You can download the [Chromium Driver](https://chromedriver.chromium.org/downloads) or [Gecko Driver](https://github.com/mozilla/geckodriver/releases) depending upon your operating System.
* The Chromium Driver or the Gecko Driver should be in the directory, which has been added to the PATHs of your System.

## Requirements
* Python 3
* fyers_api
* selenium
* python-decouple

You can use the following command to install the necessary modules
```
pip install -r requirements.txt
```

## Installation
Either download the directory or clone it using
```
git clone https://github.com/uditvashisht/Generate_Access_Token_FYERS_API.git
```
```
cd Generate_Access_Token_FYERS_API
python3 -m venv . #You can use python or python3 or python3.8 depending on your system
source bin/activate
pip install -r requirements.txt
```
## Usage
Change the .env file and add your details in it
```
USERNAME=YOUR_USERNAME
PASSWORD=YOUR_PASWORD
PANCARD=YOUR_PANCARD
APPID=YOUR_APPID
SECRETID=YOUR_SECRETID
```
You can generate the Access Token in your system by running
```
python create_access_token.py
```

And later on call the API using
```
python call_api.py
```
## Usage Guide
You can also check the detailed [video tutorial]() on Youtube.

## License

© 2020 Udit Vashisht
This repository is licensed under the MIT license. See LICENSE for details.
