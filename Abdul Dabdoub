poeng = 0

print("Velkomen Erling...")
print("Her velger du hvordan du kan kåndtere konflikten")



"""
1. printe problemstilling 
2. presentere valgmuligheter
"""
def presentereproblemogvalg(problemstilling, valgmuligheter):
    print(problemstilling)

    counter = 0
    for valg in valgmuligheter:
        counter += 1
        print(str(counter) + ". " + valg)
    brukervalg = 0
    if len(valgmuligheter) == 2:
        brukervalg = int(input("Velg 1 eller 2"))
    if len(valgmuligheter) == 3:
        brukervalg = int(input("Velg 1, 2 eller 3: "))

    while (brukervalg != 1) and (brukervalg != 2) and (brukervalg != 3):
        print("Ugyldig svar!")
        brukervalg = int(input("Velg 1, 2 eller 3: "))

    return brukervalg


problem1 = "Uenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en personkonflikt. Silje mener løsningen Sivert foreslår vil låse brukeropplevelsen og hindre innovasjon. Sivert mener Siljes forslag er urealistisk, usikkert og for kostbart."

y = [
    "Valg 1: Kjøre workshop for å legge grunnlag for teambuilding, og la konflikten vente på seg foreløpig.",
    "Valg 2: Velge Siverts løsning nå, du har ikke tid til å sette deg inn i det",
]

if presentereproblemogvalg(problem1, y) == 1:
    poeng = poeng + 1

print("Poeng:", poeng)



problem2 = """
Samtidig med konflikten mellom Silje og Sivert oppstår det spenning mellom Hamdi(kulturavdelingen) og Jabir (brukerrepresentant).De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter:• Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterendeplattform.• Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser. Prosjektetnærmer seg en viktig milepæl: første prototype skal være klar om tre uker. Stemningen erspent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan avgjøre omteamet beveger seg videre mot “norming” – eller blir stående fast i stormen.
"""

d = [
    " valg 1: Kjøre en avstemning i teamet og gå for et kompromissr",
    " valg 2:Unngå konflikten, og la Hamdi og Jabir finne ut av det selv",
    " valg 3: Analyser saken selv, og ta en sjefsvgjørelse"
    ]

brukervalg = presentereproblemogvalg(problem2, d)

if brukervalg == 1:
    poeng = poeng + 1
    print ("du valgte å ta initiativ til et felles møte")
if brukervalg == 2:
    poeng = poeng -0.5
else:
    poeng = poeng + 0.5
    print("du valgte å avvente og håpe at partene finner en løsning selv")


problem3 = """
Hvordan bevare motivasjonen i teamet som helhet?"""

e =[
    " valg 1: Invitere hele teamet på restaurant på prosjektets regning, for å bygge samhold i teamet "
    " valg 2: Avvikle 1 ukes ferie for hele teamet"
    " valg 3: Fokusere 100% på effektivitet, og kun få teamet til å jobbe med arbeidet"
    ]

brukervalg = presentereproblemogvalg(problem3, e)

if brukervalg == 1:
    poeng = poeng + 1
    print("du valgte å sette av tid til relasjonsbygging og sosiale aktiviteter for å gjenopprette tillit")
if brukervalg == 2:
    poeng = poeng + 0.5
    print("du valgte å prioritere fremdrift og leveranser for å holde fokus på resultatet")


if poeng >= 2.5:
    print("Konfliktene blir løst og gruppa jobber godt sammen! Produktiviteten er veldig god.")
elif poeng <2.1 and poeng > 1:
    print("Det gjenstår noe dårlig stemning, men produktiviteten er tilstrekkelig til å fortsette med prosjektsamarbeidet.")
else:
    print("Konfliktene løses ikke, resultatet blir svekket og gruppa får ikke gjort det de skal til rett tid. Stilling din blir satt under press av kommunestyret.")

