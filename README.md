# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_13:24:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,952 measurements** from **39** stations.
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
| 2026-09-01 13:24:58 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-09-01 13:20:14 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:12:04 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:11:37 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.035 |  |
| 2026-09-01 13:10:30 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:09:57 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:07:35 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-09-01 13:06:10 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:05:36 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:05:21 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:05:10 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-09-01 13:05:09 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-01 13:04:31 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:04:29 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:09 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:04:04 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:03 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:01 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 13:03:57 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.086 |  |
| 2026-09-01 13:03:52 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:03:51 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-01 13:03:42 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:03:34 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-01 13:03:27 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 13:03:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:03:15 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:03:07 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-01 13:02:54 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:02:48 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:02:41 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:02:33 | Manampitiya (Mahaweli Ganga) | -0.61 | 🟢 Normal | -0.020 |  |
| 2026-09-01 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.060 |  |
| 2026-09-01 13:01:43 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-09-01 13:01:19 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:01:17 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:01:08 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 13:01:43 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-09-01 13:05:09 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-01 13:03:51 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-01 13:03:07 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-01 13:03:34 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-01 13:04:01 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 13:03:27 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 13:03:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:02:54 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:01:08 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:03 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:06:10 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:02:41 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:01:19 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:09:57 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:20:14 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 11:02:11 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:04 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:01:17 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:12:04 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:09 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:04:29 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:10:30 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 13:24:58 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-09-01 13:03:15 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:03:42 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:02:48 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:04:31 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:03:52 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:05:21 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:04:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:05:36 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-01 13:07:35 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-09-01 13:02:33 | Manampitiya (Mahaweli Ganga) | -0.61 | 🟢 Normal | -0.020 |  |
| 2026-09-01 13:05:10 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-09-01 13:11:37 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.035 |  |
| 2026-09-01 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.060 |  |
| 2026-09-01 13:03:57 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)