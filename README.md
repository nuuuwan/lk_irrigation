# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_21:07:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 21:07:15 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-09 21:07:11 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.045 |  |
| 2026-10-09 21:06:24 | Urawa (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-09 21:06:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:05:30 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-10-09 21:05:09 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.050 |  |
| 2026-10-09 21:04:36 | Glencourse (Kelani Ganga) | 12.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 21:04:23 | Giriulla (Maha Oya) | 3.46 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-09 21:04:16 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:04:12 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-09 21:03:48 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-09 21:03:37 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:03:34 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-10-09 21:03:28 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-09 21:03:27 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-10-09 21:03:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:02:45 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-09 21:02:34 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:02:16 | Peradeniya (Mahaweli Ganga) | 4.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-09 21:02:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:02:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:02:13 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:01:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:01:52 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:01:37 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:00:43 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.711 |  |
| 2026-10-09 21:00:43 | Moragaswewa (Deduru Oya) | 1.63 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-09 21:00:11 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 20:09:47 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | -0.027 |  |
| 2026-10-09 20:02:47 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-09 20:06:40 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-09 20:02:02 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-10-09 21:04:12 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-09 21:00:43 | Moragaswewa (Deduru Oya) | 1.63 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-09 21:04:23 | Giriulla (Maha Oya) | 3.46 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-09 21:03:28 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-09 21:02:45 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-09 20:10:15 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-09 21:02:16 | Peradeniya (Mahaweli Ganga) | 4.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-09 21:03:48 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-09 21:04:36 | Glencourse (Kelani Ganga) | 12.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 21:07:15 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-09 21:00:11 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 21:01:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:02:13 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:02:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:06:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:02:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:03:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:03:37 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-09 21:04:16 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:01:37 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:02:34 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:01:52 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-10-09 21:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-09 20:22:33 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.017 |  |
| 2026-10-09 21:06:24 | Urawa (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-09 21:05:30 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-10-09 21:03:27 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-10-09 21:07:11 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.045 |  |
| 2026-10-09 21:05:09 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.050 |  |
| 2026-10-09 21:03:34 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-10-09 20:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.077 |  |
| 2026-10-09 21:00:43 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.711 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)