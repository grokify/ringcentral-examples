# 1) Load Environment with Credentials
# $ pip3 install -U python-dotenv
import os
from dotenv import load_dotenv

env_path = os.getenv("ENV_PATH")
if env_path is not None and len(env_path)>0:
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

# 2) Instantiate SDK
# $ pip3 install -U ringcentral
from ringcentral import SDK

sdk = SDK(
    os.getenv('RINGCENTRAL_CLIENT_ID'),
    os.getenv('RINGCENTRAL_CLIENT_SECRET'),
    os.getenv('RINGCENTRAL_SERVER_URL'))

platform = sdk.platform()
platform.login(
    os.getenv('RINGCENTRAL_USERNAME'),
    os.getenv('RINGCENTRAL_EXTENSION'),
    os.getenv('RINGCENTRAL_PASSWORD'))

# 3) Make Call Log Query
try:
    from urllib import urlencode
except: # For Python 3
    from urllib.parse import urlencode

query = {
    'dateFrom': '2018-05-01T00:00:00Z',
    'dateTo': '2018-06-01T00:00:00Z',
    'direction': 'Outbound',
    'type': 'Voice',
    'view': 'Detailed'}

qs = urlencode(query)

res = platform.get('/restapi/v1.0/account/~/extension/~/call-log?'+qs)

print(res.text())