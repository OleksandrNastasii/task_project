response = client.delete(f'/users/{user_id}')
            self.assertEqual(response.status_code, 200)  