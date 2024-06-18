from infrastructure.TDX import tdxService

class busRepository():

    def __init__(self):
        self.tdxService = tdxService()

    def queryCondition(self, city: str, routeName: str ):
        self.city = city
        self.routeName = routeName

    def busDistanceFilter(self, busCurrentStop:int):

        dis = busCurrentStop['StopSequence'] - self.StopSequence
        return  self.min_distance <= dis and dis <= self.max_distance

    async def getBusStops(self):
        try:
            resp = await self.tdxService.getStopOfRoute(self.city, self.routeName)        

            if resp is None:
                return []
            
            routes = list(filter(lambda item: item["RouteName"]["Zh_tw"] == self.routeName and item["Direction"] == self.direction, resp))

            stops = [item['StopName']['Zh_tw'] for item in routes[0]["Stops"]]
            
            return stops
        except Exception as e:
            print("Error in busRepository.getBusStops:", e)

    async def getBusNearby(self, StopSequence: int, direction: int, min_distance: int = 3, max_distance: int = 5) -> bool:
        """ 
            Get nearby bus with specific conditions

            :StopSequence: 站牌序列編號(自 1 開始)
            :direction: 車輛行駛方向 (0:去程，1:返程)
            :min_distance: 最小站距
            :max_distance: 最大站距
        """
        try:
            self.StopSequence = StopSequence
            self.direction = direction
            self.min_distance = min_distance
            self.max_distance = max_distance

            busStatus = await self.tdxService.getRealTimeNearStop(self.city, self.routeName)

            if busStatus is None:
                return []

            sameDirectionBus = list(filter(lambda x: x["Direction"] == self.direction, busStatus))

            validConditionBus = list(filter(self.busDistanceFilter, sameDirectionBus))
            
            return validConditionBus
        
        except Exception as e:
            print("Error in busRepository.getBusNearby:", e)
