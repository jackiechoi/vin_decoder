# check.py

vin = input("VIN: ").upper()

year_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y']

nested = [["SAB","UK","Optare"], ["SAJ","UK","Jaguar"], ["SAL","UK","Land Rover"], ["SAR","UK","Rover "], ["SAT","UK","Triumph"], ["SB1","UK","Toyota"], ["SBM","UK","McLaren Automotive "], ["SCC","UK","Lotus Cars "], ["SCF","UK","Aston Martin Lagonda Limited"], ["SCE","UK","DeLorean"], ["SFD","UK","Alexander Dennis"], ["SFE","UK","Alexander Dennis (North America)"], ["SHH","UK","Honda "], ["SHS","UK","Honda"], ["SJN","UK","Nissan"], ["SUD","Poland","Wielton"], ["TCC","Switzerland","Micro Compact Car"], ["TEB","UK/Switzerland","Johnston sweeper (Bucher)"], ["TMA","Czech Republic","Hyundai "], ["TMB","Czech Republic","Škoda"], ["TRU","Hungary","Audi "], ["TSM","Hungary","Suzuki "], ["U5Y","Slovakia","Kia"], ["UU","Romania","Dacia "], ["VA0","Austria","ÖAF "], ["VF1","France","Renault"], ["VF2","France","Renault"], ["VF3","France","Peugeot"], ["VF4","France","Talbot"], ["VF5","France","Iveco"], ["VF6","France","Renault Trucks/Volvo"], ["VF7","France","Citroën"], ["VF8","France","Matra/Talbot/Simca"], ["VF9","France","Bugatti"], ["VFE","France","Iveco Bus"], ["VNK","France","Toyota"], ["VR1","France","DS Automobiles"], ["VSS","Spain","SEAT"], ["VS7","Spain","Citroën"], ["VV9","Spain","Tauro Sport Auto"], ["WAG","Germany","Neoplan"], ["WAU","Germany","Audi "], ["WAP","Germany","Alpina "], ["WBA","Germany","BMW"], ["WBS","Germany","BMW M "], ["WBX","Germany","BMW"], ["WDB","Germany", "Mercedes-Benz"], ["WDC","Germany","DaimlerChrysler"], ["WDD","Germany","Mercedes-Benz"], ["WMX","Germany","Mercedes-AMG"], ["WEB","Germany","EvoBus (Mercedes-Bus)"], ["WF0","Germany","Ford"], ["WJM","Germany","Iveco Magirus"], ["WJR","Germany","Irmscher "], ["WKK","Germany","Karl Kässbohrer Fahrzeugwerke "], ["WMA","Germany","MAN"], ["WME","Germany","Smart"], ["WMW","Germany","MINI"], ["WP0","Germany","Porsche car"], ["WP1","Germany ","Porsche SUV"], ["WUA","Germany","Audi Sport"], ["WVG","Germany","Volkswagen MPV/SUV"], ["WVW","Germany","Volkswagen"], ["WV1","Germany","Volkswagen Commercial Vehicles "], ["WV2","Germany","Volkswagen Commercial Vehicles "], ["W09","Germany","Ruf Automobile "], ["W0L","Germany","Opel/Vauxhall"], ["W0SV","Germany","Opel Special Vehicles "],["XLR","Netherlands","DAF Trucks"], ["XTA","Russia","AvtoVAZ"], ["XTB","Russia","AZLK "], ["YK1","Finland","Saab "], ["YS2","Sweden","Scania"], ["YS3","Sweden","Saab "], ["YS4","Sweden","Scania Bus"], ["YTN","Sweden","Saab NEVS"], ["YV1","Sweden","Volvo Cars "], ["YV2","Sweden","Volvo Trucks"], ["YV3","Sweden","Volvo Buses "], ["YT9","Sweden","Koenigsegg Automotive AB[11]"], ["ZA9","Italy","Bugatti"], ["ZAM","Italy", "Maserati"], ["ZAP","Italy","Piaggio[12]"], ["ZAR","Italy","Alfa Romeo "], ["ZCF","Italy","Iveco"], ["ZFA","Italy","Fiat"], ["ZFF","Italy","Ferrari"], ["ZGA","Italy","Iveco Bus"], ["ZHW","Italy","Lamborghini "], ["ZLA","Italy","Lancia"], ["XLE", "Netherlands", "Scania"], ["JAA","Japan","Isuzu"],["MPA","Japan","Isuzu"], ["SCB","EU","Bentley"], ["SDB","UK","Peugeot"], ["VLU","France","Scania"], ["VSK","Spain","Nissan"], ["VNV","UK","Renault-Nissan"], ["VSA","Spain","Mercedes-Benz"], ["VSE","Spain","Suzuki"], ["VAN","Austria","MAN"], ["UU1","Romania","Renault Dacia"], ["TYB","Portugal","Mitsubishi Truck"], ["TYA","Portugal","Mitsubishi Truck"], ["TM9","Czech Republic","Škoda trolleybus"], ["TMP","Czech Republic","Škoda trolleybus"], ["SKF","EU","Vauxhall"], ["SFA","UK","Ford"], ["SCA","UK","Rolls Royce"], ["VSX","Spain","Opel"],["VS6","Spain","Ford"],["VWA","Spain","Nissan"],["VWV","Spain","Volkswagen"], ["WA1","EU","Audi SUV"], ["WBW","EU","BMW"], ["WBY","EU","BMW"], ["WDA","EU","Daimler"], ["WDF","EU","Mercedes-Benz (commercial vehicles)"], ["WSM","EU","Schmitz-Cargobull (truck trailers)"], ["W0V","Germany","Opel"], ["WV3","Germany","Volkswagen Trucks"], ["XW8","Russia","Volkswagen"],["YBW","Belgium","Volkswagen"], ["YB1","Belgium","Volvo Trucks"], ["YCM","Belgium","Mazda"], ["YE2","EU","Van Hool (buses)"], ["ZFC","EU","Fiat V.I."]]

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
			print(f"List[0]: {list[0]}")
			print(f"List[1]: {list[1]}")
			print(f"List[2]: {list[2]}")
			country = list[1]
			model = list[2]
	print(vin[0:3])
	print(vin[0:3])
	print(f"Nested checked => Year: {year} (not 100% accurate) \nCountry: {country} \nMake/Model: {model}")


mcy_check(vin)
