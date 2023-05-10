import requests

def main():
	stock_symbol = input("Enter stock symbol: ")
	response = get_stock(stock_symbol)
	print(response)
	print("Length of response: ", len(response))


def get_stock(symbol):
	stock = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=json&apikey=VPVN3LZF0ZVPNXB2&symbol=" + symbol)
	print(stock_response)
	return stock.text

main()


