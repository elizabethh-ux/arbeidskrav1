
"""
arbeidskrav 1 
Elizabeth Gray 

"""
  # Beregning av totalkostnad for elbil 
  # Beregnes strømpris, forsikring, trafikkavgift år, bomavgift
  
km = 10000  # avklare km 
strom = km * 0.2  # først skal jeg finne ut hvor mange kWh bilen bruker på 10 000 km
print(strom)
strompris = strom * 2  # ganger strømmen på 2, da det koster 2kr per kWh 
print(strompris)
forsikring_el = 5000  
trafikkavgift = 8.38 * 365  # avgift er oppgitt hver dag, derfor ganger med 365 for å få årlig avgift
print(trafikkavgift)
bom_el = km * 0.10  # bomavgiften for antall km elbil, ganger km med 0.1 for å finne total bomavgift på 10000km 
print(bom_el)
total_el = strompris + forsikring_el + trafikkavgift + bom_el  # plusser sammen alle kostnader for totalkostnader elbil 
print("Totalkostnad elbil per år:" ,total_el)

  # Beregning av totalkostnad for bensinbil
  # Her er det gjort samme beregninger som for elbil, bruker samme trafikkavgift som for elbil da kostnaden er lik 
  
drivstoff = km * 1  # her ganget med 1, da dette er pris for bensin per km for å finne totalavgift 
print(drivstoff)
forsikring_bensin = 7500
bom_bensin = km * 0.3  # bomavgift for antall km bensin, gjør samme som ved elbil med justert tall
print(bom_bensin)
total_bensin = drivstoff + forsikring_bensin + trafikkavgift + bom_bensin  # totalkostnader bensinbil, plusser sammen alle totalkostander 
print("Totalkostnad bensinbil per år:" ,total_bensin)

  # finne forskjell i avgift per år for elbil og bensinbil 
forskjell = total_bensin - total_el  # totalekostnader for bensinbil minus totale kostnader for elbil
print("Differansen årlige kostnader:" ,forskjell)

  # Vi kan da konkludere med at det er 10 500 kr billigere per 10 000 km med elbil 