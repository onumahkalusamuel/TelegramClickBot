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

p = open('phone.txt', 'r')
phones = p.readlines()
def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]

async def main():
	print(Fore.GREEN + "Telegram Crypto Bot by WebmasterLordkelly..." + Fore.RESET)
	print(Fore.GREEN + "Activating Account..." + Fore.RESET)

	total = len(phones)-1
	for phone in phones:
		phone_number = phone.strip()
		if not os.path.exists("session"):
			os.mkdir("session")

		print(f'Activating {phone_number}...')

		# Connect to client
		client = TelegramClient('session/' + phone_number, api_id, api_hash)
		await client.start(phone_number)
		me = await client.get_me()
		await client(StartBotRequest(bot="Dogecoin_click_bot",peer="Dogecoin_click_bot",start_param="6rtwl"))
		await client(StartBotRequest(bot="Litecoin_click_bot",peer="Litecoin_click_bot",start_param="aZlJK"))
		await client(StartBotRequest(bot="BCH_clickbot",peer="BCH_clickbot",start_param="tS2jw"))
		await client(StartBotRequest(bot="Zcash_click_bot",peer="Zcash_click_bot",start_param="OZJhb"))
		await client(StartBotRequest(bot="Bitcoinclick_bot",peer="Bitcoinclick_bot",start_param="j322s"))
		
		print('Account: ' + Fore.CYAN + f'{me.first_name} ({me.username})' + Fore.RESET)
		print_msg_time(Fore.YELLOW + 'Activated...\n' + Fore.RESET)

		if phones.index(phone) == total:
			exit(1)

	await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())
