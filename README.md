# taiwan-bus-tracker-telegram-bot
> Reference: [Cloud Pub/Sub Tutorial (2nd gen)](https://cloud.google.com/functions/docs/tutorials/pubsub#functions-deploy-command-python) 
# System flow

![diagram](./diagram/system_flow.png)

# RealTimeDB Schema
```json
{
  "user": {
    "1307911377": {
      "Taipei": [
        {
          "672": [
            {
              "StopSequence": 7,
              "direction": 1
            }
          ]
        }
      ]
    }
  }
}
```
