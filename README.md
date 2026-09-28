# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_11:16:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,203 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 11:16:45 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.044 |  |
| 2026-09-28 11:15:17 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | -0.023 |  |
| 2026-09-28 11:13:31 | Baddegama (Gin Ganga) | 4.03 | 🟠 Minor Flood | -0.027 |  |
| 2026-09-28 11:11:49 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.031 |  |
| 2026-09-28 11:10:40 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:10:10 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-09-28 11:08:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-28 11:08:10 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:07:44 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:06:56 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:06:49 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:06:14 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:05:42 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:05:04 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.229 |  |
| 2026-09-28 11:04:55 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:04:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.030 |  |
| 2026-09-28 11:04:34 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:04:31 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:04:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:04:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:52 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:20 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:11 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:03:04 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.011 |  |
| 2026-09-28 11:03:03 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:02:46 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.080 |  |
| 2026-09-28 11:02:03 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:01:56 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 11:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:01:36 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.032 |  |
| 2026-09-28 11:01:32 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:01:27 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-28 11:01:25 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 11:13:31 | Baddegama (Gin Ganga) | 4.03 | 🟠 Minor Flood | -0.027 |  |
| 2026-09-28 11:15:17 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | -0.023 |  |
| 2026-09-28 11:04:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.030 |  |
| 2026-09-28 11:01:18 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-09-28 11:01:27 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-28 11:08:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-28 11:01:56 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 11:03:20 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:52 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:04:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:10:40 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:06:56 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:03 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:00:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:03:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:05:42 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:04:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:01:32 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:04:34 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:06:21 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 11:04:55 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:04:31 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:06:14 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:03:11 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:08:10 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:01:01 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:02:03 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:07:44 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:06:49 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-09-28 11:03:04 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.011 |  |
| 2026-09-28 11:10:10 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-09-28 11:01:25 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.030 |  |
| 2026-09-28 11:11:49 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.031 |  |
| 2026-09-28 11:01:36 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.032 |  |
| 2026-09-28 11:16:45 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.044 |  |
| 2026-09-28 11:02:46 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.080 |  |
| 2026-09-28 11:05:04 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)