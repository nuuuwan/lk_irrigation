# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_23:19:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,641 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 23:19:58 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:18:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.008 |  |
| 2026-09-18 23:08:20 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:07:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:06:22 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-18 23:06:07 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-18 23:05:36 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-09-18 23:05:24 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-18 23:05:10 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:05:03 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-09-18 23:03:52 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 23:03:50 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-18 23:03:48 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:03:37 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:03:35 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-18 23:03:27 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:03:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:02:57 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-18 23:02:50 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.100 |  |
| 2026-09-18 23:02:45 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-18 23:02:39 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.089 |  |
| 2026-09-18 23:02:13 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:01:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-09-18 23:01:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:08 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:04 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:02 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:00 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-18 23:00:45 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 23:02:57 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-18 23:06:22 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-18 23:01:00 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-18 23:03:50 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-18 23:02:45 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-18 23:05:24 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-18 23:06:07 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-18 23:03:52 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 22:10:14 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 22:10:58 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 23:01:04 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:00:45 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:03:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:19:58 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:03:27 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:05:10 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:00:25 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:02 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:03:37 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:08:20 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:08 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:18:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.008 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:03:48 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:02:13 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:07:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:05:05 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-09-18 23:03:35 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:03:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-09-18 23:05:36 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-09-18 22:07:14 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.032 |  |
| 2026-09-18 23:05:03 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-09-18 23:02:39 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.089 |  |
| 2026-09-18 23:02:50 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)