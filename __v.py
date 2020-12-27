# Donator Groups

import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest, StartBotRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

option = ["Dogecoin_click_bot", "Litecoin_click_bot", "BCH_clickbot", "Zcash_click_bot", "Bitcoinclick_bot"] #Bot option list
url_channel = option[int(sys.argv[2])]

stp = ["6rtwl","aZlJK","tS2jw","OZJhb","j322s"]
stpp = stp[int(sys.argv[2])]

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=20)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]

async def main():
	print(Fore.GREEN + "Telegram Crypto Bot by WebmasterLordkelly\n(@onumahkalusamuel)..." + Fore.RESET)
	print(Fore.GREEN + url_channel + Fore.RESET + " selected.\n")
	bot_action = "Visit"
	try:
		print("Visit performed")
		# Check if phone number is not specified
		if len(sys.argv) < 2:
			print('-> Input number in international format (example: +639162995600)\n')
			exit(1)

		phone_number = sys.argv[1]

		if not os.path.exists("session"):
			os.mkdir("session")

		# Connect to client
		client = TelegramClient('session/' + phone_number, api_id, api_hash)
		await client.start(phone_number)
		me = await client.get_me()

		print('Current account:' + Fore.CYAN + f'{me.first_name}({me.username})\n' + Fore.RESET)
		print_msg_time(Fore.YELLOW + 'Sending /visit command' + Fore.RESET)

		# Start command /visit
		await client(StartBotRequest(bot=url_channel,peer=url_channel,start_param=stpp))
		await client.send_message(url_channel, '/visit')

		# Start visiting the ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def visit_ads(event):

			try:
				original_update = event.original_update
				if type(original_update)is not UpdateShortMessage:
					if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
						url = event.original_update.message.reply_markup.rows[0].buttons[0].url

						if url is not None:
							print_msg_time('Visiting website...')

							# Parse the html of url
							(status_code, text_response) = get_response(url)
							parse_data = BeautifulSoup(text_response, 'html.parser')
							captcha = parse_data.find('div', {'class':'g-recaptcha'})

							# Captcha detected
							if captcha is not None:

								print_msg_time(Fore.RED + 'Captcha detected!'+ Fore.RED +' Skipping ads...\n')
								# Clicks the skip
								await client(GetBotCallbackAnswerRequest(
									peer=url_channel,
									msg_id=event.message.id,
									data=event.message.reply_markup.rows[1].buttons[1].data
								))
			except:
				await client(GetBotCallbackAnswerRequest(
					peer=url_channel,
					msg_id=event.message.id,
					data=event.message.reply_markup.rows[1].buttons[1].data
				))

				print_msg_time(Fore.RED + "Error occured while visiting website..." + Fore.RESET)
		# Print earned money
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def wait_hours(event):
			message = event.raw_text
			if 'You earned' in message:	
				print_msg_time(Fore.GREEN + f'{message}' + Fore.RESET)

		# Print earned money
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def manual_skip(event):
			message = event.raw_text
			if 'Skipping task...' in message:	
				print_msg_time(Fore.YELLOW + f'{message}' + Fore.RESET)

		# No longer valid
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_valid(event):
			message = event.raw_text
			if 'Sorry, that task is no longer valid' in message:	
				print_msg_time(Fore.RED + 'Sorry, that task is no longer valid.' + Fore.RESET)
				print_msg_time(Fore.YELLOW + 'Sending /visit command' + Fore.RESET)
				await client.send_message(url_channel, '/visit')

		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:	
				print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)
				exit(1)
	except:
		print("Something went wrong running visits...")
		exit(1)
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
