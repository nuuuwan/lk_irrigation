# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_21:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,194 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 21:02:55 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.030 |  |
| 2026-11-01 21:02:54 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:40 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:28 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-11-01 21:02:21 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 21:02:18 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:13 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.065 |  |
| 2026-11-01 21:01:54 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.017 |  |
| 2026-11-01 21:01:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 21:01:38 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-01 21:01:28 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-01 21:01:25 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-11-01 21:01:20 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 21:00:37 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-01 21:00:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 20:32:36 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-01 20:26:42 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 20:15:13 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.000 |  |
| 2026-11-01 20:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-11-01 21:01:25 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-11-01 21:02:28 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-11-01 21:00:37 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-01 21:01:28 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-01 21:01:38 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-01 20:32:36 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-01 20:02:15 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 21:01:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 21:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 20:05:49 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 20:05:41 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-01 21:02:21 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 21:00:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 20:04:54 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:07:00 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:40 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 20:05:39 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:54 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:13 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:18 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 20:05:32 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 20:15:51 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:20 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 20:05:50 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-01 20:03:11 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.011 |  |
| 2026-11-01 21:01:54 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.017 |  |
| 2026-11-01 20:04:47 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.025 |  |
| 2026-11-01 21:02:55 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 20:06:43 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-11-01 20:05:23 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.041 |  |
| 2026-11-01 20:04:01 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2026-11-01 21:01:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.065 |  |
| 2026-11-01 20:03:03 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)