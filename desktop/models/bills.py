import requests

class Bill:
    def __init__(self, api_base_url):
        self.url = f"{api_base_url}/bills"

    def create(self, title, amount, regular):
    
        payload = {
            "title": title,
            "amount": amount,
            "regular": regular,
        }

        resp = requests.post(self.url, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data

    def read_all(self):
        resp = requests.get(self.url)
        data = resp.json()
        return data

    def read(self):
        pass

    def update(self):
        pass

    def delete(self, id):
        resp = requests.delete(f"{self.url}/{id}")
        data = resp.json()
        return data

