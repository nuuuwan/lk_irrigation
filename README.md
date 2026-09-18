# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_05:43:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,951 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Nawalapitiya — Major Flood; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 05:43:34 | Nawalapitiya (Mahaweli Ganga) | 9.00 | 🔴 Major Flood | 4.889 | 🔺 Rising |
| 2026-09-18 05:24:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-18 05:17:29 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.016 |  |
| 2026-09-18 05:14:48 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | -0.036 |  |
| 2026-09-18 05:11:27 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:11:16 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:08:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:07:13 | Baddegama (Gin Ganga) | 3.40 | 🟢 Normal | -0.030 |  |
| 2026-09-18 05:06:54 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.022 |  |
| 2026-09-18 05:06:14 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.066 |  |
| 2026-09-18 05:05:29 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-18 05:05:28 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:05:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:05:19 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:05:05 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-09-18 05:04:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:04:20 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-18 05:04:16 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:04:02 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-09-18 05:03:52 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.232 |  |
| 2026-09-18 05:03:36 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 05:03:12 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.051 |  |
| 2026-09-18 05:02:53 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:02:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:02:42 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:02:29 | Dunamale (Aththanagalu Oya) | 2.01 | 🟢 Normal | -0.038 |  |
| 2026-09-18 05:02:21 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:57 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:47 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.102 |  |
| 2026-09-18 05:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:21 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:17 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:00:54 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:00:50 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:00:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 05:43:34 | Nawalapitiya (Mahaweli Ganga) | 9.00 | 🔴 Major Flood | 4.889 | 🔺 Rising |
| 2026-09-18 05:01:47 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.102 |  |
| 2026-09-18 05:05:05 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-09-18 05:04:20 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-18 03:00:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 05:05:29 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-18 05:24:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-18 05:03:36 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:17 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:04:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:02:42 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:11:16 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:02:53 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:02:21 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:06:13 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:05:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:21 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:02:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:08:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:01:57 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:11:27 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:05:28 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 05:04:16 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:00:54 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:05:19 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:00:50 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-18 05:17:29 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.016 |  |
| 2026-09-18 05:06:54 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.022 |  |
| 2026-09-18 05:07:13 | Baddegama (Gin Ganga) | 3.40 | 🟢 Normal | -0.030 |  |
| 2026-09-18 05:14:48 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | -0.036 |  |
| 2026-09-18 05:02:29 | Dunamale (Aththanagalu Oya) | 2.01 | 🟢 Normal | -0.038 |  |
| 2026-09-18 05:03:12 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.051 |  |
| 2026-09-18 05:04:02 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-09-18 05:06:14 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.066 |  |
| 2026-09-18 05:03:52 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)