from main import app
from fastapi.testclient import TestClient

client = TestClient(app)
response = client.get('/')

if response.status_code == 200:
    print('[OK] GET / returns 200')
    if '&#x1f4ca; Calorie Tracker' in response.text or 'Calorie Tracker' in response.text:
        print('[OK] Template rendered correctly')
        if 'nickname' in response.text and 'food_name' in response.text:
            print('[OK] All form elements present')
            print('SUCCESS: Fix worked!')
else:
    print('Status:', response.status_code)
    print('Error:', response.text[:300])
