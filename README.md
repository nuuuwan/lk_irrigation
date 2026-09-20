# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_04:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,600 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 04:02:53 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | -0.020 |  |
| 2026-09-21 04:02:40 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 04:02:31 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-21 04:02:30 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.246 |  |
| 2026-09-21 04:02:07 | Thawalama (Gin Ganga) | 5.09 | 🟡 Alert | -0.110 |  |
| 2026-09-21 04:02:00 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 04:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.28 | 🟡 Alert | 0.155 | 🔺 Rising |
| 2026-09-21 04:01:52 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.041 |  |
| 2026-09-21 04:01:51 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -1.262 |  |
| 2026-09-21 04:01:47 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.090 |  |
| 2026-09-21 04:01:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 04:01:07 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 04:01:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 04:00:52 | Magura (Kalu Ganga) | 5.70 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 03:20:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2026-09-21 03:18:31 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.246 |  |
| 2026-09-21 03:17:04 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 04:02:31 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-21 04:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.28 | 🟡 Alert | 0.155 | 🔺 Rising |
| 2026-09-21 03:07:11 | Baddegama (Gin Ganga) | 3.79 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 04:00:52 | Magura (Kalu Ganga) | 5.70 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 03:20:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2026-09-21 04:02:53 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | -0.020 |  |
| 2026-09-21 03:09:54 | Rathnapura (Kalu Ganga) | 6.28 | 🟡 Alert | -0.064 |  |
| 2026-09-21 04:02:07 | Thawalama (Gin Ganga) | 5.09 | 🟡 Alert | -0.110 |  |
| 2026-09-21 03:06:05 | Glencourse (Kelani Ganga) | 15.23 | 🟡 Alert | -0.128 |  |
| 2026-09-21 03:14:45 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 04:02:00 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 04:02:40 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 04:01:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:37 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 04:01:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:06:45 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:54 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:14:31 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:07:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:30 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-21 04:01:07 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:01:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:04:18 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-21 03:11:54 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-09-21 03:01:33 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-09-21 03:05:30 | Badalgama (Maha Oya) | 4.17 | 🟢 Normal | -0.030 |  |
| 2026-09-21 03:17:04 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.035 |  |
| 2026-09-21 04:01:52 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.041 |  |
| 2026-09-21 03:03:01 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.070 |  |
| 2026-09-21 04:01:47 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.090 |  |
| 2026-09-21 03:02:34 | Nawalapitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.095 |  |
| 2026-09-21 03:08:39 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.101 |  |
| 2026-09-21 03:06:00 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.108 |  |
| 2026-09-21 04:02:30 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.246 |  |
| 2026-09-21 03:05:48 | Peradeniya (Mahaweli Ganga) | 4.50 | 🟢 Normal | -0.294 |  |
| 2026-09-21 04:01:51 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -1.262 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)