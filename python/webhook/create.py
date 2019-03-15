import json
import os
from dotenv import load_dotenv
from ringcentral import SDK

env_path = os.getenv("ENV_PATH")
if env_path is not None:
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

sdk = SDK(os.getenv('RINGCENTRAL_CLIENT_ID'), os.getenv('RINGCENTRAL_CLIENT_SECRET'), os.getenv('RINGCENTRAL_SERVER_URL'))
platform = sdk.platform()
platform.login(os.getenv('RINGCENTRAL_USERNAME'), os.getenv('RINGCENTRAL_EXTENSION'), os.getenv('RINGCENTRAL_PASSWORD'))

print(os.getenv('RINGCENTRAL_USERNAME'))

paramsJSON = """{
  "eventFilters":[
    "/restapi/v1.0/account/~/extension/~/message-store/instant?type=SMS"
  ],
  "deliveryMode":{
    "transportType":"WebHook",
    "address":"https://87b6122f.ngrok.io/webhook"
  },
  "expiresIn":500000000
}"""
paramsDict = json.loads(paramsJSON)

response = platform.post('/restapi/v1.0/subscription', paramsDict)
#response = platform.get('/restapi/v1.0/account/~')

print(response.text())
