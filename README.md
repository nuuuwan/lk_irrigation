# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_02:05:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,348 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 02:05:05 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:05:00 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 02:05:00 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.149 |  |
| 2026-09-23 02:04:47 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.030 |  |
| 2026-09-23 02:04:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-23 02:04:18 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.030 |  |
| 2026-09-23 02:04:14 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.174 |  |
| 2026-09-23 02:03:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:03:20 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.090 |  |
| 2026-09-23 02:02:40 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:02:34 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:02:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:02:11 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | -0.020 |  |
| 2026-09-23 02:01:59 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-23 02:01:43 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:35 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:33 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:30 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.010 |  |
| 2026-09-23 02:01:21 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-23 02:01:12 | Glencourse (Kelani Ganga) | 12.83 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-23 02:00:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:00:42 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:00:19 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:58:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:56:56 | Rathnapura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.149 |  |
| 2026-09-23 01:33:05 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:32:32 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.027 |  |
| 2026-09-23 01:21:43 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.041 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 01:12:28 | Baddegama (Gin Ganga) | 4.02 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-23 01:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | -0.041 |  |
| 2026-09-23 02:01:30 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.010 |  |
| 2026-09-23 01:00:30 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.043 |  |
| 2026-09-23 01:15:23 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-23 02:01:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-23 02:05:00 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 01:21:43 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-23 02:01:12 | Glencourse (Kelani Ganga) | 12.83 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:00:19 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:02:34 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:00:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:02:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:33:05 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:00:42 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:43 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:59 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:02:40 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:03:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:05:05 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:04:21 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:35 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-23 02:01:33 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:04:07 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-23 02:01:21 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-23 02:04:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-22 22:07:34 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.012 |  |
| 2026-09-23 02:02:11 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | -0.020 |  |
| 2026-09-23 01:32:32 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.027 |  |
| 2026-09-23 01:07:48 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | -0.029 |  |
| 2026-09-23 02:04:18 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.030 |  |
| 2026-09-23 02:04:47 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.030 |  |
| 2026-09-23 01:02:33 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-09-23 02:03:20 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.090 |  |
| 2026-09-23 02:05:00 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.149 |  |
| 2026-09-23 02:04:14 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)