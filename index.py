from bs4 import BeautifulSoup

html= """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>VIN Decoder</title>
</head>
<body>
	<h1>VIN Decoder</h1>
	<em>Jackie Choi</em>
	<h2 data-example="vin_input">VIN: </h2>
	<h3 class="special">Error Message: </h3>
	<div>
		<ul>
			<li class="special super-spcial">Country: </li>
			<li class="special">Year: </li>
			<li>Make/Model: </li>		
		</ul>
	</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
data = soup.body.contents


for el in soup.select(".special"):
	print(el.name)

user_attr_value = soup.find("h2")["data-example"]
print(user_attr_value)
