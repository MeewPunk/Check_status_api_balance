# Check_status_api_balance

# นำเข้า from binance.client import Client
# ติดตั้งผ่าน pip pip install python-binance
# https://python-binance.readthedocs.io/en/latest/
from binance.client import Client

#ใส่ api_key balance
api_key = "0IR7dA7CJk5LE0TPj9t032NOGCOZZjh0KY0BVnPQFrCFqkjKbaCJz2dwHU9MQPiX" 
#ใส่ api_secret balance
api_secret = "rHryuBUi2go7wzmhl2QTKEaCaFdMGVjZB5jPDt21yoOJfeNw2KePhgZqsnq3g73a"
client = Client(api_key, api_secret)



# ใช้ try: และ except: เพื่อรับข้อผิดพลาด
# ถ้าไม่มีอะไรผิดพลาดจบการทำงานที่ try: 
# ถ้ามีอะไรผิดพลาดจบการทำงานที่ except: 

# ใช้ client.futures_account_balance() เพื่อรับรับมูลในบัญชี

# ตัวอย่างข้อมูลได้กลับมาเป็น json
# [{'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'DOT', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'BTC', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'SOL', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'BNB', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'ETH', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'ADA', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'USDT', 'balance': '27.60439188', 'withdrawAvailable': '27.59506997', 'updateTime': 1657202964475}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'XRP', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'USDC', 'balance': '0.00000000', 'withdrawAvailable': '0.00000000', 'updateTime': 0}, 
# {'accountAlias': 'FzFzSgSguXuXsRTi', 'asset': 'BUSD', 'balance': '-0.00379876', 'withdrawAvailable': '0.00000000', 'updateTime': 1651452336506}]

# เข้าถึง USDT balance [6]['balance'] ใช้ float แปลงข้อมูล ใช้ round ปัดเศษ 
print(client.futures_account_balance())
try:
    balance_USDT = round(float(client.futures_account_balance()[6]['balance']),2)
    print('balance_USDT ',balance_USDT)
except:
    print('Binance Invalid API Key ....')