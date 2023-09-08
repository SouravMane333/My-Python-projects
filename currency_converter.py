import tkinter as tk

# Exchange rates as of July 2023)
exchange_rates = {
    # Currencies and their exchange rates
    "Indian Rupee (INR)": 82.26,
    "US Dollar (USD)": 1.0,
    "Euro (EUR)": 0.91,
    "British Pound (GBP)": 0.78,
    "Japanese Yen (JPY)": 141.4,
    "Canadian Dollar (CAD)": 1.33,
    "Australian Dollar (AUD)": 1.50,
    "Russian Ruble (RUB)": 92.06,
    "Chinese Yuan (CNY)": 7.15,
    "Singapore Dollar (SGD)": 1.33,
}


def convert_currency():   # Function to convert the currency
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            result_label.config(
                text="Error: Cannot convert to the same currency.", fg="red")
        else:
            converted_amount = amount / \
                exchange_rates[from_currency] * exchange_rates[to_currency]
            result_label.config(
                text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}", fg="black")

    except ValueError:
        result_label.config(
            text="Error: Invalid input. Please enter a valid number.", fg="red")


def show_exchange_rate():   # Function to show the exchange rates
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    if from_currency == to_currency:
        exchange_rate_label.config(
            text="Error: Cannot get exchange rate for the same currency.", fg="red")
    else:
        exchange_rate = exchange_rates[to_currency] / \
            exchange_rates[from_currency]
        exchange_rate_label.config(
            text=f"1 {from_currency} = {exchange_rate:.4f} {to_currency}", fg="black")


# Main application window
app = tk.Tk()
app.title("Currency Converter")
app.geometry("400x400")
app.configure(bg="cadet blue")

currencies = list(exchange_rates.keys())
from_currency_var = tk.StringVar(app)
from_currency_var.set(currencies[0])
to_currency_var = tk.StringVar(app)
to_currency_var.set(currencies[1])

title_label = tk.Label(app, text="Currency Converter", font=(
    "Arial", 18, "bold"), bg="black", fg="white")
title_label.pack(pady=15)

amount_label = tk.Label(app, text="Enter amount:",
                        font=("Arial", 14), bg="black")
amount_label.pack(pady=10)
amount_entry = tk.Entry(app, width=15, font=(
    "Arial", 16), borderwidth=5, relief="ridge")
amount_entry.pack()

from_currency_menu = tk.OptionMenu(app, from_currency_var, *currencies)
from_currency_menu.config(font=("Arial", 12), width=40, bg="black")
from_currency_menu.pack(pady=5)

to_currency_menu = tk.OptionMenu(app, to_currency_var, *currencies)
to_currency_menu.config(font=("Arial", 12), width=40, bg="black")
to_currency_menu.pack(pady=5)

convert_button = tk.Button(app, text="Convert", command=convert_currency, bg="black", fg="black",
                           font=("Arial", 14, "bold"), padx=10, pady=5)
convert_button.pack(pady=10)

result_label = tk.Label(app, text="", font=(
    "Arial", 14, "bold"), bg="white", fg="white")
result_label.pack(pady=10)

get_exchange_rate_button = tk.Button(app, text="Get Exchange Rate", command=show_exchange_rate, bg="black", fg="black",
                                     font=("Arial", 12), padx=10, pady=5)
get_exchange_rate_button.pack(pady=5)

exchange_rate_label = tk.Label(app, text="", font=(
    "Arial", 14, "bold"), bg="white", fg="white")
exchange_rate_label.pack(pady=20)

app.mainloop()