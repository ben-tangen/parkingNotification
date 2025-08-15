# Parking Pass Notification

A Python script that monitors the USU parking pass website and sends an email notification when a Blue Pass becomes available.

## Features
- Uses Selenium to automate browser actions
- Sends email notifications when a Blue Pass is detected
- Automatically handles session redirects and confirmation

## Setup
1. Clone this repository.
2. Install required Python packages:
   ```bash
   pip install selenium
   ```
3. Download ChromeDriver and ensure it matches your Chrome version.
4. Add your Gmail app password to `email_password.txt` (this file is ignored by Git).
5. Change the Gmail addresses for desired sender and reciever.

## Usage
Run the script:
```bash
python parking_pass_notification.py
```

Follow the prompt to log in manually the first time. The script will then monitor the page and notify you when a Blue Pass is available.

## License
This project is private and not licensed for public use, modification, or distribution.

Date: August 14, 2025

## Author
ben-tangen
