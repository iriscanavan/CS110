# Iris Canavan, Section 3
from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route("/")

def get_stock():
	html = """
	<html>
		<head>
			<meta charset = "UTF-8">
			<title>Stock Lookup</title>
			<meta name = "description" content = "display stock information">
			<meta name = "keywords" content = "html page">
		</head>
		<body>
			<h1>Stock Web Application</h1>
				<form action = "/stock_result" method = "post">
					<label>
						Stock Symbol:
						<input type = "text" id = "stock_symbol" name = "stock_symbol" required/><br><br>
					</label
					<br />
					<label>
						<input type = "checkbox" id = "opening_value" name = "1check" value = "Opening Value">
						<label for "opening_value">Opening Value</label><br>
						<input type = "checkbox" id = "high" name = "2check" value = "High">
						<label for "high">High</label><br>
						<input type = "checkbox" id = "low" name = "3check" value = "Low"
						<label for "low">Low</label><br>
						<input type = "checkbox" id = "current_price" name = "4check" value = "Current Price">
						<label for "current_price">Current Price</label><br>
						<hr />
						<input type = "submit" value = "Get Stock Info">
					</label>
				</form>
		</body>
	</html>"""
	return html

@app.route("/stock_result", methods = ["POST"])
def stock_result():
	result = ""
	symbol = request.form.get("stock_symbol")
	opening = request.form.get("1check")
	high = request.form.get("2check")
	low = request.form.get("3check")
	current = request.form.get("4check")

	if symbol == "AAPL":
		data = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=json&apikey=VPVN3LZF0ZVPNXB2&symbol=" + symbol)
		stock_response = json.loads(data.text)
		result += "The values for " + symbol + " are:<br>"
		values = stock_response["Global Quote"]
		if opening:
			result += "Opening value: " + values["02. open"] + "<br>"
		if high:
			result += "High: " + values["03. high"] + "<br>"
		if low:
			result += "Low: " + values["04. low"] + "<br>"
		if current:
			result += "Current price: " + values["05. price"] + "<br>"
	else:
		return (symbol + " is an invalid stock symbol")
	return result
	
if __name__ == "__main__":
	app.run(host = "127.0.0.1", port = 4000, debug = True)
