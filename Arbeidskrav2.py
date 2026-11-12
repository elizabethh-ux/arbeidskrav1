# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 

"""
# %% Oppgave 1 
# Beregning av alder i 2024 
# Bruker oppgir fødselsår, og programmet regner ut alder 

alder = int(input('Hvilket år er du født? '))
beregningsaar = 2024
resultat = beregningsaar - alder # trekker fødselsår fra beregningsåret for å finne alderen

print('Du fyller' , resultat, 'år i 2024') # skriver ut resultat

# %% Oppgave 2
# Beregning av antall pizzaer til klassefest 
# Hver elev spiser en fjerdel av en pizza 
# Antall pizzaer må rundes opp siden vi bare kan kjøpe hele pizzaer 

import math 
antall_elever = int(input('Skriv inn antall elever: '))
elever_per_pizza = 4
pizzaer = antall_elever / elever_per_pizza # deler antall elever på 4 for å finne pizzabehovet 
pizzaer = math.ceil(pizzaer) # runder opp til nærmeste hele pizza 

print('Det må handles inn', pizzaer, 'pizzaer til festen')

# %% Oppgave 3
# Omregning fra grader til radianer 
# Bruker en funksjon som beregner radianer ved hjelp av pi

import numpy as np 
def grader_til_radianer(grader): 
    return grader * np.pi/180 # ganger grader med pi og deler på 180

v_grad = float(input('Skriv inn gradtallet: '))
v_rad = grader_til_radianer(v_grad) # bruker funksjonen til å beregne radianer 

print(v_grad, 'grader er', v_rad, 'radianer')


# %% Oppgave 4 
# Oppretter dictionary med land, hovedsteder og innbyggertall 
# Programmet skal hente informasjon om et valgt land 
# Brukeren skal kunne legge til et nytt land etterpå

# 4a. 

data = {
        'Norge': ['Oslo', 0.634],
        'England': ['London', 8.982],
        'Frankrike': ['Paris', 2.161],
        'Italia' : ['Roma', 2.873]
        }

# 4b 

land = input('Skriv inn et land:').strip()
hovedstad = data[land][0] # henter hovedstaden til landet
innbyggere = data[land][1] # henter innbyggertallet i millioner 
print(hovedstad, 'er hovedstaden i', land, 'og det er', innbyggere, 'mill. innbyggere i', hovedstad)

 # 4c. 
 
nytt_land = input('Skriv inn et nytt land: ')
ny_hovedstad = input('Hva heter hovedstaden? ')
nye_innbyggere = float(input('Antall innbyggere i millioner: '))

data[nytt_land] = [ny_hovedstad, nye_innbyggere] # legger til det nye landet 
print(data)

# %% Oppgave 5
# Beregning av areal og ytre omkrets av en sammensatt figur 
# Figuren består av en rettvinklet trekant og en halvsirkel 
# Bruker Pytagoras for å finne den skrå siden 

import math 

def beregn_figur(a, b):
    radius = a / 2 # radius er halvparten av diameteren 
    areal_trekant = a * b / 2 # beregner arealet av trekanten 
    areal_halvsirkel = math.pi * radius **2 / 2 # beregner arealet av halvsirkelen
    areal = areal_trekant + areal_halvsirkel # legger sammen arealene 
    
    skraa_side = math.sqrt(a**2 + b**2)
    omkrets = b + skraa_side + math.pi * radius 
    
    return areal, omkrets # returnerer begge resultatene 
a = 4
b = 6
areal, omkrets = beregn_figur(a, b) # tester funksjon med a = 4 og b = 6
print('Areal:', areal)
print('Ytre omkrets:', omkrets)

# %% Oppgave 6 
# Plotter funksjonen f(x) = -x**2 - 5 
# Lager 200 punkter mellom -10 og 10 
# Bruker matplotlib til å tegne grafen 

import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-10, 10, 200) # lager 200 jevnt fordelte x-verdier 
y = -x**2 - 5  # beregner y-verdiene 

plt.plot(x, y) # tegner grafen
plt.show() # viser grafen 


