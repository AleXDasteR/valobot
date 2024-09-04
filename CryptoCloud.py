import requests

class CryptoCloudAPI:
    def __init__(self, api_key, shop_id):
        self.api_key = api_key
        self.shop_id = shop_id
        self.base_url = "https://api.cryptocloud.plus/v1"
        self.headers = {"Authorization": f"Token {self.api_key}", 'Content-Type': 'application/json'}
    
    def create_invoice(self, shop_id, amount, order_id=None, currency="USD", email=None):
        url = f"{self.base_url}/invoice/create"
        data = {"shop_id": shop_id, "amount": amount, "order_id": order_id, "currency": currency, "email": email}
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()
    
    def get_invoice(self, uuid):
        url = f"{self.base_url}/invoice/info"
        data = {"uuid": uuid}
        response = requests.get(url, headers=self.headers, params=data)
        return response.json()  

if __name__ == "__main__":
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Njk4NCwiZXhwIjo4ODA4MTIwNTI5NX0.QUjEqLlHz-lySIJyvweRRQCfSnd0ehwEOqffPLF98-c"
    shop_id = "QDRMO36eNFwdTl9O"

    api = CryptoCloudAPI(api_key, shop_id)

    # invoice = api.create_invoice(shop_id, amount=200) #amount - сумма чека
    # print(invoice)

    invoice_id = "D6MG8GBD"
    # invoice_id = invoice["invoice_id"]
    invoice_info = api.get_invoice(invoice_id)
    print(invoice_info)
