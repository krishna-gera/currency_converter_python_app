import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.api_key = '5cfe68986bc7ee09ecf76098'
        self.api_url = f'https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD'
        
        self.create_widgets()
        self.get_currencies()

    def create_widgets(self):
        font_large = ("Helvetica", 16)
        font_heading = ("Helvetica", 20, "bold")
        
        self.heading_label = tk.Label(self.root, text="Live Currency Rate Checker", font=font_heading)
        self.heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.amount_label = tk.Label(self.root, text="Enter amount:", font=font_large)
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.amount_entry = tk.Entry(self.root, font=font_large)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.from_currency_label = tk.Label(self.root, text="From currency:", font=font_large)
        self.from_currency_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.from_currency_combobox = ttk.Combobox(self.root, font=font_large)
        self.from_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.from_currency_combobox['state'] = 'normal'  
        
        self.to_currency_label = tk.Label(self.root, text="To currency:", font=font_large)
        self.to_currency_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.to_currency_combobox = ttk.Combobox(self.root, font=font_large)
        self.to_currency_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.to_currency_combobox['state'] = 'normal'  
        
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency, font=font_large)
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def get_currencies(self):
        response = requests.get(self.api_url)
        data = response.json()
        currencies = list(data['conversion_rates'].keys())
        
        self.from_currency_combobox['values'] = currencies
        self.to_currency_combobox['values'] = currencies

    def convert_currency(self):
        amount = self.amount_entry.get()
        from_currency = self.from_currency_combobox.get()
        to_currency = self.to_currency_combobox.get()
        
        if not amount or not amount.isdigit():
            messagebox.showerror("Error", "Please enter a valid amount")
            return
        
        response = requests.get(f'https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_currency}/{to_currency}')
        data = response.json()
        rate = data['conversion_rate']
        result = float(amount) * rate
        
        self.result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
