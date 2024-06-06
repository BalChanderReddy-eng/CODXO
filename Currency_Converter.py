##IMPORTING REQUESTS FOR URL
import requests

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount

        if from_currency != 'USD':  ##WE HAVE CHOSEN THE BASE AS USD
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'  ##API CONTAINS ALL THE CURRENCY VALUES
    c = CurrencyConverter(url)
    from_currency = input("From currency: ")
    to_currency = input("To currency: ")
    amount = float(input("Enter amount: "))
    result = c.convert(from_currency, to_currency, amount)
    print(f"{amount} {from_currency} is equal to {result} {to_currency}")
