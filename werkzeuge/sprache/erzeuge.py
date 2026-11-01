"""Erzeugt die Sprachdateien (MP3) für ein Spiel aus seiner texte.json.

Aufruf (im Hauptordner des Repos):
    python3 werkzeuge/sprache/erzeuge.py tierarzt

Es werden nur Sätze neu erzeugt, deren Text sich geändert hat (Merkliste: ton/.stand.json).
Stimme: Piper "thorsten-medium", umgerechnet zu einer freundlichen Frauenstimme ("Stimme B").
"""
import sys, os, re, json, hashlib, subprocess, tempfile
import soundfile as sf

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from stimme_b import convert  # noqa: E402

MODELL = os.environ.get('PIPER_MODELL', os.path.join(HIER, 'modell', 'de_DE-thorsten-medium.onnx'))

# So geschrieben, wie es gesprochen werden soll
AUSSPRACHE = [(r'\bBelles\b', 'Bells'), (r'\bBelle\b', 'Bell')]


def aussprache(text):
    for a, b in AUSSPRACHE:
        text = re.sub(a, b, text)
    return text


def sprich(text, ziel, hoehe=1.0, tempo=1.0):
    with tempfile.TemporaryDirectory() as td:
        roh, frau = f'{td}/roh.wav', f'{td}/frau.wav'
        subprocess.run([sys.executable, '-m', 'piper', '-m', MODELL,
                        '--length-scale', f'{1.05 * tempo:.3f}', '--sentence-silence', '0.35', '-f', roh],
                       input=aussprache(text).encode(), check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        x, fs = sf.read(roh)
        f0 = 1.6 * hoehe
        formant = 1.12 * min(hoehe, 1.2) ** 0.5
        sf.write(frau, convert(x, fs, f0, formant, 1.35), fs)
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', frau, '-af',
                        'highpass=f=90,loudnorm=I=-16:TP=-1.5,afade=t=in:d=0.02', '-ar', '24000', '-ac', '1',
                        '-b:a', '48k', ziel], check=True)


def liste(texte):
    """Alle Dateien: Name -> (Text, Höhe, Tempo)"""
    out = {}
    for k, t in texte.get('erzaehler', {}).items():
        out[k] = (t, 1.0, 1.0)
    for tier, d in texte.get('tiere', {}).items():
        if 'kommt' in d:
            out[f'kommt_{tier}'] = (d['kommt'], 1.0, 1.0)
        for k, t in texte.get('tiersaetze', {}).items():
            out[f'{tier}_{k}'] = (t, d.get('hoehe', 1.0), d.get('tempo', 1.0))
    return out


def main(spiel):
    ordner = os.path.join(os.getcwd(), spiel)
    texte = json.load(open(os.path.join(ordner, 'texte.json'), encoding='utf-8'))
    ton = os.path.join(ordner, 'ton'); os.makedirs(ton, exist_ok=True)
    standdatei = os.path.join(ton, '.stand.json')
    stand = json.load(open(standdatei)) if os.path.exists(standdatei) else {}
    alle = liste(texte)
    for name, (text, h, tp) in alle.items():
        key = hashlib.md5(f'{text}|{h}|{tp}|v1'.encode()).hexdigest()
        ziel = os.path.join(ton, name + '.mp3')
        if stand.get(name) == key and os.path.exists(ziel):
            continue
        sprich(text, ziel, h, tp)
        stand[name] = key
        print('✓', name, flush=True)
    for f in os.listdir(ton):  # alte Dateien entfernen
        if f.endswith('.mp3') and f[:-4] not in alle:
            os.remove(os.path.join(ton, f)); stand.pop(f[:-4], None)
    json.dump(stand, open(standdatei, 'w'), indent=0, sort_keys=True)
    json.dump(sorted(alle), open(os.path.join(ton, 'liste.json'), 'w'))
    print(len(alle), 'Sprachdateien')


if __name__ == '__main__':
    main(sys.argv[1])
