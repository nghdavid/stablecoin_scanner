import requests
import json
import os
from wallet import EthWallet, TronWallet
from dotenv import load_dotenv
from app.db.session import get_db
from sqlalchemy import text
from datetime import datetime, timedelta, timezone
load_dotenv()

api_key = os.environ.get('API_KEY')
tron_api_key = os.environ.get('TRON_API_KEY')
total_balance = 0
# for address in list(EthWallet.wallet.keys()):
#     # print("It is: "+EthWallet.wallet.get(address))
#     for contract_address in list(EthWallet.contract_address.keys()):
#         url = f"https://{EthWallet.scan_domain}/api?module=account&action=tokenbalance&contractaddress={contract_address}&address={address}&tag=latest&apikey={api_key}"
#         response = requests.request("GET", url)
#         amount = int(int(json.loads(response.text).get("result"))*EthWallet.ratio)
#         # print(EthWallet.contract_address.get(contract_address)+" "+str(amount))
#         total_balance += amount

headers = {
  'TRON-PRO-API-KEY': tron_api_key
}

for address in list(TronWallet.wallet.keys()):
    # print("It is: "+TronWallet.wallet.get(address))
    for contract_address in list(TronWallet.contract_address.keys()):
        url = f"https://{TronWallet.scan_domain}/api/account/tokens?&address={address}"
        response = requests.request("GET", url, headers=headers)
        print(response)
        data_list = json.loads(response.text).get("data")
        for data in data_list:
            if data.get("tokenId") == contract_address:
                amount = int(int(data.get("balance"))*TronWallet.ratio)
                # break
        # print(TronWallet.contract_address.get(contract_address)+" "+str(amount))
        total_balance += amount

# print(total_balance)

# Write to database
db = next(get_db())
# Get the current time in UTC
utc_time = datetime.now(timezone.utc)
# Define the UTC+8 timezone
utc_plus_8 = timezone(timedelta(hours=8))
# Convert the UTC time to UTC+8
time_in_utc_plus_8 = utc_time.astimezone(utc_plus_8)
db.execute(text("INSERT INTO stablecoin (balance, created_time) VALUES (:balance, :created_time)"), {'balance': total_balance, 'created_time': time_in_utc_plus_8})
db.commit()
db.close()
