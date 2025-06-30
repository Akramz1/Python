rates_to_usd = {
    "USD": 1.0,
    "EUR": 0.85,
    "CAD": 1.37,
    "EGP": 49.60,
    "GBP": 0.75,
    "JPY": 143.50,
    "AUD": 1.51
}

History = []


def get_number():
    while True:
        user_input = input("Enter amount (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            return None
        try:
            TheAmount = float(user_input)
            return TheAmount
        except ValueError:
            print("Enter a valid number.")


def get_source_currency():
    while True:
        Source_Currency = input(
            "Source Currency (USD/EGP/EUR/CAD/GBP/JPY/AUD): ").upper()
        if Source_Currency in rates_to_usd:
            return Source_Currency
        else:
            print("Unsupported currency code. Try again.")


def convert_results(amount, source_currency, rates):
    if History:
        History.append('\nNext Operation:\n')  # separator between sessions

    for target_currency in rates:
        if target_currency == source_currency:
            continue
        To_USD = amount / rates[source_currency]
        Converted_Money = To_USD * rates[target_currency]
        record = f"{amount:.2f} {source_currency} = {Converted_Money:.2f} {target_currency}"
        History.append(record)
        print(
            f'{amount:.2f} {source_currency} is equal to {Converted_Money:.2f} {target_currency}')


def main():
    while True:
        amount = get_number()
        if amount is None:
            break
        source_currency = get_source_currency()
        convert_results(amount, source_currency, rates_to_usd)

    print("\nYour History since you ran the program:")
    for record in History:
        print(record)


main()
