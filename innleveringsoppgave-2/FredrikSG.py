print("Interaktiv story prosjekt.")
poeng = 0
#Starter storyen med 0 poeng

#Første situasjon
print("Situasjon 1: Hvordan håndtere konflikten mellom silje og sivert?")
print("1: Kjøre workshop for å legge grunnlag for teambuilding. La konflikten vente på seg litt.")
print("2: Erling velger Siverts løsning uten å vurdere alternativene ordentlig, fordi han ikke har tid til det.")

valg = int(input("Velg mellom 1 og 2: "))
while (valg !=1) and (valg !=2):
    print ("Ugyldig valg!!")
    valg=int(input("Velg mellom 1 og 2"))
if valg == 1:
    poeng += 10
elif valg == 2:
    poeng += 0

#Situasjon 2
print("Situasjon 2: Hvordan forhindre at konflikten mellom Hamdi og Jabir blusser opp")
print("1: Kjøre avstemning med alle i bedriften og komme til kompromiss. Demokratisk løsning.")
print("2: Erling unngår konflikten.")
print("3: Erling analyserer saken selv, og tar en sjefsavgjørelse basert på fakta")

valg = int(input("Velg mellom 1, 2 og 3:"))
while (valg !=1) and (valg !=2) and (valg !=3):
    print ("ugyldig valg")
    valg = int(input("Velg mellom 1, 2 og 3"))
if valg == 1:
    poeng += 10
elif valg == 2:
    poeng +=0
elif valg == 3:
    poeng +=5

#Situasjon 3
print("Situasjon 3: Hvordan bevare motivasjonen i teamet som en helhet?")
print("1: Erling inviterer hele teamet med på restaurant, på prosjektets regning.")
print("2: Erling avvikler 1 ukes ferie for alle prosjektets ansatte.")
print("3: Erling fokuserer utelukkende på effektivitet, og får teamet til å jobbe med prosjektet")

valg = int(input("velg mellom 1, 2 og 3: "))
while (valg !=1) and (valg !=2) and (valg !=3):
    print("ugyldig valg")
    valg = int(input("Velg mellom 1, 2 og 3"))
if valg == 1:
    poeng += 10
elif valg == 2:
    poeng +=5
elif valg == 3:
    poeng += 0

#RESULTAT
print("RESULTAT")
print(poeng, "POENG")
if poeng > 20:
    print("Resultat 1: Konflikten blir løst og gruppa jobber stabilt sammen og går inn i performing fasen.")
elif 10 < poeng <= 20:
    print("Resultat 2: Det gjenstår noe dårlig stemning, og produktiviteten  er tilstrekkelig til å fortsette.")
else:
    print("Resultat 3: Konfliktene løses ikke, resultate blir svekket og gruppa får ikke gjort det de skal til rett tid. Stillingen til Erling blir satt under press av kommunestyret.")

