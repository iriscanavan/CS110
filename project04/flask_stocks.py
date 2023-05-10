from flask import Flask, request

app = Flask(__name__)

@app.route("/")

def get_stock():
	html = """
	<!DOCTYPE HTML>
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
	opening = request.form["1check"]
	if opening:
		return "The values for AAPL are: /n Opening value: "
		
#high = request.form["2check"]
#low = request.form["3check"]
#current = request.form["4check"]


if __name__ == "__main__":
	app.run(host = "127.0.0.1", port = 4000, debug = True)
