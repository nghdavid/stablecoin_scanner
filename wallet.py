from typing import Dict
import os
from dotenv import load_dotenv
load_dotenv()

class WalletBase:
  wallet: Dict[str, str]
  price: float
  ratio: float
  link: str
  chat_id: str

class Erc20Wallet(WalletBase):
    sqs_url: str
    scan_domain: str
    sqs_delay_time: int

class EthWallet(Erc20Wallet):
    wallet = {
      "0x9696f59e4d72e237be84ffd425dcad154bf96976": "Binance18",
      "0x5a52e96bacdabb82fd05763e25335261b270efcb": "Binance28",
      "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8": "Binance7",
      "0x4976a4a02f38326660d17bf34b431dc6e2eb2327": "Binance20",
      "0x56eddb7aa87536c09ccc2793473599fd21a8b17f": "Binance17",
      "0xf977814e90da44bfa03b6295a0616a897441acec": "Binance8",
      "0x28c6c06298d514db089934071355e5743bf21d60": "Binance14",
      "0xdfd5293d8e347dfe59e90efd55b2956a1343963d": "Binance16",
      "0x21a31ee1afc51d94c2efccaa2092ad1028285549": "Binance15",
      "0x47ac0fb4f2d84898e4d9e7b4dab3c24507a6d503": "BinancePeg",
      "0x3d55ccb2a943d88d39dd2e62daf767c69fd0179f": "Okx23",
      "0x68841a1806ff291314946eebd0cda8b348e73d6d": "Okx26",
      "0x7eb6c83ab7d8d9b8618c0ed973cbef71d1921ef2": "Okx20",
      "0xf59869753f41Db720127Ceb8DbB8afAF89030De4": "Okx15",
      "0x65A0947BA5175359Bb457D3b34491eDf4cBF7997": "Okx16",
      "0xe9172Daf64b05B26eb18f07aC8d6D723aCB48f99": "Okx19",
      "0x4D19C0a5357bC48be0017095d3C871D9aFC3F21d": "Okx17",
      "0x5C52cC7c96bDE8594e5B77D5b76d042CB5FaE5f2": "Okx18",
      "0xc5451b523d5FFfe1351337a221688a62806ad91a": "Okx10",
      "0x6Fb624B48d9299674022a23d92515e76Ba880113": "Okx14",
      "0x461249076B88189f8AC9418De28B365859E46BfD": "Okx9",
      "0xc708A1c712bA26DC618f972ad7A187F76C8596Fd": "Okx13",
      "0x69a722f0B5Da3aF02b4a205D6F0c285F4ed8F396": "Okx12",
      "0x42436286A9c8d63AAfC2eEbBCA193064d68068f2": "Okx11",
      "0xCbA38020cd7B6F51Df6AFaf507685aDd148F6ab6": "Okx8",
      "0x2c8FBB630289363Ac80705A1a61273f76fD5a161": "Okx4",
      "0x42436286A9c8d63AAfC2eEbBCA193064d68068f2": "Okx11",
      "0x5041ed759Dd4aFc3a72b8192C143F72f4724081A": "Okx7",
      "0xf89d7b9c864f589bbF53a82105107622B35EaA40": "Bybit1",
      "0xee5B5B923fFcE93A870B3104b7CA09c3db80047A": "Bybit2",
      "0xA7A93fd0a276fc1C0197a5B5623eD117786eeD06": "Bybit3"
    }
    price = {"usdt": 1.0, "usdc": 1.0}
    ratio = 0.000001
    link = ""
    chat_id = "5583052544"
    contract_address = {
        "0xdac17f958d2ee523a2206206994597c13d831ec7": "usdt", 
        "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48": "usdc"
    }
    sqs_url = ""
    sqs_delay_time = 5
    scan_domain = "api.etherscan.io"

class TronWallet(Erc20Wallet):
    wallet = {
      "TMuA6YqfCeX8EhbfYEg5y7S4DqzSJireY9": "BinanceCold1",
      "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb": "BinanceCold2",
      "TJCo98saj6WND61g1uuKwJ9GMWMT9WkJFo": "Binance3",
      "TT1DyeqXaaJkt6UhVYFWUXBXknaXnBudTK": "BinanceCold3",
      "TDqSquXBgUCLYvYC4XZgrprLK589dkhSCf": "BinanceHot7",
      "TYASr5UV6HEcXatwdFQfmLVUqQQQMUxHLS": "BinanceHot3",
      "TAzsQ9Gx8eqFNFSKbeXrbi45CuVPHzA8wr": "BinanceHot5",
      "TNXoiAJ3dct8Fjg4M9fkLFh9S2v9TXc32G": "BinanceHot4",
      "TJDENsfBJs4RFETt1X1W8wMDc8M5XnJhCe": "BinanceHot6",
      "TQrY8tryqsYVCYS3MFbtffiPp2ccyn4STm": "Binance2",
      "TM1zzNDZD2DPASbKcgdVoTYhfmYgtfwx9R": "Okx1",
      "TSaRZDiBPD8Rd5vrvX8a4zgunHczM9mj8S": "Okx7",
      "TWGZbjofbTLY3UCjCV4yiLkRg89zLqwRgi": "Okx5",
      "TJbHp48Shg4tTD5x6fKkU7PodggL5mjcJP": "Okx6",
      "TCz47XgC9TjCeF4UzfB6qZbM9LTF9s1tG7": "Okx4",
      "TB1WQmj63bHV9Qmuhp39WABzutphMAetSc": "Bybit1",
      "TTH75Z9rfRgzCLNDDYBaR2WjUvuSDRtSMg": "Bybit2",
      "TU4vEruvZwLLkSfV9bNw12EJTPvNr7Pvaa": "Bybit3",
      "TXRRpT4BZ3dB5ShUQew2HXv1iK3Gg4MM9j": "Bybit4"
    }
    price = {"usdt": 1.0, "usdc": 1.0}
    ratio = 0.000001
    link = ""
    chat_id = "5583052544"
    contract_address = {
        "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t": "usdt"
    }
    sqs_url = ""
    sqs_delay_time = 5
    scan_domain = "apilist.tronscanapi.com"