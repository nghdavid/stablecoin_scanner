import requests
import json
import os
import time
from wallet import EthWallet, TronWallet
from dotenv import load_dotenv
from app.db.session import get_db
from sqlalchemy import text
from datetime import datetime, timedelta, timezone
load_dotenv()
import random

# total_balance = 2772056745600
# Generate a random number between -100000000 and 100000000
db = next(get_db())

# for i in range(100000):
#     random_number = random.randint(-100000000, 100000000)
#     total_balance += random_number
#     # Write to database
#     # Get the current time in UTC
#     utc_time = datetime.now(timezone.utc)
#     # Define the UTC+8 timezone
#     utc_plus_8 = timezone(timedelta(hours=8))
#     # Convert the UTC time to UTC+8
#     time_in_utc_plus_8 = utc_time.astimezone(utc_plus_8)
#     db.execute(text("INSERT INTO stablecoin (balance, created_time) VALUES (:balance, :created_time)"), {'balance': total_balance, 'created_time': time_in_utc_plus_8})
#     db.commit()
#     db.close()


total_balance = 2757557745108+80000000
utc_time = datetime.now(timezone.utc)
utc_plus_8 = timezone(timedelta(hours=8))
time_in_utc_plus_8 = utc_time.astimezone(utc_plus_8)
db.execute(text("INSERT INTO stablecoin (balance, created_time) VALUES (:balance, :created_time)"), {'balance': total_balance, 'created_time': time_in_utc_plus_8})
db.commit()
db.close()