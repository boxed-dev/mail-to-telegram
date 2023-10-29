# Gmail Email Notifier Bot

This Python script allows you to retrieve unread emails from your Gmail account and send notifications to a Telegram channel. It uses the Gmail API to fetch emails and the Telegram Bot API to send notifications. Here's how to set it up and use it:

## Prerequisites

Before using this script, you need to set up a few things:

1. **Google API Credentials:**
   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project and enable the Gmail API.
   - Create OAuth 2.0 credentials and download the JSON file.
   - Save the JSON file as `credentials.json` in the same directory as this script.

2. **Telegram Bot:**
   - Create a Telegram bot and get your bot token. You can do this by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

3. **Telegram Channel:**
   - Create a Telegram channel where you want to receive email notifications.
   - Invite your bot to the channel and give it permission to post messages.

4. **Python Libraries:**
   - Make sure you have installed the required Python libraries. You can install them using `pip`:
     ```bash
     pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client telegram
     ```

## Usage

1. Clone the repository or download the script to your local machine.

2. Run the script using Python:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of your Python script.

3. The script will prompt you to authenticate your Google account. Follow the provided link, log in, and grant the necessary permissions to the application.

4. After successful authentication, the script will fetch the latest unread emails (up to 4) from your Gmail account.

5. It will send notifications to the specified Telegram channel with the sender, subject, and the email body.

6. You can customize the maximum number of emails fetched by modifying the `maxResults` variable in the `getEmails` function.

## Telegram Bot Token

Replace the `BOT_TOKEN` variable in the script with your Telegram bot token. Make sure the bot has access to the Telegram channel you want to use for notifications.

## Disclaimer

This script is a basic example and may require further enhancements and error handling for production use. Please use it responsibly and ensure your credentials are kept secure.

Feel free to reach out if you have any questions or need assistance with this script.

---

📧 For questions and support, please contact me: [Your Contact Information]

📝 Feel free to contribute to this project and make it even better!
