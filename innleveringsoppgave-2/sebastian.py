print("Hei, Erling. Du må gjøre noen beslutninger for håndtere et par konflikter som har oppstått i prosjektgruppen.")
poeng = 0

#Vi bruker et poengsystem for å enklere komme til en konklusjon basert på beslutningene. Den starter på 0.

# Situasjon 1
print("SITUASJON 1: HVORDAN HÅNDTERE KONFLIKTEN MELLOM SILJE OG SIVERT?")
print("1: Kjøre workshop for å legge grunnlag for teambuilding. La konflikten vente på seg litt.")
print("2: Erling velger Siverts løsning uten å vurdere alternativene ordentlig, fordi han ikke har tid til det.")

valg = input("Ditt valg (1/2): ")
while valg not in ["1", "2"]:
    valg = input("Ugyldig valg. Velg 1 eller 2: ")

#Hvis brukeren skriver noe annet enn 1 eller 2, spør programmet på nytt.

if valg == "1":
    poeng += 1
elif valg == "2":
    poeng += 0

# Situasjon 2
print("\nSITUASJON 2: HVORDAN FORHINDRE AT KONFLIKTEN MELLOM HAMDI OG JABIR BLUSSER OPP?")
print("1: Kjøre avstemning med alle i bedriften og komme til kompromiss. Demokratisk løsning.")
print("2: Erling unngår konflikten.")
print("3: Erling analyserer saken selv, og tar en sjefsavgjørelse basert på fakta.")

#bruker n/ for å gi litt plass mellom de forskjellige situasjonene, sånn at det er lettere å se når den nye blir presentert.

valg = input("Ditt valg (1/2/3): ")
while valg not in ["1", "2", "3"]:
    valg = input("Ugyldig valg. Velg 1, 2 eller 3: ")
if valg == "1":
    poeng += 1
elif valg == "2":
    poeng += 0
elif valg == "3":
    poeng -= 0.5

# Situasjon 3
print("\nSITUASJON 3: HVORDAN BEVARE MOTIVASJONEN I TEAMET SOM HELHET?")
print("1: Erling inviterer hele gjengen på restaurant, på prosjektets regning.")
print("2: Erling avvikler 1 ukes ferie for alle prosjektets ansatte.")
print("3: Erling fokuserer utelukkende på effektivitet, og får teamet til å jobbe med prosjektet.")

valg = input("Ditt valg (1/2/3): ")
while valg not in ["1", "2", "3"]:
    valg = input("Ugyldig valg. Velg 1, 2 eller 3: ")
if valg == "1":
    poeng += 1
elif valg == "2":
    poeng += 0
elif valg == "3":
    poeng -= 0.5

# Konklusjon
print("\nResultat av dine valg:")
if poeng > 2:
    print("Konklusjon 1: Konfliktene blir løst og gruppa jobber stabilt sammen og går inn i performing-fasen.")
elif 0 <= poeng <= 2:
    print("Konklusjon 2: Det gjenstår noe dårlig stemning, og produktiviteten er tilstrekkelig til å fortsette.")
else:
    print("Konklusjon 3: Konfliktene løses ikke, resultatet blir svekket og gruppa får ikke gjort det de skal til rett tid. Stillingen til Erling blir satt under press av kommunestyret.")
