# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_20:03:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,984 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 20:03:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:03:16 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-11-03 20:03:12 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-11-03 20:03:12 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-03 20:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.022 |  |
| 2026-11-03 20:03:05 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.054 |  |
| 2026-11-03 20:02:52 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-03 20:02:44 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-11-03 20:02:42 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-11-03 20:02:31 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:02:29 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-03 20:02:21 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-11-03 20:02:09 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.120 |  |
| 2026-11-03 20:01:48 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-03 20:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:01:17 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:00:32 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:00:21 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-11-03 19:18:19 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 19:07:49 | Urawa (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-11-03 19:03:29 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-11-03 20:01:48 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-03 20:03:12 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-03 20:03:16 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-11-03 19:04:38 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-03 19:15:22 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-03 20:03:12 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-03 19:04:37 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 19:04:52 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-03 20:02:29 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-03 19:00:40 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 19:05:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 20:02:31 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:02:09 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:01:17 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 19:02:29 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 20:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:03:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:00:32 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:02:57 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:01:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-03 20:02:42 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:18:19 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.016 |  |
| 2026-11-03 19:10:45 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.017 |  |
| 2026-11-03 19:12:18 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.017 |  |
| 2026-11-03 19:07:53 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.018 |  |
| 2026-11-03 20:02:52 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-03 20:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.022 |  |
| 2026-11-03 19:02:42 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.042 |  |
| 2026-11-03 20:03:05 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.054 |  |
| 2026-11-03 20:02:21 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-11-03 19:02:13 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.070 |  |
| 2026-11-03 20:02:44 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-11-03 20:00:21 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-11-03 20:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)