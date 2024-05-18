# JPplusShinkansen

Welcome to 🇯🇵🚅 **JP+Shinkansen!** 🚅🇯🇵

This is the sister set to 🚂[JP+ Engines & Wagons](https://github.com/EmperorJake/JPengines)🚂 , 🚆[JP+ Multiple Units](https://github.com/Tintinfan/JPplusSet)🚆 and 🚇[JP+ Major Private Companies](https://github.com/Yozora3/JPplusPrivate)🚇, adding the world's first High Speed Rail Network's iconic trains.

## Credits
**Coding:** KeepinItRail\
**Graphics:** KeepinItRail, Yozora, Azusa & Erato\
**Translations:** freeaim (Japanese), CoconutKR (Korean)\
**Thanks to:** The JapanSet Team, Tinny, Emperor Jake, Saya

## Features

* Long Sprites for 'full Shinkansen' - choose different liveries via the Cargo Subtype Menu
* Normal Length Sprites for Mini-Shinkansen
* Real World Stats were possible (or approximations when not known)
* Parameters for;
    * Full length Shinkansen size - Choose between 10/8 or 12/8
    * Disabling JapanSet Shinkansen
    * Enabling Shinkansen Tracks (to counteract the previous parameter which disables JapanSet Shinkansen tracks)
    * Disabling Shinkansen Track Fences
    * Capacity Levels
    * Usage of Doctor Yellow Shinkansen

## JR West of Tokyo

| | Shinkansen | Release | End Year  | Speed (km/h) | Weight per car|
| --- | --- | --- | --- | --- | --- |
|![0 Series](/src/trains/0_series/12/purchase_original.png)| 0 Series | 1964 | 2008 |  210^ | 61t |
|![100 Series](/src/trains/100_series/12/purchase_original_jnr.png)| 100 Series | 1985 | 2012 | 220 | 53t
|![300 Series](/src/trains/300_series/12/purchase.png)| 300 Series | 1992 | 2012 | 270 | 44t|
|![500 Series](/src/trains/500_series/12/purchase.png)| 500 Series | 1997 | N/A | 300 | 42t |
|![700 Series](/src/trains/700_series/12/purchase.png)| 700 Series | 1999 | N/A | 285 | 44t |
|![N700 Series](/src/trains/n700_series/12/buy_n700.png)| N700 Series | 2007 | N/A | 300|44t|
|![800 Series](/src/trains/800_series/12/purchase.png)| 800 Series | 2004 | N/A | 260 | 44t |
|![L0 Series](/src/trains/l0_series/12/purchase_32bpp.png)| L0 Series | 2027 | N/A | 505 | 88t|

^ 210 km/h until 1986, 220 km/h thereafter

## JR East

| | Shinkansen | Release | End Year  | Speed (km/h) | Weight per car |
| --- | --- | --- | --- |--- | --- |
|![200 Series](/src/trains/200_series/12/purchase_original_jre.png)| 200 Series | 1982 | 2008 | 210~ | 58t
|![400 Series](/src/trains/400_series/buy_400.png)| 400 Series | 1992 | 2010 | 240 | 42t
|![E1 Series](/src/trains/e1_series/12/buy_e1_original.png)| E1 Series | 1994 | 2012 | 240 | 58t
|![E2 Series](/src/trains/e2_series/12/buy_red.png)| E2 Series | 1997 | N/A | 275 | 46t
|![E3 Series](/src/trains/e3_series/buy_e3_r.png)| E3 Series | 1997 | N/A | 275 | 43t
|![E4 Series](/src/trains/e4_series/12/purchase_yellow.png)| E4 Series | 1997 | N/A^ | 240 | 54t |
|![E5 Series](/src/trains/e5_series/12/purchase.png)| E5 Series | 2011 | N/A | 321 | 45t
|![E6 Series](/src/trains/e6_series/purchase.png)| E6 Series | 2013| N/A | 321 | 42t
|![E7 Series](/src/trains/e7_series/12/purchase.png)| E7/W7 Series | 2014 | N/A | 275 | 45t
|![E8 Series](/src/trains/e8_series/purchase.png)| E8 Series | 2024 | N/A | 300 | 42t

~ 210 km/h until 1989, 240 km/h thereafter
^ Technically out of service from 2021, but I like it, so it won't expire. Viva the E4! 😉

## Building

These following tools are required to build the GRF:

- nmlc
- python

Using `bash` is suggested, but powershell also works.

*Note: `git on Windows` provides a `bash` environment.*

This GRF could be built on multiple platforms; however, if you are on Windows, please change the end of line sequence from `CRLF` to `LF`. You could only change `JPPlusShinkansen.nml` without changing the other files, and it would still work.

## Useful Sources

https://en.wikipedia.org/wiki/Shinkansen\
http://kakeyama.image.coocan.jp/tec.htm
