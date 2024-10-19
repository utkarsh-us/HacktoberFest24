# TeleTwilio
 TeleTwilio is a Telegram bot Script that allows users to send text messages using the Twilio API.

### Features
- Send SMS: Easily send SMS messages by using the /send command followed by the recipient's phone number and your message.

- Confirmation: The bot provides a confirmation prompt before sending the message.

### Requirements

- Telegram API Credentials
- Twilio Account SID and Auth Token
- Firebase Realtime Database (for logging)

### Setup

1. Clone the Repository

    ```sh
    git clone https://github.com/riz4d/TeleTwilio.git
    ```
    ```sh
    cd TeleTwilio
    ```

2. Install Dependencies

    ```sh
    pip install -r requirements.txt
    ```

3. Configure the Bot

    - Put configs/telegram.py file with your Telegram API credentials:

    - Put configs/firebase.py file with your Firebase configuration:

    - Put a configs/twilioconf.py file with your Twilio credentials:

4. Run the Bot

    ```sh
    python bot.py
    ```

### Usage

- Send a Message: Use the /send command followed by the recipient's phone number and your message.<br>Example:

    ```kotlin
    /send +1234567890 Hello
    ```

### Notes:

- Firebase Setup: Make sure your Firebase database rules allow appropriate access as per your security requirements.

- Twilio Configuration: Replace placeholders with your actual Twilio account details and phone number.

- Bot Security: Consider enhancing the security of commands and messages involving sensitive information.