vin = input("Type your VIN: ").upper() 
result = ""
year_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y']
country_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nested = [["SAB","UK","Optare"], ["SAJ","UK","Jaguar"], ["SAL","UK","Land Rover"], ["SAR","UK","Rover "], ["SAT","UK","Triumph"], ["SB1","UK","Toyota "], ["SBM","UK","McLaren Automotive "], ["SCC","UK","Lotus Cars "], ["SCF","UK","Aston Martin Lagonda Limited "], ["SCE","UK","DeLorean"], ["SFD","UK","Alexander Dennis"], ["SFE","UK","Alexander Dennis (North America)"], ["SHH","UK","Honda "], ["SHS","UK","Honda"], ["SJN","UK","Nissan "], ["SUD","Poland","Wielton"], ["TCC","Switzerland","Micro Compact Car"], ["TEB","UK/Switzerland","Johnston sweeper (Bucher)"], ["TMA","Czech Republic","Hyundai "], ["TMB","Czech Republic","Škoda "], ["TRU","Hungary","Audi "], ["TSM","Hungary","Suzuki "], ["U5Y","Slovakia","Kia"], ["UU","Romania","Dacia "], ["VA0","Austria","ÖAF "], ["VF1","France","Renault"], ["VF2","France","Renault"], ["VF3","France","Peugeot "], ["VF4","France","Talbot"], ["VF5","France","Iveco"], ["VF6","France","Renault Trucks/Volvo "], ["VF7","France","Citroën"], ["VF8","France","Matra/Talbot/Simca"], ["VF9","France","Bugatti"], ["VFE","France","IvecoBus"], ["VNK","France","Toyota"], ["VR1","France","DS Automobiles"], ["VSS","Spain","SEAT "], ["VS7","Spain","Citroën"], ["VV9","Spain","Tauro Sport Auto"], ["WAG","Germany","Neoplan"], ["WAU","Germany","Audi "], ["WAP","Germany","Alpina "], ["WBA","Germany","BMW"], ["WBS","Germany","BMW M "], ["WBX","Germany","BMW"], ["WDB","Germany","Mercedes-Benz "], ["WDC","Germany","DaimlerChrysler AG/Daimler AG"], ["WDD","Germany","DaimlerChrysler AG/Daimler AG"], ["WMX","Germany","DaimlerChrysler AG/Daimler AG"], ["WEB","Germany","EvoBus "], ["WF0","Germany","Ford of Europe"], ["WJM","Germany","Iveco"], ["WJR","Germany","Irmscher "], ["WKK","Germany","Karl Kässbohrer Fahrzeugwerke "], ["WMA","Germany","MAN"], ["WME","Germany","Smart "], ["WMW","Germany","Mini "], ["WP0","Germany","Porsche car"], ["WP1","Germany ","Porsche SUV"], ["WUA","Germany","Quattro"], ["WVG","Germany","Volkswagen "], ["WVW","Germany","Volkswagen"], ["WV1","Germany","Volkswagen Commercial Vehicles "], ["WV2","Germany","Volkswagen Commercial Vehicles "], ["W09","Germany","Ruf Automobile "], ["W0L","Germany","Opel/Vauxhall "], ["W0SV","Germany","Opel Special Vehicles "], ["XLR","Netherlands","DAF Trucks "], ["XTA","Russia","AvtoVAZ"], ["XTB","Russia","AZLK "], ["YK1","Finland","Saab "], ["YS2","Sweden","Scania, Södertälje "], ["YS3","Sweden","Saab "], ["YS4","Sweden","Scania, Katrineholm "], ["YTN","Sweden","Saab NEVS"], ["YV1","Sweden","Volvo Cars "], ["YV2","Sweden","Volvo Trucks "], ["YV3","Sweden","Volvo Buses "], ["YT9","Sweden","Koenigsegg Automotive AB[11]"], ["ZA9","Italy","Bugatti"], ["ZAM","Italy","Maserati"], ["ZAP","Italy","Piaggio[12]"], ["ZAR","Italy","Alfa Romeo "], ["ZCF","Italy","Iveco"], ["ZFA","Italy","Fiat"], ["ZFF","Italy","Ferrari"], ["ZGA","Italy","IvecoBus"], ["ZHW","Italy","Lamborghini "], ["ZLA","Italy","Lancia"]]


def count(vin):
	while len(vin)!=17:
		vin = input("VIN should be 17 digits. Try again: ").upper() 
	return mcy_check(vin)

def mcy_check(vin):
	year = 0 
	country = "N/A"
	model = "N/A"
	if vin[9].isdigit():
		year = int(vin[9]) + 2000
	else:
		for i in year_letters:
			if (vin[9]) == i:
				year = 2010 + year_letters.index(i)
	for list in nested:
		if vin[0:3] == list[0]:
			country = list[1]
			model = list[2]
	if country=="N/A": 
		c_check(vin, model, year) 
	else:
		print(f"mcy_check => \nYear: {year} \nCountry: {country} \nMake/Model: {model}")

def c_check(vin, model, year):
	# country
	if vin[0] not in country_letters[15:24]: 
		country = "Outside of UK/EU"
	elif vin[0]=='W': 
		country = "Germany"
	elif vin[0]=='S': 
		if vin[1] in country_letters[0:12]: 
			country = "UK" 
		elif vin[1] in country_letters[12:17]: 
			country = "Germany" 
	elif vin[0]=='V':
		if vin[1] in country_letters[0:5]: 
			country = "Austria" 
		elif vin[1] in country_letters[5:15]: 
			country = "France"
	elif vin[0]=='Y' and vin[1] in country_letters[15:20]: 
		country = "Sweden" 
	elif vin[0]=='Z' and vin[1] in country_letters[0:15]: 
		country = "Italy" 
	else: country

	print(f"c_check called with the vin!: {vin, model, year}")

count(vin)
