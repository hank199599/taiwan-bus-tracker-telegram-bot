from repository.notifyServiceRepository import notifyServiceRepository
from repository.busRepository import busRepository
from infrastructure.realTimeDB import RealTimeDatabase

class notifyUserUseCase():
  __dataPath = 'user'
  def __init__(self):
    self.busService = busRepository()
    self.notifyService = notifyServiceRepository()
    self.db = RealTimeDatabase()

  def messageGen(self, routeNumber, busDist, plateNumber, busStopName):
    return f'''【{busStopName} 到站通知】
    路線：{routeNumber} ( 往{busDist})
    車牌：{plateNumber}'''

  async def getBusStopName(self,StopSequence):
    stops = await self.busService.getBusStops()

    if stops is None:
      return ''
    
    return stops[StopSequence-1] if StopSequence < len(stops) else ''
  
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
                  busDist = await self.busService.getBusDestination(detail['direction'])
                  targetStopName = await self.getBusStopName(detail['StopSequence'])

                  notifyMessage = self.messageGen(routeName, busDist, bus['PlateNumb'], targetStopName)
                  await self.notifyService.notifyUser(user,notifyMessage)
