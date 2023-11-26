import requests

# Send a Telegram notification
def send_telegram_notification(message, chat_id, api_key):
    base_url = f"https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown"
    response = requests.get(base_url)
    if response.status_code == 200:
        print("Sent successfully!")
    else:
        print(f"Failed to send notification. Error: {response.content}")

def format_number_with_commas(number):
    return f"{number:,}"