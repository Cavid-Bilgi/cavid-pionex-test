import hmac
import hashlib
import time
import requests

API_KEY = "BURAYA_YAZ"
API_SECRET = "BURAYA_YAZ"

base_url = "https://api.pionex.com"

def generate_signature(query_string: str, secret: str):
    return hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

def get_account_info():
    timestamp = str(int(time.time() * 1000))
    query_string = f"timestamp={timestamp}"
    signature = generate_signature(query_string, API_SECRET)
    headers = {
        "X-PIONEX-KEY": API_KEY
    }
    url = f"{base_url}/api/v1/account?{query_string}&signature={signature}"
    response = requests.get(url, headers=headers)
    return response.json()
