import itertools

def sprawdz_zgodnosc(regula, przyklady):
    zgodne_przyklady = []
    for przyklad in przyklady:
        if all(przyklad[cecha] == wartosc for cecha, wartosc in regula):
            zgodne_przyklady.append(przyklad)
    return zgodne_przyklady

def znajdz_reguly(przyklady, max_dlugosc_reguly):
    liczba_cech = len(przyklady[0]) - 1
    niewykorzystane_przyklady = przyklady.copy()
    reguly = []

    for dlugosc_reguly in range(1, max_dlugosc_reguly + 1):
        if not niewykorzystane_przyklady:
            break

        najlepsza_regula = None
        najlepsze_zgodne_przyklady = []

    for regula in itertools.combinations(enumerate(range(liczba_cech)), dlugosc_reguly):
        zgodne_przyklady = sprawdz_zgodnosc(regula, niewykorzystane_przyklady)
        if len(zgodne_przyklady) > len(najlepsze_zgodne_przyklady):
            najlepsza_regula = regula
            najlepsze_zgodne_przyklady = zgodne_przyklady

    if najlepsza_regula:
        reguly.append(najlepsza_regula)
        for przyklad in najlepsze_zgodne_przyklady:
            niewykorzystane_przyklady.remove(przyklad)

    return reguly

system_decyzyjny = [
[1, 1, 1, 1, 3, 1, 1],
[1, 1, 1, 1, 3, 2, 1],
[1, 1, 1, 3, 2, 1, 0],
[1, 1, 1, 3, 3, 2, 1],
[1, 1, 2, 1, 2, 1, 0],
[1, 1, 2, 1, 2, 2, 1],
[1, 1, 2, 2, 3, 1, 0],
[1, 1, 2, 2, 4, 1, 1]
]

max_dlugosc_reguly = 2
reguly = znajdz_reguly(system_decyzyjny, max_dlugosc_reguly)

print("Znalezione reguły:")
for regula in reguly:
    print("i".join(f"a{cecha + 1} = {wartosc}" for cecha, wartosc in regula))

def znajdz_reguly_bez_usuwania(przyklady, max_dlugosc_reguly):
    liczba_cech = len(przyklady[0]) - 1
    reguly = []

    for dlugosc_reguly in range(1, max_dlugosc_reguly + 1):
        najlepsza_regula = None
        najlepsze_spojne_przyklady = []

    for regula in itertools.combinations(enumerate(range(liczba_cech)), dlugosc_reguly):
        spojne_przyklady = sprawdz_zgodnosc(regula, przyklady)
        if len(spojne_przyklady) > len(najlepsze_spojne_przyklady):
            najlepsza_regula = regula
            najlepsze_spojne_przyklady = spojne_przyklady

    if najlepsza_regula:
        reguly.append(najlepsza_regula)

    return reguly

reguly = znajdz_reguly(system_decyzyjny, max_dlugosc_reguly)

print("Znalezione reguły:")
for regula in reguly:
    print("i".join(f"a{cecha + 1} = {wartosc}" for cecha, wartosc in regula))