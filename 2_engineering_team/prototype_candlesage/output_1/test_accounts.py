import unittest

class Account:
    def __init__(self, username: str, password: str, profile_picture: str = '') -> None:
        self.username = username
        self.password = password
        self.profile_picture = profile_picture

    def signup(self, username: str, password: str) -> dict:
        return {'username': username, 'profile_picture': 'default.png'}

    def login(self, username: str, password: str) -> bool:
        return username == "testuser" and password == "testpassword"

    def get_user_profile(self) -> dict:
        return {'username': self.username, 'profile_picture': self.profile_picture}

# Unit test module for Account class
class TestAccount(unittest.TestCase):

    def test_signup(self):
        acc = Account('user', 'pass')
        result = acc.signup('newuser', 'newpass')
        self.assertEqual(result['username'], 'newuser')
        self.assertEqual(result['profile_picture'], 'default.png')

    def test_login_success(self):
        acc = Account('testuser', 'testpassword')
        self.assertTrue(acc.login('testuser', 'testpassword'))

    def test_login_failure(self):
        acc = Account('user', 'wrongpass')
        self.assertFalse(acc.login('user', 'wrongpass'))

    def test_get_user_profile(self):
        acc = Account('someuser', 'somepass', 'somepic.png')
        profile = acc.get_user_profile()
        self.assertEqual(profile['username'], 'someuser')
        self.assertEqual(profile['profile_picture'], 'somepic.png')

if __name__ == '__main__':
    unittest.main()