# Jak wygląda modelowanie matematyczne, czyli czy opłaca się biegać w deszczu?

**Autor:** Vlad Snozyk
**Instytucja:** Wydział Matematyki i Informatyki UJ

## Slide 1: Title
- Jak wygląda modelowanie matematyczne, czyli czy opłaca się biegać w deszczu?

## Slide 2: Model matematyczny na studiach
- Przykłady świetnych modeli matematycznych:
  - Wyznacznik
  - Liczby zespolone
  - Pochodne

## Slide 3: Model matematyczny na studiach
- Teoria teorią, ale w praktyce jest troszczkę inaczej...

## Slide 4: Problem biegania pod deszczem
- Na ulicy stoi człowiek. Nagle zaczyna padać deszcz.
- Osoba kieruje się do najbliższego schronienia oddalonego o l metrów.
- Pytanie: jaką prędkością powinien się poruszać, aby zmoknąć jak najmniej?

## Slide 5: Problem biegania pod deszczem (formalizacja)
- Prostopadłościan o powierzchniach równych a, b, c porusza się z prędkością prostopadłą do powierzchni a
- Pada deszcz — każda kropla ma prędkość v, ilość kropli w jednostce objętości wynosi k
- Pytanie: ile kropli N trafi w prostopadłościan podczas przemieszczenia na odległość l?
- Przy jakiej wartości prędkości liczba N będzie minimalna?

## Slide 6: Rozwiązanie
- Krok 1: Olewamy boczną stronę
- Przechodzimy do uproszczonego problemu 2D

## Slide 7: Problem uproszczony
- Na prostopadłościan pada deszcz z prędkością v w ciągu t sekund
- Ilość kropli deszczu w jednostce objętości wynosi k
- Pytanie: ile kropli trafi w prostopadłościan?
- v = vx + vy

## Slide 8–11: Plots
- pt1.png, pt2.png, pt3.png, pt4.png

## Slide 12: Wzór
- Volume = (Vx * a + Vy * b) * t
- N = Volume * k = (Vx * a + Vy * b) * t * k

## Slide 13: Wzór ogólny
- N = (Vx * a + Vy * b + Vz * c) * t * k

## Slide 14: Ruch względny
- Przykłady ruchu względnego:
  - Słońce
  - Ziemia
  - Pociąg
  - https://www.youtube.com/watch?v=8wqNX7_4vAE

## Slide 15: Animacje
- Animacje ilustrujące ruch względny i problem deszczu

## Slide 16–19: Przypadek 1. Wiatr wieje w twarz
- t = l / u
- Vx* = Vx + u (prędkość względna deszczu w osi x)
- N = (Vx* * a + Vy * b + Vz * c) * t * k
- N(u) = ((Vx + u) * a + Vy * b + Vz * c) / u * l * k
- N(u) = (Vx * a + Vy * b + Vz * c) / u * l * k + a * l * k
- Wniosek: im większa prędkość u, tym mniejsza liczba kropli — biec jak najszybciej

## Slide 20: Plot
- pt5.png

## Slide 21–26: Przypadek 2. Wiatr wieje w plecy
- t = l / u
- Vx* = Vx - u (prędkość względna deszczu w osi x)
- N(u) = (|Vx - u| * a + Vy * b + Vz * c) / u * l * k
- Podprzypadek Vx > u:
  - N(u) = (Vx * a + Vy * b + Vz * c) / u * l * k - a * l * k
  - Wniosek: im większa prędkość, tym mniej kropli — biec jak najszybciej
- Podprzypadek Vx ≤ u:
  - N(u) = (-Vx * a + Vy * b + Vz * c) / u * l * k + a * l * k
  - Wniosek: im większa prędkość, tym mniej kropli — biec jak najszybciej

## Slide 27: Plot
- pt6.png

## Slide 28: Pytania
- Pytania
