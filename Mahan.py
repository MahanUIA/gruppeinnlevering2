poeng = 0

def presentereProblemOgValg(problemStilling,valgMuligheter):
    global poeng
    print(problemStilling)
    print("Hvilket valg tar du?")
    for index, valg in enumerate(valgMuligheter):
        print(str(index + 1) + valg[0])
    while True:
        try:
            brukerValg = int(input("Velg et alternativ"))
            if brukerValg > 0 and brukerValg <= len(valgMuligheter):
                break
            else:
                print("Feil valg, prøv igjen")
        except ValueError:
            print("Ugyldig verdi")
    valget = valgMuligheter[brukerValg-1]
    print(valget)
    poeng += valget[1]
    print(poeng)

problem1 = {}

presentereProblemOgValg("hei",[("hey",1),("hey2",2),("hey3",4)])