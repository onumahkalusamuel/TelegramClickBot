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

inc = int(sys.argv[2])

url_channel = option[inc]

stp = ["6rtwl","aZlJK","tS2jw","OZJhb","j322s"]

stpp = stp[inc]

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]

async def main():
	print(Fore.GREEN + "Telegram Crypto Bot by WebmasterLordkelly\n(@onumahkalusamuel)..." + Fore.RESET)
	print(Fore.GREEN + url_channel + Fore.RESET + " selected.\n")
	answer = "Join"
	try:
		print(answer + " performed")
				# Check if phone number is not specified
		if len(sys.argv) < 2:
			exit(1)

		phone_number = sys.argv[1]

		if not os.path.exists("session"):
			os.mkdir("session")

		# Connect to client
		client = TelegramClient('session/' + phone_number, api_id, api_hash)
		await client.start(phone_number)
		me = await client.get_me()

		print('Current account:' + Fore.CYAN + f'{me.first_name}({me.username})\n' + Fore.RESET)
		print_msg_time('Sending /join command')

		# Start command /join
		await client(StartBotRequest(bot=url_channel,peer=url_channel,start_param=stpp))
		await client.send_message(url_channel, '/join')

		# Join the channel
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def join_start(event):
			channel_name = None
			try:
				message = event.raw_text
				if 'You must join' in message:
					channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
					print_msg_time(f'Joining @{channel_name}...')

					# Join the channel
					await client(JoinChannelRequest(channel_name))
					print_msg_time(f'Verifying...')

					# Clicks the joined
					await client(GetBotCallbackAnswerRequest(
						peer=url_channel,
						msg_id=event.message.id,
						data=event.message.reply_markup.rows[0].buttons[1].data
					))
				elif 'Go to ' in message:
					url = event.original_update.message.reply_markup.rows[0].buttons[0].url
					print_msg_time(f'URL @{url}')
					(status_code, text_response) = get_response(url)
					p_d = BeautifulSoup(text_response, 'html.parser')
					b_t = p_d.find('a', {'class', 'tgme_action_button_new'})
					new_url= b_t.get('href')
					channel_msg = new_url
					if '&' in channel_msg:
						channel_name = re.search(r'resolve\?domain\=(.*?)\&', channel_msg).group(1)
					elif '&' not in channel_msg:
						channel_name = re.search(r'resolve\?domain\=(.*)', channel_msg).group(1)

					print_msg_time(f'Joining @{channel_name}...')

					# Join the channel
					await client(JoinChannelRequest(channel_name))
					print_msg_time(f'Verifying...')

					# Clicks the joined
					response = await client(GetBotCallbackAnswerRequest(
						peer=url_channel,
						msg_id=event.message.id,
						data=event.message.reply_markup.rows[0].buttons[1].data
					))

			except:
				if channel_name is not None:
					await client(GetBotCallbackAnswerRequest(
								peer=url_channel,
								msg_id=event.message.id,
								data=event.message.reply_markup.rows[1].buttons[1].data
							))

				print(Fore.RED + f'Unable to Join group/channel at the moment...Skipping if possible...' + Fore.RESET)
				exit(1)


		# Print waiting hours
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def wait_hours(event):
			message = event.raw_text
			if 'You must stay' in message:	
				waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
				print_msg_time(Fore.GREEN + f'Success! Please wait {waiting_hours} to earn reward\n' + Fore.RESET)
				
		# Cannot finf
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def cannot_find(event):
			message = event.raw_text
			if 'We cannot find' in message:
				print_msg_time(Fore.YELLOW + f'{message}\n' + Fore.RESET)

		# Skipping
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def manual_skip(event):
			message = event.raw_text
			if 'Skipping task...' in message:	
				print_msg_time(Fore.YELLOW + f'{message}' + Fore.RESET)

		#for when task no longer valid
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_longer_valid(event):
			message = event.raw_text
			if 'no longer valid' in message:	
				print_msg_time(Fore.YELLOW + f'{message}' + Fore.RESET)

		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:	
				print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)
				exit(1)
	except:
		print("Unable to process joins...")
		exit

	
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
