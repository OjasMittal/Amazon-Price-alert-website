from selenium import webdriver
import yagmail
import os
from twilio.rest import Client


def get_driver(urll):

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features-AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(urll)
    return driver


def email(value,urll,id):
    sender = "automail.ojas.python@gmail.com"
    receiver = id
    subject = "Amazon product value changed "
    yag = yagmail.SMTP(user=sender, password=os.getenv("PASS"))
    contents = f"""Hey!!
  The product value at Amazon is now: {value}
  Buy Now!!
  {urll}"""
    yag.send(to=receiver, subject=subject, contents=contents)


def clean_text(text):
    """Extract only the value from text"""

    output = float(text.lstrip('$'))
    return output


def send_sms(value,no,urll):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
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