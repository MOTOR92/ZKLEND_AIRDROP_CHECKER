import requests

def airdrop_status(address):
    url = f"https://app.zklend.com/api/airdrop/{address}"
    try:
        response = requests.get(url)
        data = response.json()

        if isinstance(data, dict):
            amount_hex = data.get("amount", {}).get("value")
            if amount_hex is not None:
                amount_int = int(amount_hex, 16)
                print(f"{address} Eligible {amount_int/1000000000000000000} ZEND")
            else:
                print(f"{address} Not Eligible")
        else:
            print(f"{address} Not Eligible")

    except (ValueError, requests.RequestException) as e:
        print(f"Error processing data for address {address}: {e}")

def main():
    # Load addresses from wallets.txt
    with open('wallets.txt', 'r') as file:
        addresses = file.read().splitlines()

    for address in addresses:
        airdrop_status(address)

if __name__ == "__main__":
    main()
