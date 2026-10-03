# Digitalna obrada slike — vežbe

Materijali za vežbe iz predmeta **Digitalna obrada slike**, Univerzitet Singidunum.

## Brzi početak (Google Colab)

Na početku svake vežbe pokrenite:

```python
!wget -q -N https://raw.githubusercontent.com/bojangutic/digitalna-obrada-slike/main/dos_utils.py
from dos_utils import ucitaj_sliku, prikazi, spisak_slika

slika = ucitaj_sliku("kafa")          # BGR, uint8
siva = ucitaj_sliku("kafa", siva=True)
prikazi(slika, siva, naslovi=["Original", "Siva"])
```

`spisak_slika()` vraća imena svih dostupnih slika.

## Sadržaj

- `dos_utils.py`: pomoćne funkcije za učitavanje i prikaz slika
- `slike/`: slike za vežbe; izvor, autor i licenca svake slike su u [slike/LICENSES.md](slike/LICENSES.md)
- `pregled_slika.jpg`: pregled svih slika na jednom mestu
