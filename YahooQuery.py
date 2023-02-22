import pandas as pd
import yahooquery

# Define the ticker symbols and the quarters you want to fetch
tickers = ['AAPL', 'MSFT']
quarters = ['1Q2022', '2Q2019']

# Create an empty list to store the data for each company
data = []

# Loop through the tickers and quarters and fetch the earnings data
for ticker in tickers: 
    for quarter in quarters:
        earnings =  yahooquery.Ticker(ticker, asynchronous=True).earnings
        
        # Filter the earnings data to include only the specified quarter
        quarterly_earnings = [x for x in earnings[ticker]['earningsChart']['quarterly'] if x['date'] == quarter]
        earnings[ticker]['earningsChart']['quarterly'] = quarterly_earnings
        
        # Add a column to the earnings data with the ticker symbol
        earnings['symbol'] = ticker
        
        # Append the earnings data for this company and quarter to the list
        data.append(earnings)

# Convert each dictionary in the list to a pandas DataFrame
dfs = [pd.DataFrame(d) for d in data]

# Concatenate the DataFrames for all companies into a single DataFrame
earnings_data = pd.concat(dfs)

# Export the data to an Excel file
earnings_data.to_excel('earnings_data.xlsx', index=False)
