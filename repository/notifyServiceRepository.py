from infrastructure.telegram import TelegramService

class notifyServiceRepository():

  def __init__(self):
    self.notifyService = TelegramService()

  async def notifyUser(self,userId:str,message:str):
    try:
      await self.notifyService.SendMessage(userId,message)
    except Exception as e:
      print("Error in notifyServiceRepository.notifyUser",e)