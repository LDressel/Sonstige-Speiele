# Sprachdateien erzeugen

Die Stimme wird komplett offline erzeugt: Piper (Sprachmodell „thorsten-medium“) spricht den Text,
danach rechnet `stimme_b.py` daraus eine freundliche Frauenstimme („Stimme B“). Tierstimmen sind dieselbe
Stimme, nur höher oder tiefer (`hoehe` in der `texte.json`).

## Einmalig einrichten
```
pip install piper-tts pyworld soundfile numpy
# ffmpeg muss installiert sein
mkdir -p werkzeuge/sprache/modell && cd werkzeuge/sprache/modell
curl -LO https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-de_DE-thorsten-medium.tar.bz2
tar xjf vits-piper-de_DE-thorsten-medium.tar.bz2 --strip-components=1
```

## Erzeugen
Im Hauptordner des Repos:
```
python3 werkzeuge/sprache/erzeuge.py tierarzt
```
Es werden nur Sätze neu gemacht, deren Text sich geändert hat. Fertige Dateien landen in `tierarzt/ton/`,
dazu `liste.json` (für die Offline-Speicherung). Danach in `tierarzt/sw.js` die Zahl bei `CACHE` erhöhen,
damit das iPad die neuen Dateien holt.

## Aussprache
Wörter, die falsch ausgesprochen werden, in `erzeuge.py` bei `AUSSPRACHE` eintragen
(z. B. wird „Belle“ als „Bell“ gesprochen).

## Hinweis zu Piper 1.8
Liegt das Werkzeug in einem sehr langen Ordnerpfad, findet Piper seine Sprachdaten nicht („phontab: No such file“).
Dann das Werkzeug in einen kurzen Ordner legen oder in `piper/phonemize_espeak.py` `ESPEAK_DATA_DIR` auf einen kurzen Verweis setzen.
