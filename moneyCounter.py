import json
import os

# Definizione dei dizionari per monete e banconote
monete = {
    '1c': 0.01,
    '2c': 0.02,
    '5c': 0.05,
    '10c': 0.10,
    '20c': 0.20,
    '50c': 0.50,
    '1': 1,
    '2': 2,
}

banconote = {
    '5': 5,
    '10': 10,
    '20': 20,
    '50': 50,
    '100': 100,
    '200': 200,
    '500': 500,
}

JSON_FILENAME = 'moneycounter.json'

# Se il file JSON non esiste, inizializza i dati
if not os.path.exists(JSON_FILENAME):
    with open(JSON_FILENAME, 'w') as f:
        json.dump({}, f)

def conta_monete(monete_da_inserire):
    with open(JSON_FILENAME, 'r+') as f:
        data = json.load(f)
        for moneta in monete_da_inserire:
            if moneta in monete:
                if moneta not in data:
                    data[moneta] = 0
                data[moneta] += monete_da_inserire[moneta]
    with open(JSON_FILENAME, 'w') as f:
        json.dump(data, f)

def conta_banconote(banconote_da_inserire):
    with open(JSON_FILENAME, 'r+') as f:
        data = json.load(f)
        for banconota in banconote_da_inserire:
            if banconota in banconote:
                if banconota not in data:
                    data[banconota] = 0
                data[banconota] += banconote_da_inserire[banconota]
    with open(JSON_FILENAME, 'w') as f:
        json.dump(data, f)

def stampa_banconote_monete_totali():
    with open(JSON_FILENAME, 'r') as f:
        data = json.load(f)
        num_banconote = sum(data.get(b, 0) for b in banconote)
        num_monete = sum(data.get(m, 0) for m in monete)
        print(f"Numero totale di banconote: {num_banconote}")
        print(f"Numero totale di monete: {num_monete}")

def stampa_saldo_totale():
    with open(JSON_FILENAME, 'r') as f:
        data = json.load(f)
        saldo_totale = sum(data.get(b, 0) * banconote[b] for b in banconote) + sum(data.get(m, 0) * monete[m] for m in monete)
        print(f"Saldo totale: {saldo_totale:.2f}")

# Input del totale di soldi
total_soldi = 0
monete_da_inserire = {}
banconote_da_inserire = {}

while True:
    print("1. Inserisci monete")
    print("2. Inserisci banconote")
    print("3. Vedi numero totale di banconote e monete inserite")
    print("4. Vedi saldo totale")
    print("5. Esci")
    scelta = input("Scelta: ")
    
    if scelta == "5":
        break
    
    if scelta == "1":
        monete_da_inserire = {}
        moneta = input("Inserisci il tipo di moneta (vuoto per terminare): ")
        while moneta:
            quantita = int(input("Inserisci la quantità: "))
            if moneta in monete and quantita > 0:
                monete_da_inserire[moneta] = quantita
            moneta = input("Inserisci il tipo di moneta (vuoto per terminare): ")
        conta_monete(monete_da_inserire)
    
    if scelta == "2":
        banconote_da_inserire = {}
        banconota = input("Inserisci il tipo di banconota (vuoto per terminare): ")
        while banconota:
            quantita = int(input("Inserisci la quantità: "))
            if banconota in banconote and quantita > 0:
                banconote_da_inserire[banconota] = quantita
            banconota = input("Inserisci il tipo di banconota (vuoto per terminare): ")
        conta_banconote(banconote_da_inserire)
    
    if scelta == "3":
        stampa_banconote_monete_totali()
        
    if scelta == "4":
        stampa_saldo_totale()
