import firebase_admin
import constants
from firebase_admin import credentials
from firebase_admin import db

class RealTimeDatabase():
  __cred = credentials.Certificate(constants.FIREBASE_CONFIG_PATH)
  __dbUrl = constants.FIREBASE_REALTIME_DB_PATH

  def __init__(self):
    firebase_admin.initialize_app(self.__cred, {
    'databaseURL': self.__dbUrl
  })
    
  async def getData(self, path:str):
    ref = db.reference(path)
    data = ref.get()
    return data
  
  async def updateData(self, path: str, content: object ):
    ref = db.reference(path)
    ref.set(content)

  async def deleteData(self, path:str):
    ref = db.reference(path)
    ref.delete(path)