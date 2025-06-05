import requests

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.nseindia.com/option-chain"
}

session = requests.Session()
session.get("https://www.nseindia.com", headers=headers)
response = session.get(
    # "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY",
    "https://www.nseindia.com/api/option-chain-v3?type=Indices&symbol=NIFTY&expiry=29-May-2025",
    headers=headers
)

data = response.json()

for item in data["records"]["data"]:
    strike = item["strikePrice"]
    ce = item.get("CE", {})
    pe = item.get("PE", {})

    print(f"Strike: {strike}")
    print(f"  CE: LTP: {ce.get('lastPrice')}, OI: {ce.get('openInterest')}, IV: {ce.get('impliedVolatility')}")
    print(f"  PE: LTP: {pe.get('lastPrice')}, OI: {pe.get('openInterest')}, IV: {pe.get('impliedVolatility')}")
    print("-" * 50)
