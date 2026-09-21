# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_23:21:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,354 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 23:21:57 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-09-21 23:18:05 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-21 23:16:36 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:13:48 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-21 23:09:50 | Rathnapura (Kalu Ganga) | 5.28 | 🟡 Alert | -0.100 |  |
| 2026-09-21 23:09:30 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:09:20 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.075 |  |
| 2026-09-21 23:07:37 | Panadugama (Nilwala Ganga) | 5.33 | 🟡 Alert | -0.019 |  |
| 2026-09-21 23:06:47 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-09-21 23:06:28 | Ellagawa (Kalu Ganga) | 9.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:05:54 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-21 23:05:50 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:05:08 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-09-21 23:04:30 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:04:27 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.103 |  |
| 2026-09-21 23:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.13 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-21 23:04:16 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.049 |  |
| 2026-09-21 23:03:59 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.032 |  |
| 2026-09-21 23:03:53 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-09-21 23:03:30 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-21 23:03:13 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:02:45 | Hanwella (Kelani Ganga) | 5.24 | 🟢 Normal | -0.040 |  |
| 2026-09-21 23:02:39 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:54 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-09-21 23:01:54 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:53 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:50 | Glencourse (Kelani Ganga) | 12.87 | 🟢 Normal | -0.071 |  |
| 2026-09-21 23:01:40 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 23:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:34 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:11 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:00:58 | Magura (Kalu Ganga) | 5.15 | 🟡 Alert | -108.000 |  |
| 2026-09-21 23:00:57 | Magura (Kalu Ganga) | 5.18 | 🟡 Alert | -108.000 |  |
| 2026-09-21 23:00:48 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:00:37 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:00:34 | Magura (Kalu Ganga) | 5.18 | 🟡 Alert | -108.000 |  |
| 2026-09-21 23:00:16 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 23:05:54 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-21 23:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.13 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-21 23:21:57 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-09-21 23:07:37 | Panadugama (Nilwala Ganga) | 5.33 | 🟡 Alert | -0.019 |  |
| 2026-09-21 23:09:50 | Rathnapura (Kalu Ganga) | 5.28 | 🟡 Alert | -0.100 |  |
| 2026-09-21 23:00:58 | Magura (Kalu Ganga) | 5.15 | 🟡 Alert | -108.000 |  |
| 2026-09-21 23:03:53 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-09-21 23:03:30 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-21 23:13:48 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-21 23:01:40 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 23:18:05 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-21 22:06:13 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-21 23:00:16 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:00:37 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:00:48 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:09:30 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:06:28 | Ellagawa (Kalu Ganga) | 9.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:53 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:03:13 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:16:36 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:05:50 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:34 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:04:30 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:01:11 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:02:39 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:06:47 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-09-21 23:05:08 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-21 23:01:54 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-09-21 23:03:59 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.032 |  |
| 2026-09-21 23:02:45 | Hanwella (Kelani Ganga) | 5.24 | 🟢 Normal | -0.040 |  |
| 2026-09-21 23:04:16 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.049 |  |
| 2026-09-21 23:01:50 | Glencourse (Kelani Ganga) | 12.87 | 🟢 Normal | -0.071 |  |
| 2026-09-21 23:09:20 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.075 |  |
| 2026-09-21 23:04:27 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)