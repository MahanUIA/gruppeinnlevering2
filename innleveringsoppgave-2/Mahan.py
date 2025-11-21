poeng = 0

def presentereProblemOgValg(problemStilling, valgMuligheter):
    global poeng
    print(problemStilling)
    print("Hvilket valg tar du?")
    
    for index, valg in enumerate(valgMuligheter):
        print(str(index + 1) + ": " + valg[0])
        
    while True:
        try:
            brukerValg = int(input("Velg et alternativ: "))
            if brukerValg > 0 and brukerValg <= len(valgMuligheter):
                break
            else:
                print("Feil valg, prøv igjen")
        except ValueError:
            print("Ugyldig verdi")
            
    valget = valgMuligheter[brukerValg-1]
    
    print(f"Du valgte: {valget[0]}") 
    poeng += valget[1]
    print("\n")

# --- SITUASJON 1 ---
presentereProblemOgValg(
    "Situasjon 1: Hvordan håndtere konflikten mellom Silje og Sivert?",
    [
        ("Kjøre workshop for å legge grunnlag for teambuilding. La konflikten vente på seg litt.", 10),
        ("Erling velger Siverts løsning uten å vurdere alternativene ordentlig, fordi han ikke har tid til det.", 0)
    ]
)

# --- SITUASJON 2 ---
presentereProblemOgValg(
    "Situasjon 2: Hvordan forhindre at konflikten mellom Hamdi og Jabir blusser opp?",
    [
        ("Kjøre avstemning med alle i bedriften og komme til kompromiss. Demokratisk løsning.", 5),
        ("Erling unngår konflikten.", 0),
        ("Erling analyserer saken selv, og tar en sjefsavgjørelse basert på fakta.", 10)
    ]
)

# --- SITUASJON 3 ---
presentereProblemOgValg(
    "Situasjon 3: Hvordan bevare motivasjonen i teamet som en helhet?",
    [
        ("Erling inviterer hele teamet med på restaurant, på prosjektets regning.", 5),
        ("Erling avvikler 1 ukes ferie for alle prosjektets ansatte.", 10),
        ("Erling fokuserer utelukkende på effektivitet, og får teamet til å jobbe med prosjektet.", 0)
    ]
)

# --- RESULTAT ---
print("-" * 40)
print("RESULTAT")
print(poeng, "POENG")

if poeng > 20:
    print("Resultat 1: Konflikten blir løst og gruppa jobber stabilt sammen og går inn i performing fasen.")
elif 10 < poeng <= 20:
    print("Resultat 2: Det gjenstår noe dårlig stemning, og produktiviteten er tilstrekkelig til å fortsette.")
else:
    print("Resultat 3: Konfliktene løses ikke, resultatet blir svekket og gruppa får ikke gjort det de skal til rett tid. Stillingen til Erling blir satt under press av kommunestyret.")