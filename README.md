# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_10:09:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,246 measurements** from **39** stations.
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
| 2026-09-07 10:09:11 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:09:08 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:07:00 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:06:52 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-09-07 10:06:45 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-07 10:06:34 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:06:12 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:06:10 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:05:58 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:04:52 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:04:28 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:04:24 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 10:03:48 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:03:36 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-07 10:03:28 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:03:03 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-09-07 10:03:03 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:02:58 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:02:55 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | -0.013 |  |
| 2026-09-07 10:02:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:02:44 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 10:02:40 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:02:40 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:02:27 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 10:02:18 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.070 |  |
| 2026-09-07 10:01:58 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.059 |  |
| 2026-09-07 10:01:57 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-09-07 10:01:47 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:01:11 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:00:46 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-07 10:00:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:00:10 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 09:59:50 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 09:59:18 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 09:44:29 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 09:08:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-07 10:02:27 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 10:06:45 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-07 09:05:39 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-07 10:02:44 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 10:00:46 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-07 10:04:24 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 10:02:40 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:00:10 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:04:52 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:03:28 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:09:08 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:02:18 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:03:03 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:05:58 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:04:28 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:09:11 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:01:47 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:06:10 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:06:12 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 09:07:11 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:03:48 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:06:34 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-07 09:07:48 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:00:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 10:01:57 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-09-07 10:02:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:07:00 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:02:40 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:01:11 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:02:58 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-09-07 10:02:55 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | -0.013 |  |
| 2026-09-07 10:03:03 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-09-07 10:03:36 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-07 10:06:52 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-09-07 10:01:58 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.059 |  |
| 2026-09-07 10:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)