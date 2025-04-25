import openbb as obb

# Authenticate with your OpenBB Hub account
obb.account.login(pat="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoX3Rva2VuIjoiclpLZEZYMGZNRzJXWlNQc1dxb3l3RmQzdXBYYVNkdDdWNWxGalFaQyIsImV4cCI6MTc3NzEyMzUyNH0.aHUUD8rhZNDtj_klA1AmKfpfuHFK97T4DAjuE6Ikfc4")

# Get historical stock prices for AAPL
data = obb.equity.price.history(symbol="AAPL", timeframe="1d")

# Print the data
print(data)