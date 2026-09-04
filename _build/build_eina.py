# -*- coding: utf-8 -*-
"""
Munta l'eina autònoma «Test d'aprofitament · Punt Lila de Montgat».

Pren _build/_template.html i hi incrusta els logotips institucionals en base64
(extrets de l'eina del Segell de qualitat del comerç de Montgat, que ja els
portava incrustats) per generar un únic fitxer HTML que funciona sense connexió.

Ús:  python _build/build_eina.py
"""
import io
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
ARREL = os.path.dirname(AQUI)

TEMPLATE = os.path.join(AQUI, "_template.html")
LOGOS = os.path.join(AQUI, "logos.json")
SORTIDA = os.path.join(ARREL, "Test_Punt_Lila_Montgat.html")

with io.open(LOGOS, encoding="utf-8") as f:
    logos = json.load(f)

with io.open(TEMPLATE, encoding="utf-8") as f:
    html = f.read()

for clau in ("HDR_DIBA", "HDR_MONTGAT", "LOGO_DIBA_SEAL", "LOGO_MONTGAT_SEAL"):
    marca = "__%s__" % clau
    if marca not in html:
        raise SystemExit("Falta la marca %s a la plantilla." % marca)
    html = html.replace(marca, logos[clau])

with io.open(SORTIDA, "w", encoding="utf-8") as f:
    f.write(html)

print("Generat: %s (%.0f KB)" % (SORTIDA, os.path.getsize(SORTIDA) / 1024))
