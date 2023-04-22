from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import base64
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

sub = []
fr = []
mes = []
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

async def send_message(bot, chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)

async def getEmails():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    result = service.users().messages().list(maxResults=4, userId='me').execute()
    messages = result.get('messages')

    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()

        try:
            payload = txt['payload']
            headers = payload['headers']

            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']

            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-","+").replace("_","/")
            decoded_data = base64.b64decode(data)

            soup = BeautifulSoup(decoded_data , "lxml")
            body = soup.body()

            sub.append(subject)
            fr.append(sender)
            mes.append(body)
            BOT_TOKEN = "5900304974:AAEPksNEuQrUNmlaP4JKn0xG7hhKQTBnEXk"
            async with Bot(BOT_TOKEN) as bot:
                message = f"New unread email:\nFrom: {sender}\nSubject: {subject}\nMessage: {body}"
                print(message)
                await send_message(bot, "@vitmail", message)

        except:
            pass

async def main():
    await getEmails()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
