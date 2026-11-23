# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_01:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,038 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 01:13:45 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-24 01:10:31 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-24 01:10:27 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-24 01:06:04 | Holombuwa (Kelani Ganga) | 2.28 | 🟢 Normal | -0.380 |  |
| 2026-11-24 01:05:35 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 01:05:19 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-11-24 01:04:53 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-24 01:04:38 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.022 |  |
| 2026-11-24 01:04:27 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2026-11-24 01:03:58 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-11-24 01:03:56 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.024 |  |
| 2026-11-24 01:03:45 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-24 01:03:32 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.245 |  |
| 2026-11-24 01:03:10 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-24 01:03:05 | Giriulla (Maha Oya) | 3.90 | 🟢 Normal | 1.290 | 🔺 Rising |
| 2026-11-24 01:03:05 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-11-24 01:02:50 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.711 | 🔺 Rising |
| 2026-11-24 01:02:44 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-24 01:02:36 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-24 01:02:30 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-24 01:02:29 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 01:01:40 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:01:17 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.041 |  |
| 2026-11-24 01:01:08 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-24 01:01:07 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 00:06:03 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | 30.857 | 🔺 Rising |
| 2026-11-24 01:03:05 | Giriulla (Maha Oya) | 3.90 | 🟢 Normal | 1.290 | 🔺 Rising |
| 2026-11-24 01:02:50 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.711 | 🔺 Rising |
| 2026-11-24 01:03:58 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-11-24 01:13:45 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-24 00:11:25 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-24 01:03:45 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-24 01:04:53 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-24 00:00:17 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-24 01:03:10 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-24 01:02:44 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-24 01:01:08 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-24 01:10:27 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-24 00:24:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-24 01:10:31 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-24 00:10:40 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-24 01:05:35 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 00:04:06 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.005 |  |
| 2026-11-24 01:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-24 01:02:30 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-24 01:02:36 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:01:56 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:07:00 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:02:29 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:01:07 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:01:40 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:05:19 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-11-24 01:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.018 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-24 01:03:05 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 01:04:38 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.022 |  |
| 2026-11-24 01:03:56 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.024 |  |
| 2026-11-24 01:04:27 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2026-11-24 01:01:17 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.041 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-24 01:03:32 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.245 |  |
| 2026-11-24 01:06:04 | Holombuwa (Kelani Ganga) | 2.28 | 🟢 Normal | -0.380 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)