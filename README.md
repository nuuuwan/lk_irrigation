# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_03:29:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,474 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 03:29:43 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:23:42 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-21 03:21:28 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-11-21 03:21:27 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-11-21 03:12:18 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-21 03:08:15 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-21 03:07:40 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-21 03:07:16 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-11-21 03:07:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-11-21 03:06:41 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-21 03:06:11 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-21 03:05:39 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.118 |  |
| 2026-11-21 03:05:26 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-11-21 03:05:13 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-21 03:04:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.087 |  |
| 2026-11-21 03:04:23 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.052 |  |
| 2026-11-21 03:04:08 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:03:42 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:03:30 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -2.207 |  |
| 2026-11-21 03:03:28 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-21 03:03:15 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:47 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-11-21 03:02:47 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-21 03:02:42 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:30 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:29 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 2.820 | 🔺 Rising |
| 2026-11-21 03:02:29 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:25 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:01:50 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | 19.765 | 🔺 Rising |
| 2026-11-21 03:01:32 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:01:23 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:01:15 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-11-21 03:00:59 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 19.765 | 🔺 Rising |
| 2026-11-21 03:00:16 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.110 |  |
| 2026-11-21 02:59:29 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 19.765 | 🔺 Rising |
| 2026-11-21 02:53:20 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | 2.820 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 02:07:58 | Urawa (Nilwala Ganga) | 2.76 | 🟡 Alert | -0.086 |  |
| 2026-11-21 03:07:16 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-11-21 03:21:28 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-11-21 03:01:50 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | 19.765 | 🔺 Rising |
| 2026-11-21 03:02:29 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 2.820 | 🔺 Rising |
| 2026-11-21 03:05:26 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-11-21 03:01:15 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-11-21 03:07:40 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-21 03:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-21 03:06:41 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-21 03:05:13 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-21 03:02:47 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-21 03:08:15 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-21 00:15:47 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-21 03:06:11 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-21 00:09:50 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 03:23:42 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-21 03:03:28 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-21 03:01:32 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:25 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:01:23 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:04:08 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:42 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:29:43 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:29 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:03:42 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:02:30 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:12:18 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:03:15 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-21 03:02:47 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-21 03:04:23 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.052 |  |
| 2026-11-21 03:04:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.087 |  |
| 2026-11-21 03:00:16 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.110 |  |
| 2026-11-21 03:05:39 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.118 |  |
| 2026-11-21 03:03:30 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -2.207 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)