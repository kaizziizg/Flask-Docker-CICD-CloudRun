import unittest
from flask_testing import TestCase
from app import app

class SettingBase(TestCase):
    def create_app(self):
		# 建立flask實體
        app.config['TESTING'] = True
        return app

class TestWelcomePage(SettingBase):
    def testMainPage(self):
        response = self.client.get('/')
        print(response.data)
        self.assertEqual(response.data,b"Hello, Cloud Run!")


if __name__ == '__main__':
    unittest.main()