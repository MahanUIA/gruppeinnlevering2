def get_choice(prompt, valid_choices):
    choice = input(prompt)
    while choice not in valid_choices:
        print("Prøve igjen, du har alternativene: ", valid_choices)
        choice = input(prompt)
    return choice

points = 0
print("Hei Erling, du må gjøre en rekke valg for å guide teamet ditt")
print()
print("SITUASJON 1: HVORDAN HÅNDTERE KONFLIKTEN MELLOM SILJE OG SIVERT?")
print()
print("Valg 1: Kjøre workshop for å legge grunnlag for teambuilding. La konflikten vente på seg litt.")
print("Valg 2: Erling velger Siverts løsning uten å vurdere alternativene ordentlig, fordi han ikke har tid til det.")
print()
svar1 = get_choice("Velg mellom alternativ 1 og 2: ", ["1", "2"])
if svar1 == "1":
    print("Du har valgt valg 1")
    points += 10
elif svar1 == "2":
    print("Du har valgt valg 2")
    points -= 5

print()
print("SITUASJON 2: HVORDAN FORHINDRE AT KONFLIKTEN MELLOM HAMDI OG JABIR BLUSSER OPP?")
print()
print("Valg 1: Kjøre avstemning med alle i bedriften og komme til kompromiss. Demokratisk løsning.")
print("Valg 2: Erling unngår konflikten.")
print("Valg 3: Erling analyserer saken selv, og tar en sjefsavgjørelse basert på fakta.")
print()
svar2 = get_choice("Select a choice between alternative 1, 2, and 3: ", ["1", "2", "3"])
if svar2 == "1":
    print("Du har valgt valg 1")
    points += 10
elif svar2 == "2":
    print("Du har valgt valg 2")
    points -= 5
elif svar2 == "3":
    print("Du har valgt valg 3")
    points += 5

print()
print("SITUASJON 3: HVORDAN BEVARE MOTIVASJONEN I TEAMET SOM HELHET?")
print()
print("Valg 1: Erling inviterer hele gjengen på restaurant, på prosjektets regning.")
print("Valg 2: Erling avvikler 1 ukes ferie for alle prosjektets ansatte.")
print("Valg 3: Erling fokuserer utelukkende på effektivitet, og får teamet til å jobbe med prosjektet.")
print()
svar3 = get_choice("Select a choice between alternative 1, 2, and 3: ", ["1", "2", "3"])
if svar3 == "1":
    print("Du har valgt valg 1")
    points += 10
elif svar3 == "2":
    print("Du har valgt valg 2")
    points += 5
elif svar3 == "3":
    print("Du har valgt valg 3")
print()
print("Resultat:")
if points >= 20:
    print("Konfliktene blir løst og gruppa jobber stabilt sammen og går inn i performing-fasen.")
elif 10 <= points < 20:
    print("Det gjenstår noe dårlig stemning, og produktiviteten er tilstrekkelig til å fortsette.")
else:
    print("Konfliktene løses ikke, resultatet blir svekket og gruppa får ikke gjort det de skal til rett tid. Stillingen din blir satt under press av kommunestyret.")
