# TELEGRAM CLICK BOT

# **INTRODUCTION**
This bot helps you claim rewards on telegram crypto bots. 5 popular click bots on telegram are available. Simply follow the instructions below to be up and running in no time. It runs automatically.
**Also read the `caveats` section**

**The 5 click bots are:**
DOGE Click Bot  
LTC Click Bot  
BCH Click Bot  
Zcash Click Bot  
BTC Click Bot  

This script pauses for **60 seconds** after each full cycle of Join or Meessage operations for all bots  

# **INSTALLATION**
This bot runs on Android via Termux and on *nix based system via terminal.
Install termux from PlayStore. On a *nix system, ensure you have `nano` and `python3` installed. 
Install with the appropriate package manager.
To use the bot on Android, you need to run the following commands in Termux:  

> apt update --pkg upgrade  

> apt install python git  

> git clone https://github.com/onumahkalusamuel/TelegramClickBot  

> cd TelegramClickBot  

# **SETUP**
Setup is very straightforward. Ensure you have `nano` and `python` installed. Then run the following command:

> bash setup.sh  

# **ACTIVATION**
To activate bot, edit `phone.txt`

> nano phone.txt  

and add numbers **in international format** (e.g. +233xxxxxxxxx)  
Each number **must** be on a separate line  
  
Then run the following code to finish activation:  
# android
> python activate.py  

# *nix
python3 activate.py

A code will be sent to the telegram account. Copy and enter the code when prompted for each phone number.  
  
**Note:** If you add any number, you **must** run the above code again to activate the number.  

# **EXECUTE**
Run the following code:  

> bash run.sh  

# **CAVEATS**
If you notice that a bot action has taken over 30 seconds, you need to go to the telegram account and either complete that action manually or skip it for the bot to continue...  

# **CREDITS**
Thanks to SirGibbs for drawing my attention to Telegram Bots
Thanks to Jason for disturbing me to update the script again
