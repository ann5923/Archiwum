# Sceny interaktywne — dokładny kontrakt
## Zasada
Zagadki to działania w świecie i sprawdzanie hipotez. Nie ma zamków z arbitralnymi kodami, sekwencji kolorowych dźwigni ani „znajdź trzy klucze”. Wszystkie rozwiązania mają wizualną poszlakę przed wymaganym działaniem. Czasówki resetują tylko scenę, nigdy kampanię. Po trzech błędach gracz może włączyć pełną wskazówkę.

## P1 — Kontrola, której jeszcze nie było
Stan początkowy: bilet w dłoni, kontroler przy drzwiach, cień na przeciwległej ścianie, odbicie zegara wskazuje drugi wagon. Zwykły kontroler stempluje bilet datą dzisiejszą, a zamknięte drzwi pokazują jutro. Gracz ogląda oba stemple, odkrywa przesunięcie i używa biletu przy cieniu (światło regulowane suwakowym kołem, nie kodem). Cień stempluje jutro. Przeniesienie mokrego bagażu do wagonu z oceanem odblokowuje właściwą podróż. Dostępne alternatywne wagony dają krótkie zapowiedzi, a wracają na peron. Nie są trwałym złym wyborem.
Rozwiązanie: odkryj dwa stemple → ustaw lampę tak, aby cień sięgał drzwi wagonu → oddaj bilet cieniowi → przenieś bagaż do oceanicznego wagonu → wejdź. Lampa ma dwie czytelne skrajne pozycje i podgląd cienia.
Wskazówki: 1 „Kto stempluje bilet w innej dacie?” 2 pokaż odbicie. 3 wyróżnij cień i docelowe drzwi.

## P2 — Ruch w odbiciu
Dwie wersje tej samej sali, geografia 1:1. Warstwa A: woda w basenie, zablokowane koło. B: woda w suficie, żyrandol na wózku. Przejście przez zaznaczoną taflę odbicia przenosi gracza na bezpieczny odpowiednik. Przesuń żyrandol po szynie w B, dojedź nim nad ciężar w A, wróć i przypnij linę. Lampy wokół koła zapalają się, pokazując odciążenie. Obróć dostępne koło i przejdź podniesioną suchą galerią.
Rozwiązanie jest przestrzenne, nie liczbowe: gracz widzi linię szyny i odpowiednik celu w obu warstwach. Po pierwszym przejściu do B zatrzymuje się ściek wody, aby dać czas na orientację. Sekwencja później trwa 40 sekund; opcja dostępności usuwa limit. Błąd cofa do tafli, przywraca pozycję żyrandola, bez utraty HP.
Opcjonalna ścieżka: doprowadź Nurka do pękniętego przewodu przez zapalone lampy; dostaniesz suchą drogę awaryjną i widok rachunku bez nurkowania.

## P3 — Próba, której nie da się zagrać
Scena ma punkty: bezpiecznik, gaśnica, drzwi frontowe, wyjście kulis, projektor. Gracz ogląda krótki spektakl (20 s), cofa go i przestawia maksymalnie dwa rekwizyty. Żadna próba nie robi trwałego pożaru mapy. Uratowany manekin może wyjść przez dowolne narysowane drzwi. Prawdziwy plan warsztatu pokazuje brak wyjścia po stronie kulis. Wyprowadź go właśnie tam, aby ujawnić projekcję. Podświetlony kabel prowadzi od figury do projektora. Wyłącz projektor, zabierz oryginalny rachunek.
Nie wymagaj pięciu prób: plan i ślady ruchu dostępne od wejścia. Test bezpiecznika to opcjonalna demonstracja. Wersja kooperacyjna pozwala jednej osobie sterować próbą, drugiej chodzić za sceną; wszyscy widzą ten sam wynik.

## P4 — Zostaw sobie pomoc
Po pokazaniu własnego grobu gracz dostaje możliwość zapisu echa na 10 sekund. Stacje A/B/C w ogrodzie: A trzyma wrota, B to punkt odbioru lampy, C to winda, którą otwiera światło lampy. Próba 1: nagraj stanie przy A przez 10 sekund. Uruchom echo; gdy trzyma A, wejdź do kaplicy przez B, weź lampę i ujawnij oryginał zabezpieczenia. Dokument jest zapisany trwale po obejrzeniu, więc reset próby go nie zabiera. Próba 2: postaw lampę przy C, co włącza windę. Nagraj drogę od B do C (do 10 sekund), zresetuj wyłącznie pozycję próbnego echa, uruchom je i sam stań przy A. Echo przejdzie przez otwarte wrota do oświetlonej windy. Wyjście echa przez C usuwa grożącą mu wersję przyszłości i kończy scenę. Nie trzeba być równocześnie w trzech miejscach; układ galerii pozwala dojść od konsoli nagrywania do A w 2 sekundy, a echo ma 3-sekundowe opóźnienie startu.
Ważne: tutorial najpierw pokazuje prosty zapis stania na jednej stacji, potem pozwala dowolnie nagrywać. Echo fizycznie otwiera mechanizmy, nie powoduje obrażeń, nie kopiuje ekwipunku ani przedmiotów. Minimalna ścieżka zapisuje pozycje co tick przez 200 ticków (20 Hz), interpolacja wizualna klienta. Po załadowaniu świata aktywna próba resetuje się do checkpointu, ukończenie zostaje.
Przejście wymaga dwóch oddzielnych prób, lecz nie wymaga refleksu; w trybie spokojnym echo czeka na sygnał. Nieudana próba cofa zabezpieczenie na piedestał. Brak miękkiej blokady i możliwości duplikacji.

## P5 — Proces zamiast paska życia
Anioł ma trzy czytelne zachowania: patrol, szarża po zapowiedzianym pasie, odcięcie ostatnio użytego mostu. Przed szarżą 2 sekundy światła i dźwięku + napis. Działa bez shaderów. Bezpieczne nisze co 8 bloków. Każde koło ma fizyczny zamek na konkretny dowód. Użycie dowodu nie usuwa go z trwałego rejestru.
Koło 1 zatrzymuje sprzeczny bilet: przejdź echo-mostem, umieść bilet podczas kontroli cienia. Koło 2 zatrzymuje rachunek rekonstrukcji: przyciągnij Anioła do fałszywego obrazu, przejdź kulisami. Koło 3 zatrzymuje zabezpieczenie: nagraj echo trzymające mechanizm, sam wyjmij zabezpieczenie. W każdej fazie widoczna nowa droga do Idy. Miecz ogłusza na 2 s z cooldown 8 s, nie zabija bossa. Po trzech kołach Anioł opuszcza skrzydła i przestaje atakować.
W trybie spokojnym kontakt cofa do niszy bez obrażeń, szarże zastępują się powolnym patrolem. Czas finału bez limitu. W finale „Powrót” znikanie pięter zaczyna się dopiero po wejściu gracza na następną sekcję, więc nie jest bezlitosnym parkourem.

## Dowody i niezbędne pomoce
Bilet (P1), szalik (marker), bagaz Idy (P1), rachunek (P3), zabezpieczenie (P4), kontrakt (P5). Są zapisem stanu, nie zwykłym przedmiotem do zgubienia. Można pokazać ich kopię w dzienniku, a usunięcie reprezentacji z ekwipunku nie usuwa progresu. Trzy oryginalne dowody są osiągalne przed finałem i wracając windą z P5. Dziennik pokazuje brakujące dowody wprost po ujawnieniu reguł kontraktu.
