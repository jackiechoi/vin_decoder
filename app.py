from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

year_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y']
country_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nested = [['JAA', 'Japan', 'Isuzu'], ['MPA', 'Japan', 'Isuzu'], ['SAB', 'UK', 'Optare'], ['SAJ', 'UK', 'Jaguar'], ['SAL', 'UK', 'Land Rover'], ['SAR', 'UK', 'Rover '], ['SAT', 'UK', 'Triumph'], ['SB1', 'UK', 'Toyota'], ['SBM', 'UK', 'McLaren Automotive '], ['SCA', 'UK', 'Rolls Royce'], ['SCB', 'EU', 'Bentley'], ['SCC', 'UK', 'Lotus Cars '], ['SCE', 'UK', 'DeLorean'], ['SCF', 'UK', 'Aston Martin Lagonda Limited'], ['SDB', 'UK', 'Peugeot'], ['SFA', 'UK', 'Ford'], ['SFD', 'UK', 'Alexander Dennis'], ['SFE', 'UK', 'Alexander Dennis (North America)'], ['SHH', 'UK', 'Honda '], ['SHS', 'UK', 'Honda'], ['SJN', 'UK', 'Nissan (OBDII-Y5)'], ['SKF', 'EU', 'Vauxhall (OBDII-Y5)'], ['SUD', 'Poland', 'Wielton'], ['TCC', 'Switzerland', 'Micro Compact Car'], ['TEB', 'UK/Switzerland', 'Johnston sweeper (Bucher)'], ['TM9', 'Czech Republic', 'Škoda trolleybus'], ['TMA', 'Czech Republic', 'Hyundai '], ['TMB', 'Czech Republic', 'Škoda (OBDII-Y6)'], ['TMP', 'Czech Republic', 'Škoda trolleybus'], ['TRU', 'Hungary', 'Audi (OBDII-Y6) '], ['TSM', 'Hungary', 'Suzuki '], ['TYA', 'Portugal', 'Mitsubishi Truck'], ['TYB', 'Portugal', 'Mitsubishi Truck'], ['U5Y', 'Slovakia', 'Kia'], ['UU', 'Romania', 'Dacia '], ['UU1', 'Romania', 'Renault Dacia (OBDII-Y5)'], ['VA0', 'Austria', 'ÖAF '], ['VAN', 'Austria', 'MAN'], ['VF1', 'France', 'Renault'], ['VF2', 'France', 'Renault'], ['VF3', 'France', 'Peugeot'], ['VF4', 'France', 'Talbot'], ['VF5', 'France', 'Iveco'], ['VF6', 'France', 'Renault Trucks/Buses'], ['VF7', 'France', 'Citroën (likely OBDII-Y5)'], ['VF8', 'France', 'Matra/Talbot/Simca'], ['VF9', 'France', 'Bugatti'], ['VFE', 'France', 'Iveco Bus'], ['VLU', 'France', 'Scania'], ['VNK', 'France', 'Toyota'], ['VNV', 'UK', 'Renault-Nissan (OBDII-Y5)'], ['VR1', 'France', 'DS Automobiles'], ['VS6', 'Spain', 'Ford'], ['VS7', 'Spain', 'Citroën (likely OBDII-Y5)'], ['VSA', 'Spain', 'Mercedes-Benz'], ['VSE', 'Spain', 'Suzuki'], ['VSK', 'Spain', 'Nissan (OBDII-Y5)'], ['VSS', 'Spain', 'SEAT (OBDII-Y6)'], ['VSX', 'Spain', 'Opel (OBDII-Y5)'], ['VV9', 'Spain', 'Tauro Sport Auto'], ['VWA', 'Spain', 'Nissan (OBDII-Y5)'], ['VWV', 'Spain', 'Volkswagen'], ['W09', 'Germany', 'Ruf Automobile '], ['W0L', 'Germany', 'Opel/Vauxhall (OBDII-Y5)'], ['W0SV', 'Germany', 'Opel Special Vehicles (OBDII-Y5)'], ['W0V', 'Germany', 'Opel (OBDII-Y5)'], ['WA1', 'EU', 'Audi SUV (OBDII-Y6)'], ['WAG', 'Germany', 'Neoplan'], ['WAP', 'Germany', 'Alpina '], ['WAU', 'Germany', 'Audi (OBDII-Y6)'], ['WBA', 'Germany', 'BMW'], ['WBD', 'EU', 'Mercedes-Benz'], ['WBS', 'Germany', 'BMW M '], ['WBW', 'EU', 'BMW'], ['WBX', 'Germany', 'BMW'], ['WBY', 'EU', 'BMW'], ['WDA', 'EU', 'Daimler'], ['WDB', 'Germany', 'Mercedes-Benz (Model Unknown)'], ['WDC', 'Germany', 'DaimlerChrysler'], ['WDD', 'Germany', 'Mercedes-Benz'], ['WDF', 'EU', 'Mercedes V Class (Van)'], ['WEB', 'Germany', 'EvoBus (Mercedes-Bus)'], ['WF0', 'Germany', 'Ford'], ['WJM', 'Germany', 'Iveco Magirus'], ['WJR', 'Germany', 'Irmscher '], ['WKK', 'Germany', 'Karl Kässbohrer Fahrzeugwerke '], ['WMA', 'Germany', 'MAN'], ['WME', 'Germany', 'Smart'], ['WMW', 'Germany', 'MINI'], ['WMX', 'Germany', 'Mercedes-AMG'], ['WP0', 'Germany', 'Porsche (OBDII-Y6)'], ['WP1', 'Germany ', 'Porsche SUV (OBDII-Y6)'], ['WSM', 'EU', 'Schmitz-Cagobull (truck trailers)'], ['WUA', 'Germany', 'Audi Sport (OBDII-Y6)'], ['WV1', 'Germany', 'Volkswagen Commercial Vehicles '], ['WV2', 'Germany', 'Volkswagen Bus/Van'], ['WV3', 'Germany', 'Volkswagen Trucks'], ['WVG', 'Germany', 'Volkswagen MPV/SUV'], ['WVW', 'Germany', 'Volkswagen'], ['XLE', 'Netherlands', 'Scania'], ['XLR', 'Netherlands', 'DAF Trucks'], ['XTA', 'Russia', 'AvtoVAZ'], ['XTB', 'Russia', 'AZLK '], ['XW8', 'Russia', 'Volkswagen'], ['YB1', 'Belgium', 'Volvo Trucks'], ['YBW', 'Belgium', 'Volkswagen'], ['YCM', 'Belgium', 'Mazda'], ['YE2', 'EU', 'Van Hool (buses)'], ['YK1', 'Finland', 'Saab '], ['YS2', 'Sweden', 'Scania'], ['YS3', 'Sweden', 'Saab '], ['YS4', 'Sweden', 'Scania Bus'], ['YT9', 'Sweden', 'Koenigsegg Automotive AB[11]'], ['YTN', 'Sweden', 'Saab NEVS'], ['YV1', 'Sweden', 'Volvo Cars '], ['YV2', 'Sweden', 'Volvo Trucks'], ['YV3', 'Sweden', 'Volvo Buses '], ['YV4', 'Sweden', 'Volvo Cars'], ['ZA9', 'Italy', 'Bugatti'], ['ZAM', 'Italy', 'Maserati'], ['ZAP', 'Italy', 'Piaggio[12]'], ['ZAR', 'Italy', 'Alfa Romeo '], ['ZCF', 'Italy', 'Iveco'], ['ZFA', 'Italy', 'Fiat'], ['ZFC', 'EU', 'Fiat V.I.'], ['ZFF', 'Italy', 'Ferrari'], ['ZGA', 'Italy', 'Iveco Bus'], ['ZHW', 'Italy', 'Lamborghini '], ['ZLA', 'Italy', 'Lancia']]
wdb_list = [["638","Mark 1 Vito"], ["639","Mark 2 Vito"], ["670","Vario"], ["901","Sprinter"], ["902","Sprinter"], ["903","Sprinter"], ["904","Sprinter"], ["905","Sprinter"], ["906","Sprinter NCV3"], ["907","Sprinter VS30 (RWD)"], ["910","Sprinter VS30 (FWD)"], ["930","Actros Rigids"], ["933","Actros MP2 concrete mixer"], ["934","Actros MP2 tractor"], ["944","Axor Tractor"], ["950","Axor Rigids / Actros Mk1 Rigids"], ["954","Actros Mk1 Tractor"], ["957","Econic"], ["963","NEW ACTROS MP4"], ["964","NEW ACTROS MP4"], ["970","Atego"], ["976","Atego Fire"]]
cable_list = ['OBDII-Y3','OBDII-Y4','OBDII-Y5','OBDII-Y6','FMS','BHGV (+BTDC, BTUH for remote tachograph download)']


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		vin_input = request.form["vin"].upper()
		return redirect(url_for("count", vin=vin_input))
	else:
		return render_template("index.html")

@app.route("/<vin>")
def count(vin):
	if len(vin)!=17:
		return f"<h1>VIN should be 17 digits. Try again.</h1>"
	else:
		return year(vin)

def year(vin):
	year = 0 
	if vin[9].isdigit():
		year = int(vin[9]) + 2000
	else:
		for y in year_char:
			if (vin[9]) == y:
				year = 2010 + year_char.index(y)
	return mercedes_check(vin, year)

def mercedes_check(vin, year):
	country = 'N/A'
	model = 'N/A'
	cable = 'N/A'
	if vin[0:3] == 'WDB':
		for element in wdb_list:
			if vin[3:6]	== element[0]:
				country = 'Germany'
				model = element[1]
				if wdb_list.index(element) < 11:
					cable = cable_list[0]
				else: cable = 'Check the Mercedes-Benz Portal'
		return f"<h1>Country: {country} </br>Make/Model: {model} </br>Year: {year} (not 100% accurate) </br>Cable: {cable}</h1>"
	else: 
		return nested_check(vin, model, country, year, cable)

def nested_check(vin, model, country, year, cable):
	for i in nested:
		if vin[0:3] == i[0]:
			country = i[1]
			model = i[2]
			if "car" in model.lower():
				cable = cable_list[1]
	if country=="N/A": 
		return c_check(vin, model, country, year)
	else: 
		return f"<h1>Country: {country} </br>Make/Model: {model} </br>Year: {year} (not 100% accurate) </br>Cable: {cable}</h1>"

def c_check(vin, model, country, year):
	if vin[0] not in country_char[15:24]: 
		country = "Outside of UK/EU"
	elif vin[0]=='W': 
		country = "Germany"
	elif vin[0]=='S': 
		if vin[1] in country_char[0:12]: 
			country = "UK" 
		elif vin[1] in country_char[12:17]: 
			country = "Germany" 
	elif vin[0]=='V':
		if vin[1] in country_char[0:5]: 
			country = "Austria" 
		elif vin[1] in country_char[5:15]: 
			country = "France"
	elif vin[0]=='Y' and vin[1] in country_char[15:20]: 
		country = "Sweden" 
	elif vin[0]=='Z' and vin[1] in country_char[0:15]: 
		country = "Italy"
	elif vin[0]=='T' or vin[0]=='U' or vin[0]=='X':
		country = 'EU'
	else: country
	return f"<h1>Country: {country} </br>Make/Model: {model} </br>Year: {year} (not 100% accurate)</h1>"

if __name__ == "__main__":
	app.run(debug=True)

