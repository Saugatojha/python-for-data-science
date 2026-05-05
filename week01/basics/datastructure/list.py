# 🏦  Portfolio Tracker
# You started with 3 stocks in your portfolio. During the year you made some changes:

# Create a list of your 3 stocks ["DORDI", "HLI", "NABIL"]
# Print how many stocks you currently hold
# You bought a new stock "RHPL" — add it to portfolio
# Print your newest addition (last item using negative index) "RHPL"
# Print your oldest/first holding (first item)
# RLFL did badly — you sold it, remove it from portfolio
# Print your final portfolio with f-string like:

# My final portfolio has 3 stocks: ['DORDI', 'HLI', 'NABIL']

my_portfolio=["DORDI","HLI","NABIL"]
print(f"Holdings before removing loss {my_portfolio}")
print(len(my_portfolio))

my_portfolio.append("RHPL")
print(my_portfolio[-1])
print(my_portfolio[0])

my_portfolio.remove("DORDI")

print(f"These are my holdings {my_portfolio}")