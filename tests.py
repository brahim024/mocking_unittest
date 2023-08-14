import unittest
from unittest.mock import MagicMock,patch
from main import get_user,len_user
from revise import AuthorizationAPI,get_info
from requests.exceptions import Timeout,ConnectionError,HTTPError
import requests.exceptions

class TestResponse(unittest.TestCase):
    @patch('main.get_user')
    def test_len_user(self,mocker):
        mocker.return_value = 'one'
        mocker.status_code.return_value== 200
        self.assertEqual(len_user(),3)

    @patch('main.requests')
    def test_get_user(self,mocker):
        mock_response = MagicMock()
        mock_response.status_code = 203
        mock_response.json.return_value = {'key':"value"}

        mocker.get.return_value = mock_response 
        
        self.assertEqual(get_user(),"No Response")
    
    @patch('main.requests')
    def test_get_user_raise_timeout(self,mocker):
        mocker.get.side_effect = Timeout("Timed Out")
        mocker.exceptions = requests.exceptions
        self.assertEqual(get_user(),'Timed Out')
    
    @patch('main.requests')
    def test_get_user_raise_connection_error(self,mocker):
        mocker.get.side_effect = ConnectionError("Connection Error")
        mocker.exceptions = requests.exceptions
        self.assertEqual(get_user(),'Connection Error')

    @patch('main.requests')
    def test_get_user_raise_status_error(self,mocker):
        mocker.exceptions = requests.exceptions
        mock_response = MagicMock(status_code=403)
        
        mock_response.raise_for_status.side_effect = HTTPError("Something went wrong")
        mocker.get.return_value = mock_response
        self.assertEqual(get_user(),'HttpError was raise')

class TestAuthorizatoin(unittest.TestCase):

    @patch("revise.AuthorizationAPI.post")
    def test_get_info(self,mocker):
        
        mocker_response = MagicMock()
        mocker_response.status_code.return_value = 200
        mocker_response.json.return_value = {'key':'value'}
        
        mocker.return_value = mocker_response
        
        result = get_info()
        
        mocker.assert_called_once() 
        self.assertEqual(result.status_code,mocker_response.status_code)
        # self.assertEqual(result.json,)

    @patch('revise.requests.post')
    def test_authorization_post_raise_timeout(self,mocker):
        mocker.side_effect = Timeout('Timed Out')
        mocker.exceptions = requests.exceptions
        auth = AuthorizationAPI('api','api')
        result = auth.post({'key':'value'},'mock_url')
        self.assertEqual(result,'Timed Out')


        


if __name__ == "__main__":
    unittest.main()