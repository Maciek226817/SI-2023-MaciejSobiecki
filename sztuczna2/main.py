import gradio as gr

# Funkcja informacje_o_pliku(nazwa_pliku) odczytuje plik o podanej nazwie
# i zwraca informacje o liczbie linii w pliku oraz liczbę wystąpień poszczególnych klas

def informacje_o_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        linie = plik.readlines()

    liczba_linii = len(linie)
    linie_tekstu = odczytaj_plik_tekstowy(nazwa_pliku)

    informacja = f"Plik zawiera {liczba_linii} wierszy."
    klasy = {}

    for linia in linie_tekstu:
        nazwa_klasy = linia.split()[0]
        if nazwa_klasy not in klasy:
            klasy[nazwa_klasy] = 0
        klasy[nazwa_klasy] += 1

    return klasy, informacja

# Funkcja odczytaj_plik_tekstowy odczytuje zawartość pliku tekstowego
# o podanej nazwie nazwa_pliku. Następnie usuwa białe znaki na początku
# i końcu każdej linii, a także usuwa puste linie. Ostatecznie zwraca listę linii tekstu.

def odczytaj_plik_tekstowy(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        linie = plik.readlines()
    linie_tekstu = [linia.strip() for linia in linie if linia.strip()]
    return linie_tekstu

# Ta funkcja służy do wyświetlania informacji
# o pliku tekstowym oraz wybranych przez użytkownika wierszach tego pliku.

def wyswietl_plik(nazwa_pliku, liczba_wierszy):
    klasy, info = informacje_o_pliku(nazwa_pliku)
    odpowiedz = "Liczba klas decyzyjnych to: {}\n".format(len(klasy))
    for nazwa_klasy, rozmiar_klasy in klasy.items():
        odpowiedz += "Rozmiar klasy {} to: {}\n".format(nazwa_klasy, rozmiar_klasy)

    wiersze = odczytaj_plik_tekstowy(nazwa_pliku)
    liczba_wierszy = int(liczba_wierszy)
    wyswietlone_wiersze = "\n".join(wiersze[:liczba_wierszy])
    return f"{info}\n{odpowiedz}\nWybrane wiersze:\n{wyswietlone_wiersze}"



nazwa_pliku = gr.inputs.Textbox(label="Podaj nazwę pliku:" )
liczba_wierszy = gr.inputs.Number(label="Wybierz liczbę wierszy do wyświetlenia:", default=1)
output_tekst = gr.outputs.Textbox(label="Wynik:")

instrukcje_instrukcja = "Wprowadź instrukcje, które chcesz wykonać na danych."
wybierz_plik_instrukcja = "Wprowadź nazwę pliku, który chcesz wyświetlić."
liczba_wierszy_instrukcja = "Wybierz liczbę wierszy, które chcesz wyświetlić z pliku. Możesz wprowadzić liczbę bezpośrednio lub użyć suwaka, aby wybrać wartość z listy."
wybierz_klasy_instrukcja = "Wybierz klasy, które chcesz wyświetlić z pliku."
wykonaj_instrukcja = "Kliknij przycisk 'Zatwierdz', aby uruchomić aplikację i wyświetlić wynik. Wynik zostanie wyświetlony na stronie interfejsu."



iface = gr.Interface(fn=wyswietl_plik, inputs=[nazwa_pliku, liczba_wierszy], outputs=output_tekst, title="CHAT BOT Sztuczna inteligencja LAB 2",
                     description="{}\n\n{}\n\n{}\n\n{}\n\n{}".format(wybierz_plik_instrukcja,instrukcje_instrukcja,liczba_wierszy_instrukcja,wybierz_klasy_instrukcja,wykonaj_instrukcja))
iface.font_color = "red"
iface.background_color = "#0072C6"
iface.theme = "light"
iface.launch()