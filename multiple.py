import concurrent.futures
import requests
from wallet import EthWallet
import json
headers = {
      'Content-Type': 'application/json'
    }

def fetch_url_with_payload(url, payload):
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

url = "https://withered-clean-smoke.quiknode.pro/d70ae819a02371788cd569d60564a514157508b2/"
payloads = []
for address in list(EthWallet.wallet.keys()):
  payloads.append(json.dumps({
    "id": 67,
    "jsonrpc": "2.0",
    "method": "qn_getWalletTokenBalance",
    "params": [{
      "wallet": address,
      "contracts": list(EthWallet.contract_address.keys())
    }]
  }))

max_threads = 2
total_balances = []
with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    # Schedule the API calls with different payloads
    future_to_payload = {executor.submit(fetch_url_with_payload, url, payload): payload for payload in payloads}
    for future in concurrent.futures.as_completed(future_to_payload):
        payload = future_to_payload[future]
        try:
            response_data = future.result()
        except Exception as exc:
            print(f"Payload {payload} generated an exception: {exc}")
        else:
            # print(f"Payload {payload} returned response data: {response_data}")
            print(json.loads(response_data.text))
            while json.loads(response_data.text).get("error"):
                print("Error............")
                response_data = requests.request("POST", url, headers=headers, data=payload)
            data_list = json.loads(response_data.text).get("result").get("result")
            # print(data_list)
            if len(data_list) > 0:
              for data in data_list:
                balance = int(int(data.get("totalBalance"))*EthWallet.ratio)
                print(data.get("symbol")+" "+str(balance))
                total_balances.append(balance)

print(sum(total_balances))
