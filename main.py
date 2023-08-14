import requests

def len_user():
    joke = get_user()
    return len(joke)

def get_user():
    url = 'https://randomuser.me/api/'
    try:
        response = requests.get(url,timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return "Timed Out"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.HTTPError:
        return "HttpError was raise"
    
    
    else:
        if response.status_code == 200:
            
            return response.json().get('results')
        else:
            return 'No Response'
    
print(len_user())