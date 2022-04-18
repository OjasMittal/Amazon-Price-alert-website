from selenium import webdriver
import yagmail
from twilio.rest import Client
from selenium.webdriver.chrome.service import Service

import os
def get_driver(urll):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("disable-blink-features-AutomationControlled")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(urll)
    return driver





#def get_driver(urll):
    #service = Service('chromedriver.exe')
    #options = webdriver.ChromeOptions()
    #options.add_argument("disable-infobars")
    #options.add_argument("start-maximized")
    #options.add_argument("disable-dev-shm-usage")
    #options.add_argument("no-sandbox")
    #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #options.add_argument("disable-blink-features-AutomationControlled")
    #driver = webdriver.Chrome(service=service,options=options)
    #driver.get(urll)
    #return driver



def email(value,urll,id):
    sender = "automail.ojas.python@gmail.com"
    receiver = id
    subject = "Amazon product value changed "
    yag = yagmail.SMTP(user=sender, password='ilhx hvvw yanv grfz')
    contents = f"""Hey!!
  The product value at Amazon is now: {value}
  Buy Now!!
  {urll}"""
    yag.send(to=receiver, subject=subject, contents=contents)


def clean_text(text):
    """Extract only the value from text"""

    output = float(text.lstrip('$'))
    return output


def send_sms(value,no,urll,ac_id,key):
    account_sid = ac_id
    auth_token = key
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"""Hey!!
  The product value at Amazon is now: {value}
  Buy Now!!
  {urll}
                     """,
        from_='+16203159923',
        to=no
    )

    print(message.sid)