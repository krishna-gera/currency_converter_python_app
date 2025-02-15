## Currency Converter Application

### Overview
This application is a desktop-based currency converter built using the Tkinter library in Python. It provides live currency conversion rates and allows users to convert an amount from one currency to another.

### Features
- **Live Currency Rates**: The application fetches live exchange rates using an API.
- **User-friendly Interface**: A simple and intuitive graphical user interface (GUI) built with Tkinter.
- **Customizable API Key**: Users can replace the provided API key with their own for personalized use.
- **Dropdown Menus for Currency Selection**: Easy selection of currencies using dropdown menus.

### Installation
1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Install Dependencies**: Ensure you have Python installed on your system. You will also need the `requests` library, which can be installed using:
   ```bash
   pip install requests
   ```
3. **API Key Setup**: Obtain an API key from [ExchangeRate-API](https://www.exchangerate-api.com/) and replace the placeholder API key in the code with your own.

### Usage
1. **Run the Application**: Execute the script to launch the currency converter application.
   ```bash
   python currency_converter.py
   ```
2. **Enter Amount**: Input the amount you want to convert in the designated entry field.
3. **Select Currencies**: Choose the source and target currencies from the dropdown menus.
4. **Convert**: Click the "Convert" button to perform the conversion and display the result.

### Dependencies
- **Python**: Ensure that Python is installed on your system.
- **Tkinter**: Tkinter is included with Python, so no additional installation is required.
- **Requests**: Used to make HTTP requests to the exchange rate API.

### Screenshots
You can include screenshots of the application to give users a visual idea of its appearance and functionality.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgments
- [ExchangeRate-API](https://www.exchangerate-api.com/) for providing the exchange rate data.
