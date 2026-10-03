# Digitalna obrada slike — vežbe

Materijali za vežbe iz predmeta **Digitalna obrada slike**, Univerzitet Singidunum.

## Sveske za vežbe (Google Colab)

Za svaku vežbu postoji sveska sa popunjenom prvom ćelijom i praznim ćelijama za svaki korak
vođenog primera, u koje kucate kod iz praktikuma. Sveska se otvara klikom na dugme; da biste
sačuvali svoj rad, u Colab-u izaberite **File → Save a copy in Drive**.

| Vežba | Sveska |
|---|---|
| 1. Slika kao matrica | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v01-slika-kao-matrica.ipynb) |
| 2. Geometrijske transformacije | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v02-geometrijske-transformacije.ipynb) |
| 3. Boje i aritmetika piksela | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v03-boje-i-aritmetika.ipynb) |
| 4. Histogram i intenzitetske transformacije | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v04-histogram.ipynb) |
| 5. Šum i prostorno filtriranje | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v05-sum-i-filtriranje.ipynb) |
| 6. Frekvencijski domen | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v06-frekvencijski-domen.ipynb) |
| 7. Ivice | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v07-ivice.ipynb) |
| 8. Binarizacija i morfologija | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v08-binarizacija-i-morfologija.ipynb) |
| 9. Segmentacija i konture | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v09-segmentacija-i-konture.ipynb) |
| 10. Obeležja i poravnanje | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v10-obelezja-i-poravnanje.ipynb) |
| 11. Neuronske mreže za slike | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v11-neuronske-mreze.ipynb) |
| 12. Transfer learning i savremeni modeli | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/v12-transfer-learning.ipynb) |
| Dodatak A: NumPy za rad sa slikama | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bojangutic/digitalna-obrada-slike/blob/main/sveske/dodatak-a-numpy.ipynb) |

## Brzi početak bez sveske

U praznoj Colab svesci na početku vežbe pokrenite:

```python
!wget -q -N https://raw.githubusercontent.com/bojangutic/digitalna-obrada-slike/main/dos_utils.py
from dos_utils import ucitaj_sliku, prikazi, spisak_slika

slika = ucitaj_sliku("kafa")          # BGR, uint8
siva = ucitaj_sliku("kafa", siva=True)
prikazi(slika, siva, naslovi=["Original", "Siva"])
```

`spisak_slika()` vraća imena svih dostupnih slika.

## Sadržaj

- `sveske/`: Colab sveske za vežbe (tabela iznad)
- `dos_utils.py`: pomoćne funkcije za učitavanje i prikaz slika
- `slike/`: slike za vežbe; izvor, autor i licenca svake slike su u [slike/LICENSES.md](slike/LICENSES.md)
- `pregled_slika.jpg`: pregled svih slika na jednom mestu
