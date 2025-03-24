import unittest
import subprocess
import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from main import app

class TestCreateUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(["python", "main.py"])
        time.sleep(2)

    def test_create_user(self):
        user_data = {'name': 'John Doe', 'email': 'mksss333@xop.com'}
        with app.test_client() as client:
            response = client.post('/users', json=user_data)
            user_id = response.json['id']
            self.assertEqual(response.status_code, 201)
            
            response = client.delete(f'/users/{user_id}')
            self.assertEqual(response.status_code, 200)  


    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

if __name__ == '__main__':
    unittest.main()