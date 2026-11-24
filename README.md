# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_23:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,818 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 23:03:16 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 23:02:28 | Dunamale (Aththanagalu Oya) | 3.75 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-11-24 23:02:12 | Pitabeddara (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-24 23:01:28 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 23:01:24 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.000 |  |
| 2026-11-24 23:01:02 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-24 23:00:57 | Siyambalanduwa (Heda Oya) | 1.99 | 🟢 Normal | 0.838 | 🔺 Rising |
| 2026-11-24 23:00:50 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-24 23:00:42 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-24 23:00:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-24 22:30:21 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -1.256 |  |
| 2026-11-24 22:28:55 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -1.256 |  |
| 2026-11-24 22:22:58 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-24 22:12:14 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 23:02:28 | Dunamale (Aththanagalu Oya) | 3.75 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-11-24 23:01:24 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.000 |  |
| 2026-11-24 23:00:57 | Siyambalanduwa (Heda Oya) | 1.99 | 🟢 Normal | 0.838 | 🔺 Rising |
| 2026-11-24 22:05:57 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | 0.486 | 🔺 Rising |
| 2026-11-24 22:02:10 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-11-24 22:05:26 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.375 | 🔺 Rising |
| 2026-11-24 23:00:42 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-24 22:03:57 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-24 22:04:36 | Glencourse (Kelani Ganga) | 12.67 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-11-24 22:01:18 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-11-24 23:02:12 | Pitabeddara (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-24 22:05:23 | Urawa (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-24 22:11:03 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-24 22:04:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-24 22:02:52 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-24 23:00:50 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-24 22:10:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-24 22:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-24 22:04:26 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-24 22:03:17 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-24 22:01:32 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 21:01:08 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-24 22:12:14 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-24 23:03:16 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 22:02:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-24 23:01:28 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 22:02:29 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 23:01:02 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-24 23:00:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-24 22:03:46 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 22:09:21 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | -0.074 |  |
| 2026-11-24 22:11:06 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.089 |  |
| 2026-11-24 22:05:13 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.199 |  |
| 2026-11-24 22:01:36 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | -0.368 |  |
| 2026-11-24 22:30:21 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -1.256 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)