"""Macht aus einer Männerstimme eine Frauenstimme (WORLD-Vocoder).
Aufruf: python3 female.py in.wav out.wav [f0_faktor] [formant_faktor] [melodie]
f0_faktor: Tonhöhe (1.7 = deutlich höher)
formant_faktor: Klangfarbe/Stimmtrakt (1.15 = kürzerer Stimmtrakt, weiblicher)
melodie: verstärkt die Satzmelodie (1.0 = unverändert, 1.3 = lebendiger)
"""
import sys
import numpy as np
import soundfile as sf
import pyworld as pw


def convert(x, fs, f0k=1.7, fk=1.15, mel=1.25):
    x = x.astype(np.float64)
    f0, t = pw.harvest(x, fs, f0_floor=60, f0_ceil=400, frame_period=5.0)
    sp = pw.cheaptrick(x, f0, t, fs)
    ap = pw.d4c(x, f0, t, fs)
    # Tonhöhe anheben und Satzmelodie (um den Mittelwert) etwas verstärken
    v = f0 > 0
    if v.any():
        lf = np.log(f0[v])
        m = lf.mean()
        f0[v] = np.exp(m + (lf - m) * mel) * f0k
    # Formanten verschieben: Spektrum entlang der Frequenzachse strecken
    n = sp.shape[1]
    src = np.arange(n) / fk
    sp2 = np.empty_like(sp)
    for i in range(sp.shape[0]):
        sp2[i] = np.interp(src, np.arange(n), sp[i])
    ap2 = np.empty_like(ap)
    for i in range(ap.shape[0]):
        ap2[i] = np.interp(src, np.arange(n), ap[i])
    y = pw.synthesize(f0, np.ascontiguousarray(sp2), np.ascontiguousarray(ap2), fs, 5.0)
    y = y / (np.abs(y).max() + 1e-9) * 0.9
    return y


if __name__ == '__main__':
    inp, out = sys.argv[1:3]
    f0k = float(sys.argv[3]) if len(sys.argv) > 3 else 1.7
    fk = float(sys.argv[4]) if len(sys.argv) > 4 else 1.15
    mel = float(sys.argv[5]) if len(sys.argv) > 5 else 1.25
    x, fs = sf.read(inp)
    sf.write(out, convert(x, fs, f0k, fk, mel), fs)
