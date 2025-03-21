from app.db.session import get_db
from app.models.stablecoin import Stablecoin
from sqlalchemy import text
from utils import send_telegram_notification, format_number_with_commas
from wallet import EthWallet
from app.db.redis import cache
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '.env')
# load_dotenv()
load_dotenv(dotenv_path=env_path)

telegram_api_key = os.environ.get('TELEGRAM_KEY')
chat_id = EthWallet.chat_id
interval = 10
threshold = 50000000

db = next(get_db())
balances = db.query(Stablecoin).order_by(Stablecoin.created_time.desc()).limit(int(25*60/10)).all()

latest_balance = balances[0].balance
balance_6h_ago = balances[int(6*60/10)].balance
balance_12h_ago = balances[int(12*60/10)].balance
balance_24h_ago = balances[int(24*60/10)].balance
cache.setex('is_executed', 590, '1')
if latest_balance > balance_12h_ago + threshold or latest_balance > balance_24h_ago + threshold or latest_balance > balance_6h_ago + threshold:
    is_expire = cache.get('is_expire')
    if is_expire is None or int(is_expire) == -2:
        message = f"Balance of stablecoin has increased {format_number_with_commas(latest_balance-balance_24h_ago)} in the last 24 hours. \nBalance of stablecoin has increased {format_number_with_commas(latest_balance-balance_12h_ago)} in the last 12 hours. \nBalance of stablecoin has increased {format_number_with_commas(latest_balance-balance_6h_ago)} in the last 6 hours."
        send_telegram_notification(message, chat_id, telegram_api_key)
        message = f"The current balance of stablecoin is {format_number_with_commas(latest_balance)}."
        send_telegram_notification(message, chat_id, telegram_api_key)
    cache.setex('is_expire', 3600, '1')
