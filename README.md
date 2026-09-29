# Mijn beleggingen

Toont totale winst en rendement (%) in de tijd.

## Opzetten
1. Zet deze bestanden in je repository en push.
2. Settings → Pages → Deploy from branch → `main` / root.
3. Settings → Actions → General → Workflow permissions → *Read and write*.
4. Actions → "Update koersen" → *Run workflow* (haalt koersen op).

## Transacties toevoegen
Voeg een regel toe aan `trades.json` (`type`: `buy` of `sell`, optioneel `fee`).
Controleer bij "tickers" of de Yahoo-tickers kloppen (Vanguard-ETF staat op `CHECK-TICKER`).
