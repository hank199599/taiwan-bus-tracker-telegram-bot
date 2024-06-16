import requests
import json
import constants

class TelegramService:
  __bot_token = constants.TELEGRAM_BOT_TOKEN
  
  async def getUpdates(self):
    try:
      url = f"https://api.telegram.org/bot{self.__bot_token}/getUpdates"

      response = requests.get(url)

      res = json.loads(response.text)

      # Handle the response here
      if response.ok == True:
          print(res)
          return res
      else:
          print(f"Getting response status error: {response.status_code}")
    except Exception as e:
        print(f"Unexpected error: {e}")
      
  async def SendMessage(self, chat_id:str, message: str):
    
    url = f"https://api.telegram.org/bot{self.__bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    resp = requests.get(url, params=params)

    # Throw an exception if Telegram API fails
    resp.raise_for_status()  
