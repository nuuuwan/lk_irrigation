# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_20:09:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 20:09:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-28 20:07:35 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-09-28 20:07:24 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:06:18 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-09-28 20:06:16 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.033 |  |
| 2026-09-28 20:05:17 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-09-28 20:04:57 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -18.000 |  |
| 2026-09-28 20:04:55 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -18.000 |  |
| 2026-09-28 20:04:50 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.048 |  |
| 2026-09-28 20:04:40 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-09-28 20:04:36 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 20:04:30 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.022 |  |
| 2026-09-28 20:04:02 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-28 20:03:47 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:03:40 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | -0.030 |  |
| 2026-09-28 20:03:39 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:03:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-28 20:03:02 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:03:01 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.112 |  |
| 2026-09-28 20:02:49 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:45 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:43 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.050 |  |
| 2026-09-28 20:02:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:32 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.052 |  |
| 2026-09-28 20:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:09 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-09-28 20:01:54 | Baddegama (Gin Ganga) | 3.68 | 🟡 Alert | -0.050 |  |
| 2026-09-28 20:01:39 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:01:18 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-28 20:01:17 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:01:16 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:00:41 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:00:39 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-28 20:00:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 20:03:40 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | -0.030 |  |
| 2026-09-28 20:01:54 | Baddegama (Gin Ganga) | 3.68 | 🟡 Alert | -0.050 |  |
| 2026-09-28 20:02:09 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-28 20:09:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-28 19:11:57 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-28 20:01:18 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-28 20:04:36 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 20:03:02 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:00:41 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:01:16 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:03:47 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:49 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:00:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:07:24 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:03:39 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:02:45 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:09:21 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:01:39 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:01:17 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:07:35 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-09-28 20:04:02 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-28 20:05:17 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-09-28 20:03:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-28 20:00:39 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 20:06:18 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-09-28 20:04:30 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.022 |  |
| 2026-09-28 20:06:16 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.033 |  |
| 2026-09-28 20:04:50 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.048 |  |
| 2026-09-28 19:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.048 |  |
| 2026-09-28 20:02:43 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.050 |  |
| 2026-09-28 20:02:32 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.052 |  |
| 2026-09-28 20:04:40 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-09-28 20:03:01 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.112 |  |
| 2026-09-28 20:04:57 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)