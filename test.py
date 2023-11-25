import requests
import json
from wallet import EthWallet
url = "https://withered-clean-smoke.quiknode.pro/d70ae819a02371788cd569d60564a514157508b2/"
headers = {
  'Content-Type': 'application/json'
}

total_balance = 0
for address in list(EthWallet.wallet.keys()):
    payload = json.dumps({
        "id": 67,
        "jsonrpc": "2.0",
        "method": "qn_getWalletTokenBalance",
        "params": [{
          "wallet": address,
          "contracts": list(EthWallet.contract_address.keys())
        }]
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print("It is: "+EthWallet.wallet.get(address))
    print(response.text)
    # json.loads(response.text).get("error")
    while type(json.loads(response.text)) == list:
        print("GOT STUCK")
        print(json.loads(response.text))
        response = requests.request("POST", url, headers=headers, data=payload)
    # print(type(json.loads(response.text)))
    data_list = json.loads(response.text).get("result").get("result")
    if len(data_list) > 0:
        for data in data_list:
            balance = int(int(data.get("totalBalance"))*EthWallet.ratio)
            print(data.get("symbol")+" "+str(balance))
            total_balance += balance
print(total_balance)
