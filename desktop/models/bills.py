import requests

class Bill:
    def __init__(self, api_base_url):
        self.url = api_base_url

    def create(self, title, amount, regular):
    
        payload = {
            "title": title,
            "amount": amount,
            "regular": regular,
        }

        resp = requests.post(f"{self.url}/bills", json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data



    def list(self, id):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
