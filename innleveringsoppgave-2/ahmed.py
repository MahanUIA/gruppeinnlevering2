print("Hei erling, det har oppstått noen konflikter i teamet")
print("\n\nUenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til personkonflikt. Silje mener løsningen Sivert foreslår vil låse brukeropplevelsen og hindre innovasjon.Sivert mener Siljes forslag er urealistisk, usikkert og for kostbart. Diskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet.") 
print("1: Kjøre workshop for å legge grunnlag for teambuilding. La konflikten vente på seg litt.")
print("2: Erling velger Siverts løsning uten å vurdere alternativene ordentlig, fordi han ikke har tid til det.")

#Disse første linjene fungerer som en introduksjon til programmet, pluss at den presenterer problemstillingen og valgmulighetene

poeng = 0
#Vi oppretter en variabel som lagrer brukerens poeng underveis
valg = int(input("hva velger du?"))
if valg == 1:
    poeng = 1

#Hvis brukeren velger alternativ 1, skal han få 1 poeng. Hvis han velger 2 skal han ikke få noe poeng, og da trengs ikke poeng-variabelen å endres heller.

print ("Takk for svar! Her er neste problemstlling")
print("\nSITUASJON 2: HVORDAN FORHINDRE AT KONFLIKTEN MELLOM HAMDI OG JABIR BLUSSER OPP?")
print("1: Kjøre avstemning med alle i bedriften og komme til kompromiss. Demokratisk løsning.")
print("2: Erling unngår konflikten.")
print("3: Erling analyserer saken selv, og tar en sjefsavgjørelse basert på fakta.")


valg = int(input ("Hva velger du?"))
if valg == 1:
    poeng=poeng+1
elif valg==2:
    poeng = poeng-0.5
elif valg ==3:
    poeng = poeng +0.5
else:
    print ("Ugyldig svar")

#Vi sjekker hva brukeren svarer. Om han svarer feil, får han opp en feilmelding.

print("\nSITUASJON 3: HVORDAN BEVARE MOTIVASJONEN I TEAMET SOM HELHET?")
print("1: Erling inviterer hele gjengen på restaurant, på prosjektets regning.")
print("2: Erling avvikler 1 ukes ferie for alle prosjektets ansatte.")
print("3: Erling fokuserer utelukkende på effektivitet, og får teamet til å jobbe med prosjektet.")
valg = int(input("Hva velger du?"))
if valg == 1:
    poeng = poeng+1
elif valg == 2:
    poeng = poeng+0.5
else:
    print ("Ugyldig svar")

if poeng <= 1:
    print ("\nKonfliktene løses ikke, resultatet blir svekket og gruppa får ikke gjort det de skal til rett tid. Stilling din blir satt under press av kommunestyret.")

if poeng >1 and poeng < 2:
    print ("\nDet gjenstår noe dårlig stemning, men produktiviteten er tilstrekkelig til å fortsette med prosjektsamarbeidet")

if poeng >=2:
    print ("\nKonfliktene blir løst og gruppa jobber godt sammen! Produktiviteten er veldig god.")

#Til slutt sjekkes det hvor mange poeng brukeren har fått underveis i programmet: om han har 1 eller mindre, mellom 1 og 2, eller mer enn 2 poeng, og får melding om resultat basert på dette.
