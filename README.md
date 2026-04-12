# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_02:42:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 02:42:02 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-04-13 02:39:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 2.667 | 🔺 Rising |
| 2026-04-13 02:38:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 2.667 | 🔺 Rising |
| 2026-04-13 02:28:42 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-13 02:23:24 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:13:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.051 |  |
| 2026-04-13 02:12:19 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.125 |  |
| 2026-04-13 02:09:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 02:07:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:06:16 | Rathnapura (Kalu Ganga) | 3.68 | 🟢 Normal | -3.214 |  |
| 2026-04-13 02:06:07 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -6.261 |  |
| 2026-04-13 02:05:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-13 02:05:44 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -6.261 |  |
| 2026-04-13 02:05:26 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -6.261 |  |
| 2026-04-13 02:04:38 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.071 |  |
| 2026-04-13 02:04:24 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -3.214 |  |
| 2026-04-13 02:04:09 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-13 02:03:43 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 02:39:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 2.667 | 🔺 Rising |
| 2026-04-13 02:04:09 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-13 02:05:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-13 02:00:21 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-13 02:01:00 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 02:28:42 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-13 02:01:08 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-13 02:02:59 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-13 01:06:09 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 02:09:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 02:01:02 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-13 02:01:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:00:11 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:00:51 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:01:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:03:32 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:01:18 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:01:29 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:23:24 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:02:36 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:07:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:40:30 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:06:28 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:00:31 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:03:43 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:03:03 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:02:01 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:00:18 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-13 02:42:02 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-04-13 02:13:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.051 |  |
| 2026-04-13 02:04:38 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.071 |  |
| 2026-04-13 02:12:19 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.125 |  |
| 2026-04-13 02:02:57 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.171 |  |
| 2026-04-13 02:06:16 | Rathnapura (Kalu Ganga) | 3.68 | 🟢 Normal | -3.214 |  |
| 2026-04-13 02:06:07 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -6.261 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)