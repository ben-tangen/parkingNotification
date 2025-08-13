from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "ben.tangen0234@gmail.com"  # Gmail sender
    # Read password from file
    with open("email_password.txt", "r") as f:
        sender_password = f.read().strip()
    receiver_email = "ben.tangen0234@gmail.com"  # Email recipient

    subject = "Blue Pass Available!"
    body = "Blue Pass is AVAILABLE! Go to the website to claim it."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent to", receiver_email)
    except Exception as e:
        print("Failed to send email:", e)


# Suppress ChromeDriver logs
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # Suppress most logs
service = Service(log_path='chromedriver.log')  # Redirect logs to file

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://usu.t2hosted.com/cmn/auth_ext.aspx")

# Log in manually first time, then continue
input("Log in and press Enter here...")

last_refresh = time.time()
number_of_refreshes = 0

while True:
    # If redirected, navigate back and confirm
    if driver.current_url != "https://usu.t2hosted.com/per/selectpermit.aspx":
        driver.get("https://usu.t2hosted.com/per/index.aspx")
        time.sleep(2)
        try:
            # Click confirm button 3 times to return to the desired page
            for i in range(3):
                confirm_button = driver.find_element(By.ID, "ctl00_ctl01_MainContentPlaceHolder_T2Main_cmdNext")
                confirm_button.click()
                time.sleep(2)
            print("Clicked confirm button to return to desired page.")
            time.sleep(2)
        except Exception as e:
            print("Confirm button not found or error clicking:", e)

    # Refresh every 60 seconds to keep session up-to-date
    driver.refresh()
    
    number_of_refreshes+= 1
    print(f"Total refreshes: {number_of_refreshes}.")

    # Check for blue pass availability
    try:
        # Look for a label containing 'BLUE' (case-insensitive)
        blue_pass_elements = driver.find_elements(By.XPATH, "//label[contains(translate(text(), 'blue', 'BLUE'), 'BLUE')]")
        if blue_pass_elements:
            print("Blue Pass is AVAILABLE!")
            send_email()
        else:
            print("Blue Pass is not available. \n" )
    except Exception as e:
        print(f"Error checking Blue Pass: {e}")

    time.sleep(60)  # Check every 60 seconds