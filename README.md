# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/dankurniaone/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/rank.svg)](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/dankurniaone/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/reward.svg)](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [Deadpan Forecasts for Cities That Do Not Exist bounty on make.fun](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c).

`main.py` writes one deadpan weather forecast to `/output/entry.txt`: a
broadcast-style line for the invented city of Vostok-on-Sea — a high of
2 degrees, a low of one (1) working radiator, and snow that tastes
faintly of paperwork.

> Vostok-on-Sea: a high of 2 degrees, a low of one (1) working radiator, and snow that tastes faintly of paperwork.

Stdlib only, no network, deterministic. The program validates the 1–160
character gate (plus a concrete-number check, since the quest rewards a
concrete detail) before writing and verifies the file round-trips byte
for byte.

## Run

```sh
python3 main.py
```
