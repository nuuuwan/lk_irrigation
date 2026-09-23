# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_03:03:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Urawa — Alert; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 03:03:49 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:03:38 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-09-24 03:03:35 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:03:32 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 03:02:58 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:02:40 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 03:02:25 | Pitabeddara (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-09-24 03:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:30 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:16 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:59:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 03:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 02:05:10 | Urawa (Nilwala Ganga) | 2.80 | 🟡 Alert | 0.345 | 🔺 Rising |
| 2026-09-24 02:00:43 | Thawalama (Gin Ganga) | 4.33 | 🟡 Alert | 0.199 | 🔺 Rising |
| 2026-09-24 02:07:45 | Baddegama (Gin Ganga) | 3.83 | 🟡 Alert | 0.066 | 🔺 Rising |
| 2026-09-24 03:02:25 | Pitabeddara (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-09-24 02:04:19 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-09-24 02:02:58 | Peradeniya (Mahaweli Ganga) | 4.16 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-24 00:01:32 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 03:03:32 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 02:08:56 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-24 02:07:16 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-24 02:04:14 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-24 02:02:58 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 02:04:47 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 03:02:40 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:03:35 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:06:08 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:02:57 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:02:18 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:12:08 | Panadugama (Nilwala Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:03:49 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:04:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:00:15 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:05:53 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:03:29 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:06:18 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 02:09:08 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:02:58 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:01:30 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-24 01:32:25 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.018 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 03:03:38 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-09-24 02:04:56 | Nawalapitiya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.041 |  |
| 2026-09-24 02:07:04 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)