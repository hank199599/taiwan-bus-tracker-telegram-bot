import firebase_admin
import constants
from firebase_admin import credentials
from firebase_admin import db

# config content downloaded from Firebase
config = {}


cred = credentials.Certificate(config)
dbUrl = constants.FIREBASE_REALTIME_DB_PATH

firebase_admin.initialize_app(cred, {
    'databaseURL': dbUrl
})

class RealTimeDatabase():
    
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