# Wieża, która ukradła jutro — nowa paczka projektowa
Nowy projekt, bez poprzednich dialogów, mobów i fabuły.

Zacznij od 00_OKLADKA.png i 01_HISTORIA/HISTORIA.md. W 03_MAPY każde piętro ma własną ilustrację koncepcyjną i obraz faktycznie zbudowanej struktury. W 02_MODELE każda postać ma edytowalny model, geometrię, teksturę, bazowe animacje, dokładne rendery i osobną koncepcję wyglądu.

**Gotowe:** historia i scenariusz bez rozmów NPC, pięć scen zagadkowych opartych na zmianie zdarzeń, trzy zakończenia, pięć modeli z detalami stroju, maski i mechaniki oraz teksturami 128×128, pięć dekorowanych struktur 47×35×47, zdjęcia koncepcyjne poziomów i postaci, prompt zawierający pełną specyfikację.
**Do wdrożenia:** kod moda Fabric, renderery Java, kontrolery i specjalne animacje, mechaniki scen, pełnowymiarowe mapy, dźwięki, test w grze. Nie jest to gotowy JAR ani kompletny zapis świata. Ilustracje AI nie są screenshotami z Minecrafta i nie pokazują dokładnie zawartości NBT; faktyczne modele i struktury mają własne rendery.

## Oglądanie modeli
Otwórz .bbmodel w Blockbench. Tekstura jest osadzona, dodatkowo dostępna jako PNG. .geo.json i .animation.json są zasobami Bedrock/Molang do integracji przez odpowiedni renderer; nie działają przez samo skopiowanie do Minecraft Java. Idle i walk to bazowe animacje, nie gotowy zestaw zachowań.

## Ustawienie struktur
Utwórz NOWY pusty świat kreatywny 1.21.4. Skopiuj folder 04_DATAPACK/wieza do jego datapacks. Włącz komendy. /reload, /function wieza:build. /tp @s 23 84 7. Piętra stoją obok siebie przy x=0,64,128,192,256, y=80, z=0. Przykład pojedynczej budowy: /place template wieza:03_teatr 0 80 0.
Budowa nadpisuje zajęte bloki w obszarze x=0..302, y=80..114, z=0..46. Używaj pustego świata testowego. Każda struktura ma całą ścianę obwodową, wejście i dwa ciągi schodów. Render ukrywa fragment ściany dla widoku wnętrza. Zagadka nie działa w samym datapacku; to demonstracja map.

## Prompt
05_PROMPT/PROMPT_DO_SKOPIOWANIA.txt jest samodzielnym pełnym zleceniem wdrożenia. Dołącz też cały ZIP, aby programista otrzymał zasoby. 06_ZRODLA zawiera skrypty generujące modele i struktury, umożliwiające dalsze edytowanie.
