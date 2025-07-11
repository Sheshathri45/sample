import requests

def convert_currency(amount: float, from_cur: str, to_cur: str) -> float:
    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    rates = data.get("rates", {})
    if to_cur not in rates:
        raise ValueError(f"Unsupported currency: {to_cur}")
    return amount * rates[to_cur]

def main():
    print("==== Real-Time Currency Converter ====")
    try:
        amount = float(input("1) Enter amount: "))
        from_currency = input("2) Convert from (e.g., USD): ").strip().upper()
        to_currency = input("3) Convert to (e.g., INR): ").strip().upper()
        converted = convert_currency(amount, from_currency, to_currency)
        print(f"4) Converted amount: {converted:.2f} {to_currency}")
    except ValueError as e:
        print("Error:", e)
    except requests.RequestException as e:
        print("Network/API error:", e)
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()
