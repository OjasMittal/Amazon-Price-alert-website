import streamlit as st
from pyrebase import initialize_app
import functions
import time
from PIL import Image
#secret = '2921d4f2d89ab0a7ec7239783a567197'



img=Image.open('icon1.png')
st.set_page_config(page_title="Amazon Price Alert",page_icon=img)

firebaseConfig = {
    'apiKey': "AIzaSyCIGH1T226lrzpvPfBBj_gVxQFcYhgF8B8",
    'authDomain': "price-alert-d685d.firebaseapp.com",
    'projectId': "price-alert-d685d",
    'databaseURL': "https://price-alert-d685d-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "price-alert-d685d.appspot.com",
    'messagingSenderId': "611217487779",
    'appId': "1:611217487779:web:ca956ff3a8bdb2a0d80c16",
    'measurementId': "G-X75ECNWBFZ"
};

firebase = initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

st.title("Amazon Price Alert Tool")
st.subheader('Wanna save some bucks :dollar:? Buy when things go Cheap!! :smile:  ')
st.info("Sign Up/Login to start using the services in Beta Mode")
col1, col2, col3 = st.columns(3)
with col2:
    image = Image.open('download.jpg')
    st.image(image, caption='The price of anything is the amount of life you exchange for it. – Henry David Thoreau',
             width=400)
st.sidebar.title("WELCOME!")
choice = st.sidebar.selectbox('Login/SignUp', ['Login', 'Sign up'])
email = st.sidebar.text_input("Enter your email address")
password = st.sidebar.text_input("Enter your password", type="password")
hide_menu_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)



if choice == "Sign up":
    handle = st.sidebar.text_input("Please enter your nickname", value="Cool Panda")
    submit = st.sidebar.button('Create my Account')
    if submit:
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Your account is created successfully!")
            st.balloons()
            user = auth.sign_in_with_email_and_password(email, password)
            db.child(user['localId']).child("Handle").set(handle)
            db.child(user['localId']).child("Id").set(user['localId'])
            st.title("Welcome " + handle + " !")
        except:
            st.info("This account already exists !")

st.info("Login through login option in the left drop down menu to use the services")
if choice == "Login":
    login = st.sidebar.checkbox('Login')
    if login:
        try:
            user = auth.sign_in_with_email_and_password(email, password)

            st.write(
                    "This app is designed to provide free sms and email alert services. Just post your Amazon link and your desired price for the product, we will Alert you as soon as the price drops")
            url = st.text_input('Paste the Amazon link of the product below')
            price = st.text_input('Enter the price below which you want to but it:')
            id = st.text_input('Enter your email on which you want to get notified: ')
            bio = st.radio('Do you want to receive alert on your phone no.? You will need a Twilio account for it', ['Yes', 'No'])
            st.write('<style>div.row-widget.stRadio > div {flex-direction:row;}</style>', unsafe_allow_html=True)
            if bio=="Yes":
                ac_id=st.text_input("Enter Twilio Account Sid")
                secret = st.text_input('Enter Twilio Auth. token')
                no = st.text_input('Enter mobile using +country code, eg: +91 : ')

                result = st.button("Monitor")
                if result:

                        driver=functions.get_driver(url)
                        time.sleep(8)
                        element = driver.find_element(by='xpath',
                                                      value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')

                        data = functions.clean_text(element.text)
                        print(data)
                        while True:
                            if data < float(price):
                                functions.email(element.text,url,id)

                                functions.send_sms(element.text,no,url,ac_id,secret)
                                st.write("Hurry! Prices are down now! Check your mail or messages")
                                break
                            else:
                                st.write("Price is high now! ")
                                st.write("You will receive an email and a SMS when price will go down")
                                time.sleep(3600)
            if bio=="No":
                result = st.button("Monitor")
                if result:

                    driver = functions.get_driver(url)
                    time.sleep(2)
                    element = driver.find_element(by='xpath',
                                                  value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')

                    data = functions.clean_text(element.text)
                    print(data)
                    while True:
                        if data < float(price):
                            functions.email(element.text, url, id)
                            st.write("Hurry! Prices are down now! Check your mail")
                            break
                        else:
                            st.write("Price is high now! ")
                            st.write("You will receive an email and a SMS when price will go down")
                            time.sleep(3600)
        except:
            st.info("Enter a valid email/password !")





