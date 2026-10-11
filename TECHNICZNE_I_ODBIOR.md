# Wdrożenie Fabric 1.21.4
Minecraft Java 1.21.4, JDK 21, namespace wieza, Fabric. Pakiet danych format 61, zasobów 46. Zgodne wersje Loader/Loom/Yarn/Fabric API przypnij po sprawdzeniu oficjalnych metadanych 1.21.4; nie używaj bieżących API z 1.21.11 lub 26.x.

Źródła wersji: https://fabricmc.net/2024/12/02/1214.html ; https://github.com/FabricMC/fabric-docs/blob/main/versions/1.21.4/develop/getting-started/setting-up-a-development-environment.md ; https://www.minecraft.net/fr-fr/article/minecraft-java-edition-1-21-4

## Modele
Pięć .bbmodel jako źródła Blockbench Bedrock, pięć geometrii .geo.json i pięć plików .animation.json w standardzie Bedrock/Molang. Każdy ma kości części i osadzoną teksturę 128×128. Idle/walk są bazowymi zapisami animacji, nie gotową choreografią scen. Minecraft Java nie czyta ich natywnie: potrzebny renderer Fabric albo zgodna z 1.21.4 wersja biblioteki animacji + konwersja w razie różnic schematu. Nie dołączono bibliotek, JAR moda ani gotowych kontrolerów. Animacje specjalne (stempel, pływanie, scena, szarża, uwolnienie) trzeba wykonać i sprawdzić w edytorze.
Rendery pokazują rzeczywistą geometrię, koncepcje AI mają kierunek wizualny i mogą różnić się drobnymi detalami. Geometria jest źródłem prawdy przy eksporcie. Podczas wdrożenia sprawdź pivots, UV, hierarchię i animację każdego modelu w Blockbench. Ręce i nogi są oddzielnymi kośćmi, nie sklejaj wszystkich części do jednego mesh.

## Zapis i multiplayer
CampaignState per instancja: schemaVersion=1, stage enum, solvedScenes set, evidence set, committedOutcome, unlockedFloors, idaFreed, ending enum/null. Zapis przy checkpoint i autosave. PlayerState: journalPagesSeen, accessibility, hintLevel. Jedna drużyna 1–4 osoby na kampanię, dołączenie w trakcie synchronizuje etap i przestrzeń. Sceny manipulują stanem instancji, nie zwykłym Overworld. Echo jest jedną autorytatywną encją serwera z nagranym ruchem; klient nie wysyła gotowego rozwiązania.
Interakcja C2S zawiera id interakcji i intencję; serwer sprawdza etap, wymiar, dystans <=6, cooldown i dostępność przedmiotu-stanu. Packety zmian świata mają rewizję; klient ignoruje stare. Dialogi nie są wymagane; napisy opisowe przy obiektach nie blokują ruchu. Kampania nie powinna zależeć od realnej daty systemu, użyj stałego kalendarza fabularnego.

## Przywracanie prób
Każda scena ma initial, running, solved; reset przywraca lokalne obiekty i checkpoint, nie kasuje dowodów. Restart w trakcie próby ładuje initial tego etapu. Rozłączenie właściciela echa resetuje próbę po bezpiecznej synchronizacji. Śmierć oddaje wszystkie reprezentacje dowodów. Dodatkowy dziennik /wieza journal. Debug /wieza reset_scene wymaga OP. Budowa /wieza start generuje nową instancję bez nadpisywania bazy gracza. NBT w dołączonym datapacku jest demonstracją w osobnym pustym świecie, nie implementacją tego systemu.

## Audio i UI
Brak nagrań audio w paczce. Brief: stempel suchy trzask, pociąg cichy metal, Ocean odgłos kropli i rezonans szkła, Teatr skrzypiące deski bez głośnych scare, Ogród wiatr i ptaki, Serce niski rytm zegara. Odtwarzanie napisów dźwięków; jasność ostrzeżenia bez stroboskopu. Dostępność: echo bez limitu czasu, tryb spokojny, napisy dużą czcionką, ograniczone cząstki, żadnych zagadek opartych wyłącznie na słuchu.

## Kryteria odbioru gotowego moda
1. Gradle build z JDK21, faktyczny JAR, uruchomienie klienta 1.21.4 i dedykowanego serwera.
2. Kompletna trasa od paczki po trzy osobne zakończenia; wszystkie poszlaki obecne przed zagadką.
3. Dwie osoby w każdej scenie, wejście późnego gracza, rozłączenie przy odbiciu/echu/finale.
4. Śmierć z dowodem, restart w każdym rozdziale, reset zagadki, brak duplikacji i utraty stanu.
5. Wszystkie modele bez błędów UV, proporcji i pivots; animacje bez przenikania w typowych pozycjach.
6. Każda mapa ma trzyblokową trasę, sprawne schody, lampy i nieprzerwany powrót do windy.
7. Bez shaderów, tryb spokojny, bardzo wolne rozwiązywanie zagadek, powiększone napisy.

W paczce wykonano walidację plików, nie uruchomiono Minecrafta ani Blockbench. Nie twierdź, że kompletne mechaniki działają: to projekt i zasoby do produkcji.
