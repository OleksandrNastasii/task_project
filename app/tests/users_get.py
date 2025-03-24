import unittest
import subprocess
import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from main import app


class TestGetAllUsers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(["python", "main.py"])
        time.sleep(2)

    def test_get_all_users(self):
        with app.test_client() as client:

            response = client.get('/users')
            self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

if __name__ == '__main__':
    unittest.main()