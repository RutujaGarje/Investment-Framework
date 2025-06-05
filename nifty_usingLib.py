from nsepython import nse_optionchain_scrapper
import pandas as pd

try:
    # Fetch NIFTY option chain from NSE
    option_data = nse_optionchain_scrapper("NIFTY")

    # Extract list of expiry dates
    expiries = option_data['records']['expiryDates']
    print("Available expiries:", expiries)

    # Pick the first expiry
    expiry = expiries[0]

    # Extract full option chain data
    all_data = option_data['records']['data']

    # Prepare lists to store call/put data for selected expiry
    call_list = []
    put_list = []

    for entry in all_data:
        if entry['expiryDate'] == expiry:
            if 'CE' in entry:
                ce = entry['CE']
                call_list.append({
                    'strikePrice': ce.get('strikePrice'),
                    'lastPrice': ce.get('lastPrice'),
                    'bid': ce.get('bidprice'),
                    'ask': ce.get('askPrice'),
                    'volume': ce.get('totalTradedVolume'),
                    'openInterest': ce.get('openInterest'),
                    'impliedVolatility': ce.get('impliedVolatility'),
                    'inTheMoney': ce.get('inTheMoney'),
                    'expiryDate': ce.get('expiryDate')
                })
            if 'PE' in entry:
                pe = entry['PE']
                put_list.append({
                    'strikePrice': pe.get('strikePrice'),
                    'lastPrice': pe.get('lastPrice'),
                    'bid': pe.get('bidprice'),
                    'ask': pe.get('askPrice'),
                    'volume': pe.get('totalTradedVolume'),
                    'openInterest': pe.get('openInterest'),
                    'impliedVolatility': pe.get('impliedVolatility'),
                    'inTheMoney': pe.get('inTheMoney'),
                    'expiryDate': pe.get('expiryDate')
                })

    # Convert to DataFrames
    calls_df = pd.DataFrame(call_list)
    puts_df = pd.DataFrame(put_list)

    print("\nCalls:\n", calls_df.head())
    print("\nPuts:\n", puts_df.head())

except Exception as e:
    print(f"Error fetching NIFTY options data: {e}")
