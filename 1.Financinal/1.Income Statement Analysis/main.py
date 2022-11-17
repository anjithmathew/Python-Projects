""" import requests and matlabplot"""

import requests
import matplotlib.pyplot as plt

""" importing api key & company specifications"""

api_key = open("api_key", "r").read() 
company = "AAPL"
years = 10

""" Income statement analysis for 10 years in plot & csv code"""

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?datatype=csv&limit={years}&apikey={api_key}")
# income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
# income_statement = income_statement.json()
# revenue  = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
# grossProfit = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

# plt.plot(revenue , label ="revenue")

# plt.plot(grossProfit , label ="grossprofit")
# plt.legend(loc = "upper left")
# plt.show()

with open("aapl.csv", "wb") as f:
    f.write(income_statement.content)
