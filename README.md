# Sonstige-Speiele

Eine Spiele-Sammlung fürs Tablet. Die Startseite zeigt alle Spiele als große Kacheln:
`https://ldressel.github.io/Sonstige-Speiele/`

Auf dem iPad: Startseite in Safari öffnen → Teilen → „Zum Home-Bildschirm“. Dann gibt es ein Symbol „Spiele“,
über das man alle Spiele erreicht. In Flecki führt der bunte Knopf oben links auf dem Titelbild zurück zur Übersicht.

### Neues Spiel hinzufügen
1. Neuen Ordner anlegen (z. B. `zahlenzug/`) mit einer `index.html` und einem quadratischen Bild (z. B. `icon-512.png`)
2. In der `index.html` im Hauptordner oben in der Liste `GAMES` eine Zeile ergänzen:
   `{ ordner: 'zahlenzug', titel: 'Zahlenzug', text: 'Kurze Beschreibung', bild: 'icon-512.png' },`

## Fleckis Herbstabenteuer (`flecki/`)

Ein Tablet-Spiel für Kinder ab ca. 5 Jahren. Die Geschichte hat sich meine Tochter ausgedacht:
Die schwarz-weiße Babykatze **Flecki** schleicht sich im Herbst aus dem Haus, sammelt in der
Nachbarschaft Schlüssel und bringt am Abend alles wieder zurück.

**Spielen:** `https://ldressel.github.io/Sonstige-Speiele/flecki/` (sobald GitHub Pages aktiv ist)

### Ablauf
1. Vom Kratzbaum runterhüpfen (auf die leuchtende Plattform tippen)
2. Durchs Wohnzimmer schleichen: Nur laufen, wenn die Ampel oben grün ist, sonst wird Flecki entdeckt (und sanft zurückgesetzt)
3. Schlüssel klauen: auf Flecki tippen, dann das baumelnde Band schnappen, Schlüssel ins Schloss ziehen und im Kreis drehen
4. Auf der Stromleitung balancieren: auf die leuchtende Seite tippen
5. Drei Nachbarhäuser: Kürbisse zermatschen, durch den Kamin rein, Schlüssel schnappen, durch den Kamin wieder raus
6. Nach jedem Haus den Weg auf Fleckis Karte mit dem Finger nachmalen
7. Abends auf dem Rückweg den passenden Schlüssel (Farbe und Zeichen) ins richtige Haus bringen, an den Haken hängen,
   die Tür mit der Kralle zusperren (nach unten wischen) und durch den Kamin raus
8. Zuhause zusperren, auf den Kratzbaum klettern, Bad gegen den Ruß, schlafen

### Für Eltern
- Kein Game Over, keine Texte zum Lesen, keine Werbung, keine Daten werden gesendet
- Der Spielstand wird nach jedem Abschnitt gespeichert (Titelbild: „Weiter")
- Das Haus-Symbol oben links pausiert das Spiel
- Auf dem iPad: In Safari öffnen → Teilen → „Zum Home-Bildschirm". Dann startet es wie eine App im Vollbild und läuft auch offline.
- Ton kommt nur, wenn der Stummschalter aus ist

Alles (Grafik und Töne) ist im Code gezeichnet bzw. erzeugt, es gibt keine externen Bilder oder Bibliotheken.

## Die erste Katze im Weltraum: Mitzi (`mitzi/`)

Das zweite Spiel – wieder hat sich meine Tochter die Geschichte ausgedacht:
Ein frecher Alien schnappt sich die Katze **Belle** und wirft sie auf dem Mars in eine Grube.
Die schwarze Katze **Mitzi** (mit weißem Hals) fliegt mit ihrer eigenen Rakete hinterher und rettet sie.

**Spielen:** `https://ldressel.github.io/Sonstige-Speiele/mitzi/`

### Ablauf
1. Zuhause: Das Ufo holt Belle. Auf Mitzi tippen (sie steigt in die Rakete), dann auf den roten Knopf: 3, 2, 1, los!
2. Flug zum Mars: Rakete mit dem Finger schieben (wischen, egal wo auf dem Bildschirm), Meteoriten ausweichen und
   durch fünf Sterne fliegen. Bei einem Treffer wackelt die Rakete und ein Stern fällt raus, den man schnell wieder einfangen muss.
3. Auf dem Mars: Mit dem Finger von Stern zu Stern fahren, so entsteht die Sternenkette.
4. Kampf gegen den Alien: Er guckt hinter den Steinen hervor, dann schnell antippen (3 Treffer).
   Wirft er ein Netz, auf Mitzi tippen, damit sie hochspringt. Ist sie im Netz, schnell oft auf Mitzi tippen.
   Danach den schwindeligen Alien einwickeln (Kreise malen), ins Weltall werfen (nach oben wischen)
   und die Sterne wieder abholen (antippen). Tschüss, Alien!
5. Belle retten: Sternenkette in die Grube ziehen, dann immer wieder nach oben wischen (sonst rutscht Belle zurück).
6. Rückflug: Durch die leeren Sternenplätze im Himmel fliegen, dann bleibt dort ein Stern hängen. Wieder Meteoriten ausweichen.
7. Wieder zu Hause.

### Für Eltern
- Mama erklärt alles mit fertigen Sprachdateien (`mitzi/ton/`, erzeugt aus `mitzi/texte.json`). Der rosa Herz-Knopf oben rechts
  wiederholt die letzte Anweisung, nach längerem Warten wiederholt sie sich auch von selbst.
- Ist der Ton leise, hört man Mama nicht.
- Kein Game Over, keine Werbung, keine Daten werden gesendet. Der Spielstand wird nach jedem Abschnitt gespeichert.

## Belles Tierarztpraxis (`tierarzt/`)

Das dritte Spiel – die Idee kommt wieder von meiner Tochter: Die Katze **Belle** ist Tierärztin.
Jeden Tag kommen kranke Tiere in ihre Praxis, und Belle (also das Kind) findet heraus, was ihnen fehlt.

**Spielen:** `https://ldressel.github.io/Sonstige-Speiele/tierarzt/`

### Ablauf eines Patienten
1. Ein Tier kommt durch die Tür, hüpft auf den Behandlungstisch und erzählt, was ihm wehtut.
2. **Untersuchen:** Ein Gerät aus dem roten Arztkoffer auf das Tier ziehen. Im großen Kreis sieht man, was das Gerät zeigt.
   Jeder Befund landet auf Belles Klemmbrett (rot = da stimmt was nicht, grün = alles gut).
3. **Diagnose:** Aufs Klemmbrett tippen und die richtige Karte auswählen. Falsch geraten ist nicht schlimm – dann noch mal untersuchen.
4. **Behandeln:** Die Hilfsmittel in der richtigen Reihenfolge benutzen (ziehen, reiben, tropfen …).
5. Das Tier ist gesund, bedankt sich und seine Karte kommt ins **Patientenbuch** (Herz-Buch oben rechts).
   Dort erklärt die Stimme jede Krankheit und jedes Gerät kindgerecht.

### Neue Geräte und Krankheiten
| Tag | Neues Gerät | Neue Krankheit | Behandlung |
|---|---|---|---|
| 1 | Lupe, Thermometer | Splitter, Schramme, Fieber | Pinzette + Pflaster · Tupfer + Salbe + Pflaster · Fiebersaft + Waschlappen |
| 2 | Stethoskop | Husten | Hustensaft + Schal |
| 3 | Röntgengerät | Knochenbruch | Gips wickeln + Sticker |
| 4 | Ohrenspiegel | Ohrenentzündung | Ohrentropfen + Watte |
| ab 5 | – | alles gemischt | |

Neue Krankheiten kommen in `tierarzt/index.html` in die Listen `KRANK`, `BEFUND` und `FREI`,
die Sprechtexte in `tierarzt/texte.json` (danach Sprachdateien neu erzeugen, siehe unten).

### Für Eltern
- Die Stimme kommt aus fertigen Sprachdateien (`tierarzt/ton/`), nicht mehr aus der Vorlesestimme des iPads.
  Der Lautsprecher-Knopf oben rechts wiederholt die letzte Anweisung.
- Kein Game Over, keine Werbung, keine Daten werden gesendet. Der Spielstand wird nach jedem Patienten gespeichert.
- Auf dem Titelbild setzt der kleine Pfeil-Knopf oben rechts das Spiel zurück (zweimal tippen).

## Sprachdateien erzeugen (`werkzeuge/sprache/`)

Alle Sprechtexte stehen in der `texte.json` des jeweiligen Spiels. Daraus macht `erzeuge.py` MP3s
mit „Stimme B“ (freundliche Frauenstimme, offline erzeugt). Anleitung: `werkzeuge/sprache/LIESMICH.md`.
