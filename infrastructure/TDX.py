import requests
import urllib.parse
import json
import constants

class tdxService():
  __base_path = 'tdx.transportdata.tw'
  __client_id = constants.TDX_CLIENT_ID
  __client_secret = constants.TDX_CLIENT_SECRET

  def __init__(self):
    self.accessToken =  self.getAccessToken()

  def getAccessToken(self) -> str:

    try:
        url = f"https://{self.__base_path}/auth/realms/TDXConnect/protocol/openid-connect/token"

        data = {
            "grant_type": "client_credentials",
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            return response.json()['access_token']
        else:
            print(f"Getting response status error: {response.status_code}")
    except Exception as e:
        print(f"Unexpected error: {e}")

  async def getRouteInfo(self, city:str, name:str):
    '''
    /v2/Bus/Route/City/{City}/{RouteName}
    取得指定[縣市],[業者編號]的市區公車動態資料
    '''
  
    try:

      url = f"https://{self.__base_path}/api/basic/v2/Bus/Route/City/{city}/{urllib.parse.quote(name)}?%24top=30&%24format=JSON"

      headers = {
          "Content-Type": "application/x-www-form-urlencoded",
          "Authorization": f"Bearer {self.accessToken}"
      }

      response = requests.get(url, headers=headers)

      res = json.loads(response.text)

      # Handle the response here
      if response.status_code == 200:
          return res[0]
      else:
        print(f"Getting response status error: {response.status_code}")
    except Exception as e:
        print(f"Unexpected error: {e}")
      
  async def getStopOfRoute(self, city:str, name:str):
    '''
    /v2/Bus/StopOfRoute/City/{City}/{RouteName}
    取得指定[縣市],[業者編號]的市區公車動態資料
    '''
  
    try:

      url = f"https://{self.__base_path}/api/basic/v2/Bus/StopOfRoute/City/{city}/{urllib.parse.quote(name)}?%24format=JSON"

      headers = {
          "Content-Type": "application/x-www-form-urlencoded",
          "Authorization": f"Bearer {self.accessToken}"
      }

      response = requests.get(url, headers=headers)

      res = json.loads(response.text)

      # Handle the response here
      if response.status_code == 200:
          return res
      else:
        print(f"Getting response status error: {response.status_code}")
    except Exception as e:
        print(f"Unexpected error: {e}")
      
  async def getRealTimeNearStop(self, city:str, name:str):
    '''
    /v2/Bus/RealTimeByFrequency/City/{City}/{RouteName}
    取得指定[縣市],[業者編號]的市區公車動態資料
    '''
    try:

      url = f"https://{self.__base_path}/api/basic/v2/Bus/RealTimeNearStop/City/{city}/{urllib.parse.quote(name)}?%24format=JSON"

      headers = {
          "Content-Type": "application/x-www-form-urlencoded",
          "Authorization": f"Bearer {self.accessToken}"
      }

      response = requests.get(url, headers=headers)

      res = json.loads(response.text)

      # Handle the response here
      if response.status_code == 200:
          return res
      else:
          print(f"Getting response status error: {response.status_code}")
    except Exception as e:
        print(f"Unexpected error: {e}")
      