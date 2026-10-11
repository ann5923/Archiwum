# Pięć pięter jednej wieży
## Wspólna architektura
Wieża na klifie, zewnętrzna średnica 96 bloków, wysokość docelowa 240. Wewnątrz piętra są szersze niż zewnętrzna bryła; ładowane jako osobne przestrzenie instancji. Hub: wejście, winda i kopia dziennika. Do każdego ukończonego piętra można wrócić. Główna ścieżka ma szerokość >=3 bloki, brak obowiązkowego parkouru. Architektura jest nienaruszona: sklepienia, filary z bazami i głowicami, powtarzalne detale, ramy okienne, balustrady. Ślady wydarzeń są celowe i lokalne.

W ZIP-ie dla każdego poziomu jest ilustracja koncepcyjna oraz osobny render faktycznej struktury NBT. Ilustracja przedstawia DOCZELOWY poziom szczegółowości. NBT jest mniejszym, dekorowanym modułem 47×35×47, zgodnym z limitem struktury 48 bloków, do dalszej rozbudowy. To nie screenshot gry. Przekrój renderu ukrywa przednią ścianę, ale NBT zawiera całą obwodową ścianę i wejście.

## 01 Peron
Docelowo 96×96×40. Dwa pociągi, zegar nad peronem, wyjście przez wagon, galeria wokół. Komory wagonów pokazują trzy przyszłości. Kolory: granat, bordo, mosiądz. Oś widokowa od wejścia do zegara. Ślady Idy: walizka, szalik. Moduł NBT zawiera jeden wagon z oknami i wejściem, tory, filary, zegar, bagaże i dwie schodowe drogi na galerię.
## 02 Ocean
Docelowo 96×96×48, dodatkowa identyczna warstwa odbicia. Podwójna sala, suche galerie, akwarium pod szklanym pomostem, żyrandol i stacja Nurka. Kolory: błękit, kość słoniowa, srebro. Nigdy nie trzeba płynąć bez tlenu do celu fabularnego. NBT ma basen, szkło, podest, pomost i żyrandol; ruch i alternatywną grawitację realizuje mod, nie NBT.
## 03 Teatr
Docelowo 96×80×40, widownia z miejscami, kulisy po obu stronach, scena z budynkiem warsztatu. Kolory: bordo, złoto, papier. Cały mechanizm kulis widoczny po udowodnieniu fałszu. NBT ma scenę, rzędy foteli, domek, manekiny i czerwony księżyc. Projector i próby do wykonania w kodzie.
## 04 Ogród
Docelowo 96×96×48, dwa równoległe stany przestrzeni. Cztery uporządkowane wyspy kwiatowe, białe kaplice, kanały, tabliczki, dwa łuki. Kolory: lawenda, róż, kość słoniowa, ciepłe złoto. Groby są eleganckimi oznaczeniami futures, bez makabry. NBT ma cztery uformowane drzewa, kanały, ścieżki, pomniki i łuk; nie jest losowo zniszczonym lasem.
## 05 Serce
Docelowo 112×112×64, pionowy mechanizm, trzy radialne drogi, bezpieczne nisze i balkon Idy. Kolory: fiolet, złoto, czerń. Koła wielkości budynków przesuwają się z wyraźnym zapowiedzeniem; obrażenia nie resetują całej fazy. NBT ma trzy miedziane pierścienie, świecący rdzeń, podłogę areny i trzy kotwice. Animowane koła najlepiej zrealizować jako encje/renderer; nie przestawiać tysięcy bloków co tick.

## Oświetlenie i wykończenie
Zewnętrzny chłód, wnętrza ciepłe, co najmniej jeden rozpoznawalny obiekt z wejścia. Nie przesadzaj z mgłą; cel zagadki musi być czytelny. Podświetlane krawędzie interakcji + podpis + symbol, nie tylko kolor. Bez obowiązkowych shaderów. Lampy vanilla wspierają podstawowy wygląd. Nie kopiuj ilustracji 1:1 jako obietnicy, że shader jest częścią moda.
