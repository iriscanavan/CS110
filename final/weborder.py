# Iris Canavan, Section 3

from flask import Flask, request

app = Flask(__name__)

strHTML_top = "<!DOCTYPE HTML><html><head><body>"
strHTML_bottom = "</body></html>"

@app.route("/")
@app.route("/home")
def home():
	strHTML = strHTML_top + "<h1>This is the Order home page</h1>" + strHTML_bottom
	return strHTML

@app.route("/order")
def order():
	form = """
	<form action = "/review" method = "get">
		<body>
			<p>
				Enter Order Data: <br> Coffee, $21.55<br> Tea,
				$8.56<br> Eggs, $3.99<br>
			</p>
		</body>
		<label for = "product">Product:</label>
		<input type = "text" id = "product" name = "product" required><br><br>
		<label for = "quantity">Quantity:</label>
		<input type = "text" id = "quantity" name = "quantity" required><br><hr>
		<input type = "submit" value = "Order">
	</form>
	"""
	return strHTML_top + "<h2>Order</h2><hr>" + form + strHTML_bottom

@app.route("/review", methods = ["GET"])
def review():
	product = request.args.get("product")
	quantity = request.args.get("quantity")
	dict_products = {"Coffee": 21.55, "Tea": 8.56, "Eggs": 3.99}
	if product in dict_products:
		price = dict_products[product]
		total = price * float(quantity)
		review_html = f"<h2>Total Order</h2><p>Product: {product}</p><p>Quantity ordered: {quantity}</p><p>Total: {total}</p>"
	else:
		review_html = "<h2>Review Order</h2><p>Product not found.</p>"
	review_html += """<a href = "/order">Go Back to Order Page</a>"""
	return strHTML_top + review_html + strHTML_bottom

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
