"""Compone la mappa satellitare dello Stretto per la pagina Why STRATUS.

Scarica le tessere del mosaico Sentinel-2 cloudless di EOX (CC BY 4.0), le
cuce, ritaglia il riquadro che contiene tutto il comune di Messina e scrive
images/lupa/stretto-satellite.jpg.

Si rilancia solo per cambiare inquadratura o annata del mosaico:
    python3 .github/scripts/stretto_satellite.py 2024

Stampa anche la posizione in percentuale dei punti noti: sono quelle che
why-stratus.md usa per piazzare il segnaposto sopra l'immagine.
"""
import math, io, os, sys, time, urllib.request
from PIL import Image

# Le tessere scaricate restano accanto allo script, cosi` rilanciarlo non
# ribussa a EOX novanta volte. La cartella e` fuori dal repository.
QUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(QUI, "tessere")

ANNO = sys.argv[1] if len(sys.argv) > 1 else "2024"
Z = 13
# Messina per tutta l'estensione del comune, da Capo Peloro a Giampilieri,
# piu` la sponda calabra che chiude lo Stretto.
LAT_N, LAT_S = 38.300, 37.985
LON_O, LON_E = 15.400, 15.760

def xy(lat, lon, z):
    n = 2 ** z
    x = (lon + 180.0) / 360.0 * n
    r = math.radians(lat)
    y = (1.0 - math.asinh(math.tan(r)) / math.pi) / 2.0 * n
    return x, y

x0f, y0f = xy(LAT_N, LON_O, Z)
x1f, y1f = xy(LAT_S, LON_E, Z)
x0, y0, x1, y1 = int(x0f), int(y0f), int(x1f), int(y1f)
os.makedirs(CACHE, exist_ok=True)
print(f"tessere {x1-x0+1} x {y1-y0+1} = {(x1-x0+1)*(y1-y0+1)}")

tela = Image.new("RGB", ((x1-x0+1)*256, (y1-y0+1)*256))
for ty in range(y0, y1+1):
    for tx in range(x0, x1+1):
        cache = os.path.join(CACHE, f"{ANNO}-{Z}-{ty}-{tx}.jpg")
        if not os.path.exists(cache):
            u = f"https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-{ANNO}_3857/default/g/{Z}/{ty}/{tx}.jpg"
            req = urllib.request.Request(u, headers={"User-Agent": "stratus-lab-site/1.0"})
            for tentativo in range(5):
                try:
                    with urllib.request.urlopen(req, timeout=60) as r:
                        dati = r.read()
                    break
                except Exception as e:
                    if tentativo == 4: raise
                    time.sleep(2 * (tentativo + 1))
            open(cache, "wb").write(dati)
            time.sleep(0.15)
        tela.paste(Image.open(cache), ((tx-x0)*256, (ty-y0)*256))
    print("  riga", ty-y0+1, "di", y1-y0+1)

ritaglio = (round((x0f-x0)*256), round((y0f-y0)*256), round((x1f-x0)*256), round((y1f-y0)*256))
img = tela.crop(ritaglio)
print("ritagliata:", img.size)
img.thumbnail((1100, 4000), Image.LANCZOS)
uscita = os.path.join(QUI, "..", "..", "images", "lupa", "stretto-satellite.jpg")
img.save(uscita, quality=82, optimize=True, progressive=True)
print("scritta:", uscita, img.size)


# Dove cadono i punti noti, in percentuale sull'immagine: servono al segnaposto
# che why-stratus.md mette sopra la foto.
PUNTI = {"Dipartimento di Ingegneria": (38.2595, 15.5956),
         "Capo Peloro": (38.2665, 15.6525),
         "porto di Messina": (38.1930, 15.5660)}
print()
for nome, (la, lo) in PUNTI.items():
    px, py = xy(la, lo, Z)
    print(f"  {nome:<28} left={100*(px-x0f)/(x1f-x0f):5.1f}%  top={100*(py-y0f)/(y1f-y0f):5.1f}%")
