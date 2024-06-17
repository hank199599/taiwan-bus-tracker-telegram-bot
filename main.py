import base64
import functions_framework
from cloudevents.http import CloudEvent
from usecase.notifiyUserUseCase import notifyUserUseCase
import asyncio

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def subscribe(cloud_event:CloudEvent) -> None:
    # Print out the data from Pub/Sub, to prove that it worked
    print(
        "Hello, " + base64.b64decode(cloud_event.data["message"]["data"]).decode() + "!"
    )
    usecase = notifyUserUseCase()
    asyncio.run(usecase.exec())