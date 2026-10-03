"""Pomoćne funkcije za vežbe iz predmeta Digitalna obrada slike.

Upotreba u Colab-u (prva ćelija svake vežbe):

    !wget -q -N https://raw.githubusercontent.com/bojangutic/digitalna-obrada-slike/main/dos_utils.py
    from dos_utils import ucitaj_sliku, prikazi, spisak_slika
"""

import json
import os
import urllib.request

import cv2
import matplotlib.pyplot as plt
import numpy as np

REPO_URL = "https://raw.githubusercontent.com/bojangutic/digitalna-obrada-slike/main/slike/"

# Ako se modul pokreće iz kloniranog repozitorijuma, slike se čitaju lokalno.
_LOKALNI_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slike")
_KES_DIR = "slike"

SLIKE = {
    "astronaut": "astronaut.png",
    "autoput": "autoput.jpg",
    "cigle": "cigle.png",
    "dinari": "dinari.jpg",
    "dinari_dodir": "dinari_dodir.jpg",
    "ihc": "ihc.png",
    "kafa": "kafa.png",
    "kamerman": "kamerman.png",
    "konj": "konj.png",
    "macka": "macka.png",
    "mitoza": "mitoza.png",
    "novcici": "novcici.png",
    "orao": "orao.png",
    "otisak_prsta": "otisak_prsta.png",
    "panorama_1": "panorama_1.jpg",
    "panorama_2": "panorama_2.jpg",
    "panorama_3": "panorama_3.jpg",
    "pijaca": "pijaca.jpg",
    "racun": "racun.jpg",
    "raketa": "raketa.jpg",
    "raster_portret": "raster_portret.png",
    "rendgen": "rendgen.jpg",
    "sahovnica": "sahovnica.png",
    "smog": "smog.jpg",
    "stranica": "stranica.jpg",
    "stranica_senka": "stranica_senka.jpg",
    "tekst": "tekst.png",
    "zeleni_ekran": "zeleni_ekran.jpg",
    "zgrada": "zgrada.jpg",
    "zgrada_tamna": "zgrada_tamna.jpg",
}


def spisak_slika():
    """Vraća listu imena svih dostupnih slika."""
    return sorted(SLIKE)


def _putanja(fajl):
    """Vraća lokalnu putanju do fajla; preuzima ga sa GitHub-a ako je potrebno."""
    lokalno = os.path.join(_LOKALNI_DIR, fajl)
    if os.path.exists(lokalno):
        return lokalno
    os.makedirs(_KES_DIR, exist_ok=True)
    kes = os.path.join(_KES_DIR, fajl)
    if not os.path.exists(kes):
        urllib.request.urlretrieve(REPO_URL + fajl, kes)
    return kes


def ucitaj_sliku(ime, siva=False):
    """Učitava sliku iz repozitorijuma kursa.

    ime  -- ime slike bez ekstenzije, npr. "kafa" (vidi spisak_slika())
    siva -- ako je True, slika se učitava kao siva (jedan kanal)

    Vraća NumPy niz u OpenCV konvenciji: BGR redosled kanala, tip uint8.
    """
    if ime not in SLIKE:
        raise ValueError(f"Nepoznata slika '{ime}'. Dostupne slike: {', '.join(spisak_slika())}")
    slika = cv2.imread(_putanja(SLIKE[ime]), cv2.IMREAD_GRAYSCALE if siva else cv2.IMREAD_COLOR)
    if slika is None:
        raise IOError(f"Slika '{ime}' nije mogla da se učita.")
    return slika


def ucitaj_resenje(ime):
    """Učitava tačne podatke za sintetičke slike (npr. "dinari": pozicije i apoeni novčića)."""
    with open(_putanja(ime + ".json"), encoding="utf-8") as f:
        return json.load(f)


def prikazi(*slike, naslovi=None, kolone=None, velicina=4, bgr=True):
    """Prikazuje jednu ili više slika jednu pored druge.

    slike   -- jedna ili više slika (NumPy nizovi)
    naslovi -- lista naslova, po jedan za svaku sliku
    kolone  -- broj slika u jednom redu (podrazumevano: sve u jednom redu, najviše 4)
    velicina -- visina jedne slike u inčima
    bgr     -- True ako su slike u boji u BGR redosledu (kao iz OpenCV-a)

    Sive slike tipa uint8 prikazuju se u opsegu 0-255, bez automatskog
    razvlačenja kontrasta, tako da slika izgleda onako kako zaista jeste.
    """
    n = len(slike)
    if n == 0:
        return
    kolone = kolone or min(n, 4)
    redovi = (n + kolone - 1) // kolone
    fig, ose = plt.subplots(redovi, kolone, figsize=(velicina * kolone, velicina * redovi), squeeze=False)
    for i, osa in enumerate(ose.flat):
        osa.axis("off")
        if i >= n:
            continue
        slika = np.asarray(slike[i])
        if slika.ndim == 3 and slika.shape[2] == 4:
            slika = slika[:, :, :3]
        if slika.ndim == 3:
            if bgr:
                slika = slika[:, :, ::-1]
            if slika.dtype != np.uint8:
                slika = np.clip(slika, 0, 1 if slika.max() <= 1 else 255)
                if slika.max() > 1:
                    slika = slika.astype(np.uint8)
            osa.imshow(slika)
        elif slika.dtype == np.uint8:
            osa.imshow(slika, cmap="gray", vmin=0, vmax=255)
        elif slika.dtype == bool:
            osa.imshow(slika, cmap="gray", vmin=0, vmax=1)
        else:
            osa.imshow(slika, cmap="gray")
        if naslovi and i < len(naslovi):
            osa.set_title(naslovi[i])
    plt.tight_layout()
    plt.show()
