# Mijn beleggingen

Toont totale winst en rendement (%) in de tijd.

## Opzetten
1. Zet deze bestanden in je repository en push.
2. Installeer de Python-afhankelijkheden: `python -m pip install -r requirements.txt`.
3. Settings → Pages → Deploy from branch → `main` / root.
4. Settings → Actions → General → Workflow permissions → *Read and write*.
5. Actions → "Update koersen" → *Run workflow* (haalt koersen op).

## Transacties toevoegen
Voeg een regel toe aan `trades.json` (`type`: `buy` of `sell`, optioneel `fee`).
Controleer bij "tickers" of de Yahoo-tickers kloppen; de script slaat alleen geldige datums/koersen op en gooit `NaN` weg zodat `prices.json` altijd geldig JSON blijft.
Het dashboard toont koersresultaat en dividend apart. Dividend wordt op Yahoo's ex-dividenddatum aan de positie toegerekend; die datum kan verschillen van de betaaldatum.
Het geannualiseerde rendement gebruikt XIRR: aankopen, verkopen, dividend en de huidige waarde worden op hun werkelijke datums meegenomen. Dat maakt het beter vergelijkbaar als er op verschillende momenten is ingelegd.
