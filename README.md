# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_07:39:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,048 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 07:39:32 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | -0.018 |  |
| 2026-09-28 07:34:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:17:36 | Baddegama (Gin Ganga) | 4.15 | 🟠 Minor Flood | -0.098 |  |
| 2026-09-28 07:14:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:12:42 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:11:40 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:10:38 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:09:25 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.027 |  |
| 2026-09-28 07:08:57 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:08:48 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 07:08:40 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-28 07:07:47 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.027 |  |
| 2026-09-28 07:07:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.198 |  |
| 2026-09-28 07:07:34 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.036 |  |
| 2026-09-28 07:07:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:06:54 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-09-28 07:06:49 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | -0.154 |  |
| 2026-09-28 07:06:17 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:05:56 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:05:46 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-09-28 07:05:31 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-09-28 07:04:35 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:04:30 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-09-28 07:03:55 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 07:03:43 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | -0.217 |  |
| 2026-09-28 07:03:34 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 07:39:32 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | -0.018 |  |
| 2026-09-28 07:17:36 | Baddegama (Gin Ganga) | 4.15 | 🟠 Minor Flood | -0.098 |  |
| 2026-09-28 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | -0.217 |  |
| 2026-09-28 07:02:49 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 07:03:55 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 07:08:48 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 07:08:40 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-28 07:00:22 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:10:38 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:07:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:06:17 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:02:22 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:34:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:11:40 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:14:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:03:43 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:05:56 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:12:42 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:08:57 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:02:26 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:00:18 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:06:54 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-09-28 07:05:46 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-09-28 07:04:30 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-09-28 07:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-28 07:01:09 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-28 07:05:31 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-09-28 07:01:25 | Dunamale (Aththanagalu Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-09-28 07:01:14 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.022 |  |
| 2026-09-28 07:09:25 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.027 |  |
| 2026-09-28 07:07:47 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.027 |  |
| 2026-09-28 07:07:34 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.036 |  |
| 2026-09-28 07:00:22 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.041 |  |
| 2026-09-28 07:00:16 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.052 |  |
| 2026-09-28 07:03:15 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.128 |  |
| 2026-09-28 06:08:43 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.144 |  |
| 2026-09-28 07:06:49 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | -0.154 |  |
| 2026-09-28 07:07:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.198 |  |
| 2026-09-28 07:03:04 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)