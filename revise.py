import requests
from dataclasses import dataclass

def get_info():
    info = 'https://paypal.sanbox.api'
    grant_type = "client_credentials"
    url = info + "/v1/oauth2/token"
    body_params = {"grant_type": grant_type}

    client = AuthorizationAPI(
        api_client="token_id", api_secret="token_secret"
    )
    res_data = client.post(body_params, url, timeout=20)
    return res_data


@dataclass
class AuthorizationAPI:
    api_client: str
    api_secret: str

    def post(self, data, base_url=None, timeout=10):
        try:
            response = requests.post(
                base_url, data, auth=(self.api_client, self.api_secret), timeout=timeout
            )
        
        except requests.exceptions.Timeout:
            return "Timed Out"
        except requests.exceptions.ConnectionError:
            return "Connection Error"
        else:
            return response