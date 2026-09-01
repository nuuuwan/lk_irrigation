# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_08:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,756 measurements** from **39** stations.
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
| 2026-09-01 08:11:57 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-09-01 08:10:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-01 08:10:28 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:07:30 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:06:46 | Manampitiya (Mahaweli Ganga) | -0.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-01 08:05:24 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.070 |  |
| 2026-09-01 08:05:12 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:59 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:47 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:40 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-01 08:04:33 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 08:04:30 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:22 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:20 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 08:04:14 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.031 |  |
| 2026-09-01 08:04:05 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 08:04:01 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-01 08:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-09-01 08:03:42 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:03:35 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:03:12 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.034 |  |
| 2026-09-01 08:03:06 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.114 |  |
| 2026-09-01 08:03:04 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:48 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:47 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:37 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:35 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-09-01 08:02:34 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-01 08:02:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.040 |  |
| 2026-09-01 08:02:23 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:16 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 08:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:01:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.138 |  |
| 2026-09-01 08:01:35 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:01:06 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:00:46 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-01 07:34:13 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 08:04:01 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-01 07:00:53 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-01 08:02:34 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-01 08:04:05 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 08:06:46 | Manampitiya (Mahaweli Ganga) | -0.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-01 08:04:20 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 08:02:16 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 08:04:33 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 08:03:04 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:01:35 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:03:35 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:01:06 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:23 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:10:28 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:00:46 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:47 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:47 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:59 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:48 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:03:42 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:37 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:22 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:05:12 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:07:30 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 07:34:13 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:04:30 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:11:57 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-09-01 08:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-09-01 08:10:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-01 08:04:40 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-01 08:04:14 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.031 |  |
| 2026-09-01 08:03:12 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.034 |  |
| 2026-09-01 08:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.040 |  |
| 2026-09-01 08:05:24 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.070 |  |
| 2026-09-01 08:02:35 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-09-01 08:03:06 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.114 |  |
| 2026-09-01 08:01:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)