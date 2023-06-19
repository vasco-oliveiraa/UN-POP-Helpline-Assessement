import requests

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        ip_address = data['ip']
        return ip_address
    except requests.exceptions.RequestException:
        return "Unknown"