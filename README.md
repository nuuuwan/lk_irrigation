# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_03:20:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 03:20:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2026-09-21 03:18:31 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.033 |  |
| 2026-09-21 03:17:04 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.035 |  |
| 2026-09-21 03:14:45 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-21 03:14:18 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | -0.041 |  |
| 2026-09-21 03:11:54 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-09-21 03:09:54 | Rathnapura (Kalu Ganga) | 6.28 | 🟡 Alert | -0.064 |  |
| 2026-09-21 03:08:39 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.101 |  |
| 2026-09-21 03:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-09-21 03:07:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:07:11 | Baddegama (Gin Ganga) | 3.79 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 03:06:45 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:06:05 | Glencourse (Kelani Ganga) | 15.23 | 🟡 Alert | -0.128 |  |
| 2026-09-21 03:06:00 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.108 |  |
| 2026-09-21 03:05:48 | Peradeniya (Mahaweli Ganga) | 4.50 | 🟢 Normal | -0.294 |  |
| 2026-09-21 03:05:30 | Badalgama (Maha Oya) | 4.17 | 🟢 Normal | -0.030 |  |
| 2026-09-21 03:04:18 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:54 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:51 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-09-21 03:03:37 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:32 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-21 03:03:30 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:01 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.070 |  |
| 2026-09-21 03:02:57 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:02:34 | Nawalapitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.095 |  |
| 2026-09-21 03:02:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:02:23 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 03:02:20 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.023 |  |
| 2026-09-21 03:02:19 | Thawalama (Gin Ganga) | 5.20 | 🟡 Alert | -0.134 |  |
| 2026-09-21 03:01:44 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.175 |  |
| 2026-09-21 03:01:33 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-09-21 03:01:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:00:45 | Magura (Kalu Ganga) | 5.68 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 03:00:34 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 03:02:20 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.023 |  |
| 2026-09-21 03:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-09-21 03:07:11 | Baddegama (Gin Ganga) | 3.79 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 03:00:45 | Magura (Kalu Ganga) | 5.68 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 03:02:23 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 03:20:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2026-09-21 03:09:54 | Rathnapura (Kalu Ganga) | 6.28 | 🟡 Alert | -0.064 |  |
| 2026-09-21 03:06:05 | Glencourse (Kelani Ganga) | 15.23 | 🟡 Alert | -0.128 |  |
| 2026-09-21 03:02:19 | Thawalama (Gin Ganga) | 5.20 | 🟡 Alert | -0.134 |  |
| 2026-09-21 03:14:45 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 03:03:32 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 03:00:34 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:37 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:02:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:06:45 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:54 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:14:31 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:07:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:30 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:02:57 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:03:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:01:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 03:04:18 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-21 03:11:54 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-09-21 03:03:51 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-09-21 03:01:33 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-09-21 03:05:30 | Badalgama (Maha Oya) | 4.17 | 🟢 Normal | -0.030 |  |
| 2026-09-21 03:18:31 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.033 |  |
| 2026-09-21 03:17:04 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.035 |  |
| 2026-09-21 03:14:18 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | -0.041 |  |
| 2026-09-21 03:03:01 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.070 |  |
| 2026-09-21 03:02:34 | Nawalapitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.095 |  |
| 2026-09-21 03:08:39 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.101 |  |
| 2026-09-21 03:06:00 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.108 |  |
| 2026-09-21 03:01:44 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.175 |  |
| 2026-09-21 03:05:48 | Peradeniya (Mahaweli Ganga) | 4.50 | 🟢 Normal | -0.294 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)