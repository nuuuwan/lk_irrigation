# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_13:14:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,370 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 13:14:32 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:13:27 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-07 13:09:22 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:08:23 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.014 |  |
| 2026-09-07 13:07:27 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-09-07 13:06:54 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-07 13:05:54 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:05:36 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-09-07 13:05:35 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-07 13:05:34 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:05:03 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:52 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 13:04:47 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:39 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:39 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:23 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-09-07 13:04:18 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:08 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:03:56 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-07 13:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-07 13:02:49 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:48 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:31 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:31 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:22 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:20 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-09-07 13:02:14 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:46 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:42 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-07 13:01:42 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:36 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-09-07 13:01:26 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:00:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:00:48 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-07 13:00:41 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 13:01:42 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-07 12:06:25 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-07 13:03:56 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-07 13:04:52 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 13:05:35 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-07 13:06:54 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-07 13:00:48 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-07 13:13:27 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-07 13:02:14 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:00:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:18 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:00:41 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:14:32 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:05:34 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:48 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:31 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:39 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:22 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:09:22 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:39 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:31 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:05:03 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:26 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:47 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:20 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:42 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:05:54 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:01:46 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:04:08 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:49 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-07 13:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-07 13:01:36 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-09-07 13:07:27 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-09-07 13:08:23 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.014 |  |
| 2026-09-07 13:04:23 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-09-07 13:05:36 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-09-07 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)