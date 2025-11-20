print('Hei Erling! Det har oppstått noen konflikter i prosjektet ditt, og du må ta en rekke valg for å ta vare på teamet ditt.')

print('\nDu får 2 valg: \n')

poeng = 0

#Vi lager variabelen poeng for å lagre brukerens progresjon gjennom storyen.

def PoengFraValg (problem, valgmuligheter):
    # Vi lager en funksjon som tar seg av prosessen med å presentere problemstillingen og valgmulighetene, og som returnerer svaret som brukeren avgir til programmet.
    print (problem)

    for alternativ in valgmuligheter:
        print (alternativ)
        #Presenterer valgmulighetene i terminalen

    #Vi tenkte det var lov å ha flere enn 2 valgmuligheter, og har lagd programmet slik at den kan behandle situasjoner med både 2 og 3 svaralternativer.
    if(len(valgmuligheter) == 2):
        #Dette kjøres om spørsmålet har 2 svaralternativer
        valg = input('\nVelger du A) eller B)?').lower()
        #Spør brukeren om å avgi et svar
    
        while valg != 'a' and valg != 'b':
            #Om brukeren svarer feil, blir den spurt på nytt. Dette legges in en while-løkke, slik at brukeren kan avgi så mange feil svar den vil uten at programmet tryner
            print ('\nUgyldig svar.')
            valg = input('\nVelger du A) eller B)? ').lower()

    if (len(valgmuligheter) == 3):
        #Dette kjøres om spørsmålet har 3 svaralternativer
        valg = input('\nVelger du A), B) eller C)?').lower()
    
        while valg != 'a' and valg != 'b' and valg != 'c':
            print ('\nUgyldig svar.')
            valg = input('\nVelger du A), B) eller C)?').lower()

    return valg
    #Funksjonen returnerer valget til brukeren. Slik logikken er lagt opp, skal det kun være mulig å returnere gyldige svar.

#Situasjon 1:

problem = '\n\nUenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til personkonflikt. Silje mener løsningen Sivert foreslår vil låse brukeropplevelsen og hindre innovasjon.Sivert mener Siljes forslag er urealistisk, usikkert og for kostbart. Diskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet.'

valgListe = ['\nA) Kjøre workshop for å legge grunnlag for teambuilding, og la konflikten vente på seg foreløpig.', '\nB) Velge Siverts løsning nå, du har ikke tid til å sette deg inn i det']

#Problemstilling og valgmuligheter. Valgmuligheter blir lagret i en liste, slik at det blir enklest å gå gjennom dem i funksjonen.

if (PoengFraValg(problem, valgListe) == 'a'):
    poeng = poeng + 10
    #Hvis brukeren svarer A), får han 10 poeng.

#Om brukeren svarer B), får han ingen poeng. Dermed trengs ingenting å gjøres.


#Situasjon 2:

print ('\nTakk! Neste problemstilling:')
problem = '\n\nSamtidig med konflikten mellom Silje og Sivert oppstår det spenning mellom Hamdi(kulturavdelingen) og Jabir (brukerrepresentant).De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter:• Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterendeplattform.• Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser. Prosjektetnærmer seg en viktig milepæl: første prototype skal være klar om tre uker. Stemningen erspent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan avgjøre omteamet beveger seg videre mot “norming” – eller blir stående fast i stormen.'
valgListe = ['\nA) Kjøre en avstemning i teamet og gå for et kompromiss', '\nB) Unngå konflikten, og la Hamdi og Jabir finne ut av det selv', '\nC) Analyser saken selv, og ta en sjefsvgjørelse']

valg = PoengFraValg(problem, valgListe)

if valg == 'a':
    poeng = poeng + 10
elif valg == 'b':
    #Om brukeren ikke svarer A), sjekkes det om den svarer B) i stedet. C) trengs ikke sjekkes, fordi det er lik 0 poeng.
    poeng = poeng + 5

print ('\nTakk! Her er siste problemstilling:')

#Situasjon 3:

problem = '\n\nHvordan ønsker du å bevare motivasjonen i teamet som helhet?'
valgListe = ['\nA) Invitere hele teamet på restaurant på prosjektets regning, for å bygge samhold i teamet', '\nB) Avvikle 1 ukes ferie for hele teamet', '\nC) Fokusere 100% på effektivitet, og kun få teamet til å jobbe med arbeidet']

valg = PoengFraValg(problem, valgListe)

if valg == 'a':
    poeng = poeng + 10
elif valg == 'b':
    poeng = poeng + 5


print ('\n\nHer er resultatene:')

#Resultatene preenteres basert på brukerens poengsum. Poengsummen kan være 10 eller mindre, mellom 11 og 20, og 21 eller mer.

if poeng < 11:
    print ('\nKonfliktene løses ikke, resultatet blir svekket og gruppa får ikke gjort det de skal til rett tid. Stilling din blir satt under press av kommunestyret.')

elif poeng > 10 and poeng < 21:
    print ('\nDet gjenstår noe dårlig stemning, men produktiviteten er tilstrekkelig til å fortsette med prosjektsamarbeidet')
else:
    print ('\nKonfliktene blir løst og gruppa jobber godt sammen! Produktiviteten er veldig god.')
    
    




