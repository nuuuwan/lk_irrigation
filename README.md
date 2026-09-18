# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_03:03:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 03:03:05 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.090 |  |
| 2026-09-19 03:03:03 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.055 |  |
| 2026-09-19 03:02:46 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:41 | Magura (Kalu Ganga) | 4.06 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-19 03:02:32 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.122 |  |
| 2026-09-19 03:02:30 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:27 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:26 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:26 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -17.419 |  |
| 2026-09-19 03:02:24 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.080 |  |
| 2026-09-19 03:02:14 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:01:55 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -17.419 |  |
| 2026-09-19 03:01:48 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-09-19 03:01:37 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:01:25 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.044 |  |
| 2026-09-19 03:01:10 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:01:09 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-09-19 03:01:07 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 03:01:00 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:56:24 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 02:19:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-19 02:19:11 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 03:02:41 | Magura (Kalu Ganga) | 4.06 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-19 02:14:19 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-19 02:19:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-19 02:03:26 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-19 02:56:24 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 01:03:55 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 03:01:07 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 01:43:50 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-19 03:01:00 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:01:37 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:26 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:50 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:01:25 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:46 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:01:10 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:14 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:02:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:30 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:10:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:02:27 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:04:51 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:16:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-19 02:02:14 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-19 02:00:26 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-19 03:01:09 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-09-19 00:11:55 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-09-19 01:08:47 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.021 |  |
| 2026-09-19 03:01:48 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-09-19 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.044 |  |
| 2026-09-19 03:03:03 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.055 |  |
| 2026-09-19 03:02:24 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.080 |  |
| 2026-09-19 03:03:05 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.090 |  |
| 2026-09-19 03:02:32 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.122 |  |
| 2026-09-19 02:09:37 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -12.923 |  |
| 2026-09-19 03:02:26 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -17.419 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)