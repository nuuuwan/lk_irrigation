# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_16:04:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,613 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 16:04:08 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-26 16:03:48 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-26 16:03:37 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.162 |  |
| 2026-09-26 16:03:21 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-26 16:03:18 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:03:15 | Hanwella (Kelani Ganga) | 5.33 | 🟢 Normal | -0.031 |  |
| 2026-09-26 16:03:15 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 16:03:14 | Nawalapitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.050 |  |
| 2026-09-26 16:02:54 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 16:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.95 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-26 16:02:33 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:02:20 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:02:11 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.110 |  |
| 2026-09-26 16:02:01 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:02:00 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | -0.034 |  |
| 2026-09-26 16:01:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:01:56 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:01:53 | Thawalama (Gin Ganga) | 2.81 | 🟢 Normal | -0.045 |  |
| 2026-09-26 16:01:38 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | -0.020 |  |
| 2026-09-26 16:01:31 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-09-26 16:01:23 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 16:01:11 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.034 |  |
| 2026-09-26 16:01:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:01:05 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 16:00:54 | Kithulgala (Kelani Ganga) | 2.42 | 🟢 Normal | -0.215 |  |
| 2026-09-26 16:00:45 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.103 |  |
| 2026-09-26 16:00:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 15:04:28 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 15:03:12 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 16:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.95 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-26 15:09:26 | Panadugama (Nilwala Ganga) | 5.90 | 🟡 Alert | -0.009 |  |
| 2026-09-26 16:01:05 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 15:09:09 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 16:02:54 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 16:03:15 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 16:01:31 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-09-26 16:02:20 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:00:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:02:01 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:01:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:02:33 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:19 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:04:17 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:01:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:31 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:05:38 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:01:56 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:03:18 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:04:08 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-26 16:01:23 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 16:03:21 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-26 15:02:54 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-09-26 16:01:38 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | -0.020 |  |
| 2026-09-26 16:03:48 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-26 15:05:10 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.031 |  |
| 2026-09-26 16:03:15 | Hanwella (Kelani Ganga) | 5.33 | 🟢 Normal | -0.031 |  |
| 2026-09-26 16:02:00 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | -0.034 |  |
| 2026-09-26 16:01:11 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.034 |  |
| 2026-09-26 16:01:53 | Thawalama (Gin Ganga) | 2.81 | 🟢 Normal | -0.045 |  |
| 2026-09-26 16:03:14 | Nawalapitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.050 |  |
| 2026-09-26 15:07:45 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | -0.072 |  |
| 2026-09-26 16:00:45 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.103 |  |
| 2026-09-26 16:02:11 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.110 |  |
| 2026-09-26 16:03:37 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.162 |  |
| 2026-09-26 16:00:54 | Kithulgala (Kelani Ganga) | 2.42 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)