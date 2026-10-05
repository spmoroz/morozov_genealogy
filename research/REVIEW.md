# Archival verification: proposed changes to DATA

Run 2026-10-05. 41 low-confidence persons (deceased or born before ~1926). Detail and sources: `findings_*.json`.
**Applied 2026-10-05:** all rows marked certain/probable in sections A and D (owner approval). Section B rows and "possible" matches remain open.

**Coverage caveat.** The cloud environment's network policy blocked pamyat-naroda.ru, obd-memorial.ru, podvignaroda.ru, bessmertnybarak.ru, nlr.ru/visz.nlr.ru, familysearch.org, forum.vgd.ru, kremnik.ru and others. "Nothing found" below means "not found in reachable sources", not "no record exists".

## A. Externally sourced (ЦГА РМ metrical books via Yandex Archive search)

| ID | Proposed change | Match | Source |
|---|---|---|---|
| P093 Евдокия Стефановна | Wife of P090 Пётр Ильич Прохоров; add as wife in F16; confidence → high | certain (re-verified) | ЦГА РМ ф.57 оп.4 д.120 скан 468; д.130 скан 50, 288; оп.5 д.23 скан 51; д.29 скан 299 |
| P082–P088 line | Church-record surname is **Антонов**, not Костин; add "Антонов" as primary or alias | probable | ф.57 оп.4 д.120, д.130, д.908, д.1095; оп.5 д.23, д.29 |
| P088 Фёдор | Фёдор Иванов Антонов, запасный унтер-офицер; wife Анна Ивановна; son Антон; confidence → medium | probable | findings_B_kostin.json |
| P087 Михаил | Михаил Иванов Антонов; wife Дарья Васильевна; brother of P088 (P088 was his wedding guarantor); confidence → medium | probable | findings_B_kostin.json |
| P092 Илья Иванов Прохоров | Wives: Варвара Ивановна (d. 1891–96), later Феодосия Семеновна; alive 1901–1908; confidence → medium | probable | findings_B_kostin.json |
| P201 Стефан | Parents confirmed as a couple 1897–1912; five siblings died in childhood | probable | findings_B_kostin.json |
| P084 Иван Николаевич | Age at death (74 in 1912) gives birth c. 1838, tree says 1841 | probable | findings_B_kostin.json |
| P086 Иван | Candidate: Иван Иванов Антонов, wife Дария Лаврентьева. Not proven, no change | possible | findings_B_kostin.json |

## B. Internal inconsistencies (from DATA itself, checked)

| ID | Problem | Suggested action |
|---|---|---|
| P060 Николай Фёдорович Миронов | Born 1881 but married 12.06.1891 to a wife born 1870 (age 10) | Re-check source; birth likely c. 1868–1871 |
| P032–P034 | Hypothesis "half-brothers (Ивановичи)" **refuted** by second pass: OBD/Подвиг народа give patronymic Константинович, born Керамсурка. See section D | Keep as sons of P030 |
| P104 / F36 | Екатерина **Евфимовна**, but F36 makes Андрей Широнин (P130) her father | Either F36 or the patronymic is wrong; if the patronymic holds, father = P131 Евфим |
| P062 Фёдор Миронов | Вольная/Малая Лашма founded after 1861 by settlers from Воскресенская Лашма | Birth place → Воскресенская Лашма (possible) |

## D. Second pass (obd-memorial.ru, podvignaroda.ru), `findings_E_wwii.json`

| ID | Proposed change | Source |
|---|---|---|
| P032 Василий Константинович | Birth 25.06.1912 Керамсурка (tree: 29.06); drafted 1934 Ардатовский РВК; МВД майор, off register 1960; confidence → medium | obd-memorial info.htm?id=70007423184 |
| P033 Сергей Константинович | Birth 12.09.1914 Керамсурка (tree: 11.09); drafted 1936 Козловский РВК; МВД капитан, off register 1961; confidence → medium | obd-memorial id=70009456670 |
| P034 Иван Константинович | Born 1919 Керамсурка; старшина, drafted 12.11.1939 Саранский РВК; орден Славы III ст. (12.01.1945, 385 сп 112 сд); confidence → medium | podvignaroda 1373927009, 40779743 |
| P146 Константин Балковский | Patronymic Константинович (fits P140 as father); drafted 15.09.1941 Калининский РВК Ленинграда, старшина 2 статьи | obd-memorial id=60011184278 |
| P143 Владимир Балковский | Birth 18.03.1906 Ленинград confirmed; инженер-капитан | obd-memorial id=70005022828 |
| new | Григорий Иванович Морозов, b. 22.11.1915 Керамсурка: possible son of P040, not in tree | obd-memorial id=70009160642 |

Discrepancies of 1–4 days in birth dates: officer files vs family data; keep both until a metrical record decides.

## C. Manual follow-ups (blocked or needs form search)

- pamyat-naroda.ru / obd-memorial.ru: Морозов Василий/Сергей/Иван (1912/1914/1919; try Константинович and Иванович); Ефремов Владимир/Георгий/Николай Павлович (1900–1915); Балковский Константин (1912, d. 09.01.1942), whose record may name his wife (P240).
- visz.nlr.ru/blockade: «Глод», address «Аптекарский пер. 4» (P171, P172); «Скородумова» (P239).
- ЦГА РМ ф.57 оп.5 д.23 (Кочелаево 1897–98): Стефан's birth 29.07.1898 (P201).
- ЦГА РМ ф.57 оп.5 д.37 (Воскресенская Лашма) and ГАПО 1858 revision list, Араповы estate (P062–P065, P241).
- familio.org: Керамсурка tree by С. Сорокин from revision lists to 1850 (P052, P053).
- ГАРО: Спасский у. as well as Сапожковский у. for Лукмос after ~1906.

## Not searched (possibly living, masked on the page)
P012, P013, P094, P095, P148, P231–P233.

## E. Manual checks by the owner, 2026-10-05 (pamyat-naroda.ru)

| Query | Result | Action |
|---|---|---|
| Балковский Константин, 1912 | 5 documents: lists 1941, loss register and report 26.04.1944, ЦАМО card 1982. Wife Смирнова Варвара Ивановна, daughter Валентина Константиновна, address Выборгская наб. 35 кв. 14 | Applied: P240, P148, F44 → high; P146 death place |
| ОБД id 70009160642 (opened by owner) | Учетно-послужная картотека офицерского состава: Морозов Григорий Иванович, b. 22.11.1915, Мордовская АССР, Козловский р-н, с. Керамсурка; призван 27.09.1937; ст. лейтенант; выбыл 01.02.1964; ЦАМО шкаф 659 ящик 858 | Not added to tree: parentage unproven. Patronymic, year and village fit P040 × P041 (married 1910). Awaiting relatives. Next step: request the personal file from ЦАМО (шкаф 659, ящик 858), which lists parents |
| Морозов Григорий Иванович, 1915 | Two namesakes, neither from Керамсурка: (1) b. Молдавия, Дубоссарский р-н, Орден Отечественной войны I ст. 1985; (2) b. Орловская обл., с. Сабурово, гв. сержант 26 гв. пабр, Орден Красной Звезды 30.04.1944 | Rejected. The Керамсурка record (OBD id 70009160642) remains the only lead; question to relatives stands |
| Глод-Сачук | Nothing found on pamyat-naroda | None |
| «Глод», «Глод-Сачук» in Блокада. Книга памяти (visz.nlr.ru) | Nothing found | Remaining: Ленинградский мартиролог, Пискарёвское кладбище lists, ЦГА СПб death records |
