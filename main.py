from usecase.notifiyUserUseCase import notifyUserUseCase
import asyncio

def __main__():
  usecase = notifyUserUseCase()
  asyncio.run(usecase.exec())

__main__()