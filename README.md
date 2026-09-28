# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_19:23:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,512 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 19:23:25 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.008 |  |
| 2026-09-28 19:14:02 | Baddegama (Gin Ganga) | 3.72 | 🟡 Alert | -0.038 |  |
| 2026-09-28 19:12:44 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:11:57 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-28 19:11:34 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-28 19:10:17 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:09:21 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:09:18 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-09-28 19:09:17 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-09-28 19:07:59 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-28 19:06:50 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-28 19:06:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.086 |  |
| 2026-09-28 19:06:14 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-09-28 19:05:34 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-28 19:05:19 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:05:15 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-09-28 19:05:01 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.068 |  |
| 2026-09-28 19:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.048 |  |
| 2026-09-28 19:04:38 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:04:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:04:13 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:04:10 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:03:28 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-09-28 19:03:00 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:02:41 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:02:31 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:02:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:02:15 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-28 19:02:14 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.032 |  |
| 2026-09-28 19:02:13 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.011 |  |
| 2026-09-28 19:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 19:01:34 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:01:17 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 19:01:12 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:00:43 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 19:23:25 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.008 |  |
| 2026-09-28 19:14:02 | Baddegama (Gin Ganga) | 3.72 | 🟡 Alert | -0.038 |  |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-28 19:11:34 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-28 19:06:50 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-28 19:05:34 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-28 19:07:59 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-28 19:01:17 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 19:11:57 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-28 19:02:15 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-28 19:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 19:00:43 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:02:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:02:31 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:04:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:04:13 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:10:17 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:04:10 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:12:44 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:03:00 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:04:38 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:05:19 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:02:41 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:09:21 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:01:12 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:01:34 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 19:05:15 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 19:02:13 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.011 |  |
| 2026-09-28 18:02:25 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-09-28 19:09:17 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-09-28 19:06:14 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-09-28 19:09:18 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-09-28 19:03:28 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-09-28 19:02:14 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.032 |  |
| 2026-09-28 19:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.048 |  |
| 2026-09-28 19:05:01 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.068 |  |
| 2026-09-28 19:06:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)