# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_03:33:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 03:33:02 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-09-18 03:14:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-09-18 03:13:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-09-18 03:12:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:12:42 | Baddegama (Gin Ganga) | 3.45 | 🟢 Normal | -3.789 |  |
| 2026-09-18 03:12:23 | Baddegama (Gin Ganga) | 3.47 | 🟢 Normal | -3.789 |  |
| 2026-09-18 03:12:08 | Baddegama (Gin Ganga) | 3.49 | 🟢 Normal | -3.789 |  |
| 2026-09-18 03:09:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-18 03:08:37 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | -0.018 |  |
| 2026-09-18 03:08:22 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | -0.107 |  |
| 2026-09-18 03:07:34 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:07:32 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:06:55 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-09-18 03:06:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:06:21 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:06:13 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:05:47 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:05:29 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-09-18 03:05:09 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:04:53 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.319 |  |
| 2026-09-18 03:03:33 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:03:11 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:03:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:03:09 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:50 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-18 03:02:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:48 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:41 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:35 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:22 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:02:20 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:01:55 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:01:30 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:00:47 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:00:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 03:08:22 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | -0.107 |  |
| 2026-09-18 03:14:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-09-18 02:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-18 03:09:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-18 03:02:50 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-18 03:00:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 03:02:22 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:03:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:12:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:06:21 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:05:47 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:03:33 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:48 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:06:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:03:09 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:20 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:07:32 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:06:13 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:41 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:03:11 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:07:34 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:02:35 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:00:47 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:01:30 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:05:09 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:08:37 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | -0.018 |  |
| 2026-09-18 03:33:02 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-09-18 03:06:55 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-09-18 03:05:29 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-09-18 02:03:40 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-09-18 00:01:47 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.060 |  |
| 2026-09-18 03:04:53 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.319 |  |
| 2026-09-18 02:18:09 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -1.091 |  |
| 2026-09-18 03:12:42 | Baddegama (Gin Ganga) | 3.45 | 🟢 Normal | -3.789 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)