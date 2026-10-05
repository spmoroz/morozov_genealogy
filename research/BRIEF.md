# Archival verification brief

Goal: for each assigned person (confidence `low` in `index.html` → `DATA.persons`), find independent records in open online archives that confirm, correct or extend the data. Do NOT edit `index.html`. Write findings only to your own output file.

## Inputs
- `index.html`: full `DATA` (persons + families). Read relatives' records too: places, dates and spouses of parents/children are the main search keys.
- `research/low_confidence_input.json`: your persons with parents/spouses/children pre-resolved.

## Key places (pre-1917 names)
- Керамсурка: Ардатовский у., Симбирская губ. (later Атяшевский р-н, Мордовия)
- Кочелаево, Малая/Вольная Лашма, Воскресенская Лашма: Наровчатский у., Пензенская губ. (later Ковылкинский р-н, Мордовия)
- Куваки: Нижнеломовский у., Пензенская губ.
- Лукмос: Сапожковский у., Рязанская губ.
- Ленинград / Санкт-Петербург (Балковские, Роговы, Глод-Сачук; блокада)
- Ташкент (Иван Павлович Ефремов, Ташкентская ж.д. 1921–1957)

## Sources to try (record each one you tried, with result)
- WWII: pamyat-naroda.ru, obd-memorial.ru, podvignaroda.ru
- Repression: lists.memo.ru (Жертвы политического террора), bessmertnybarak.ru, открытый список (ru.openlist.wiki)
- Blockade: «Блокада. Книга памяти» (visz.nlr.ru/blockade), Ленинградский мартиролог
- Pre-1917: FamilySearch catalog/indexes, metrical-book and ревизские сказки indexes, ЦГА Республики Мордовия, ГАПО (Пенза), ГАУО (Ульяновск/Симбирск), ГАРО (Рязань), vgd.ru forum threads for the villages, local village histories
- General web search (WebSearch / Exa) with name + village + year

## Rules
- Only deceased persons and persons born before ~1926. Do not search or record anything about living people. If a person might be living, mark `status: "skipped_possibly_living"` and move on.
- "Not found" is a fact about the source, not the person. Always list what was searched.
- A finding must have a URL and a short quote or record summary. No URL, no finding.
- If a record plausibly matches but identity is not certain (common name, age off by >3 years, different village), mark `match: "possible"` and say why.
- Flag conflicts with existing data explicitly.
- If a site is blocked by the network or needs a login, record that in `sources_tried` with result `"inaccessible"` and continue.
- Budget: roughly 10–15 searches per person max; prioritise persons with the most search keys (dates, village).

## Output: `research/findings_<GROUP>.json`
```json
[
  {
    "id": "P032",
    "name": "Василий Морозов",
    "status": "new_data | confirmed | conflict | nothing_found | skipped_possibly_living",
    "sources_tried": [{"source": "pamyat-naroda.ru", "query": "Морозов Василий Константинович 1912", "result": "found | not_found | inaccessible"}],
    "findings": [
      {"field": "death_date | birth_place | parents | military | other", "proposed_value": "...", "match": "certain | probable | possible", "source_url": "...", "evidence": "short quote or record summary", "conflicts_with_existing": "..." }
    ],
    "proposed_confidence": "low | medium | high",
    "rationale": "one or two sentences"
  }
]
```
Finish with a 5-line summary in your final message: persons with new data, conflicts, inaccessible sources.
