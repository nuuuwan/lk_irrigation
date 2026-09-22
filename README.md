# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_01:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,305 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 01:03:15 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:02 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.081 |  |
| 2026-09-23 01:02:57 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:33 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-09-23 01:02:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 01:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | -0.041 |  |
| 2026-09-23 01:01:55 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:01:48 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.022 |  |
| 2026-09-23 01:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:22 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.010 |  |
| 2026-09-23 01:01:09 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-09-23 01:00:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:00:30 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.043 |  |
| 2026-09-23 00:26:55 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.848 | 🔺 Rising |
| 2026-09-23 00:24:02 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 00:09:10 | Baddegama (Gin Ganga) | 4.04 | 🟠 Minor Flood | -0.028 |  |
| 2026-09-23 01:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | -0.041 |  |
| 2026-09-23 01:01:22 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.010 |  |
| 2026-09-23 01:00:30 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.043 |  |
| 2026-09-23 00:02:31 | Glencourse (Kelani Ganga) | 12.77 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-09-23 00:26:55 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.848 | 🔺 Rising |
| 2026-09-23 00:02:07 | Deraniyagala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-23 00:04:54 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 00:07:56 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-23 00:08:30 | Hanwella (Kelani Ganga) | 4.55 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-23 00:05:02 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 00:10:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-23 00:24:02 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-23 01:02:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:00:31 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:00:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 00:04:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 00:01:18 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 00:12:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:15 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:57 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-23 00:03:38 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:55 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-23 00:08:58 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 00:04:28 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-22 22:07:34 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.012 |  |
| 2026-09-23 00:05:49 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-09-23 01:01:09 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-09-23 01:01:48 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.022 |  |
| 2026-09-23 01:02:33 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-09-23 00:02:34 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.051 |  |
| 2026-09-23 01:03:02 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)