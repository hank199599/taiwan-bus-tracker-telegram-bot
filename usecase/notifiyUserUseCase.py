from repository.notifyServiceRepository import notifyServiceRepository
from repository.busRepository import busRepository
from infrastructure.realTimeDB import RealTimeDatabase

class notifyUserUseCase():
  __dataPath = 'user'
  def __init__(self):
    self.busService = busRepository()
    self.notifyService = notifyServiceRepository()
    self.db = RealTimeDatabase()

  def messageGen(self, routeName:str, busDist:str, plateNumber:str, busStopName:str, distance: int):
    return f'''【{busStopName} 即將進站 (距離 {distance} 站)】
    路線：{routeName}
    終點站:{busDist}
    車牌：{plateNumber}'''

  async def getBusStopNames(self):
    stops = await self.busService.getBusStops()

    if stops is None:
      return ''
    
    return stops
  
  async def exec(self):
    data = await self.db.getData(f"{self.__dataPath}/")
    # print(data)
    for user, cities in list(data.items()):
      for city, routes in list(cities.items()):
        for route in routes: 
          for routeName, details in list(route.items()):
            for detail in details:
              # print(user,city,routeName,details)
              self.busService.queryCondition(city,routeName)
              buses = await self.busService.getBusNearby(detail['StopSequence'],detail['direction'])

              if buses is not None:
                for bus in buses:
                  stops = await self.busService.getBusStops()

                  busDist = stops[len(stops)-1]
                  targetStopName = stops[detail['StopSequence']-1]
                  distance = detail['StopSequence'] - bus['StopSequence']

                  notifyMessage = self.messageGen(routeName, busDist, bus['PlateNumb'], targetStopName, distance)
                  await self.notifyService.notifyUser(user,notifyMessage)
