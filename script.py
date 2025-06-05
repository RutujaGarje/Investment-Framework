import yfinance as yf


try:
   symbol = yf.Ticker("^NSEI")
   current_price = symbol.fast_info.last_price
except Exception as e:
   print("Error fetching stock price: {e}")


#if current_price is not None:
#    print(f"The current price of Microsoft stock ({$symbol}) is: ${current_price:.2f}")

# list all available option expiry dates
expiries = symbol.options
print("Available expiries:", expiries)

# pick an expiry (e.g. the first one)
expiry = expiries[0]

# fetch the option chain for that expiry
opt_chain = symbol.option_chain(expiry)

# opt_chain.calls and opt_chain.puts are both pandas DataFrames
calls = opt_chain.calls
puts  = opt_chain.puts

print("\nCalls:\n", calls.head())
print("\nPuts:\n",  puts.head())
#print("\nPuts:\n",  puts.volume())


