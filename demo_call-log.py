# 1) Load Environment with Credentials
# $ pip3 install -U python-dotenv
import os
from pathlib import Path  # python3 only
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=os.getenv('ENV_PATH'))

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
    'type': 'Voice',
    'direction': 'Outbound',
    'dateFrom': '2018-05-01T00:00:00Z',
    'dateTo': '2018-06-01T00:00:00Z',
    'view': 'Detailed'}

qs = urlencode(query)

res = platform.get('/restapi/v1.0/account/~/extension/~/call-log?'+qs)

print(res.text())