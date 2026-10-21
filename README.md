# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_03:07:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,511 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 03:07:22 | Holombuwa (Kelani Ganga) | 2.40 | 🟢 Normal | -0.077 |  |
| 2026-10-22 03:07:03 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-22 03:06:32 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.140 |  |
| 2026-10-22 03:06:17 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.005 |  |
| 2026-10-22 03:06:06 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-10-22 03:05:57 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-10-22 03:05:48 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 03:05:38 | Glencourse (Kelani Ganga) | 13.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-10-22 03:05:15 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 03:05:15 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-10-22 03:04:31 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2026-10-22 03:04:20 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-22 03:04:13 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-10-22 03:04:00 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-22 03:03:57 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.101 |  |
| 2026-10-22 03:03:21 | Yaka Wewa (Ma Oya) | 1.50 | 🟢 Normal | -0.059 |  |
| 2026-10-22 03:02:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-22 03:02:42 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 03:02:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.027 |  |
| 2026-10-22 03:02:24 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-22 03:02:22 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-10-22 03:02:11 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-22 03:02:06 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-22 03:02:03 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.051 |  |
| 2026-10-22 03:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.209 |  |
| 2026-10-22 03:01:20 | Horowpothana (Yan Oya) | 2.87 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-22 02:46:22 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 02:42:04 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-22 02:36:30 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.140 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 02:01:46 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-10-22 00:20:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 2.535 | 🔺 Rising |
| 2026-10-22 03:02:24 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-22 03:04:31 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2026-10-22 03:04:20 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-22 03:05:15 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-10-22 03:05:38 | Glencourse (Kelani Ganga) | 13.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-10-22 03:04:00 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-22 03:02:11 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-22 00:05:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 02:17:40 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-22 03:01:20 | Horowpothana (Yan Oya) | 2.87 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-22 03:07:03 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 02:03:21 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 03:05:48 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 03:05:15 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 03:06:06 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-10-22 03:02:42 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 03:06:17 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.005 |  |
| 2026-10-22 03:02:06 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-22 03:02:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-22 03:02:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.027 |  |
| 2026-10-22 02:04:21 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-10-22 03:05:57 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-10-22 03:02:22 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-10-22 03:04:13 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-10-22 03:02:03 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.051 |  |
| 2026-10-22 01:05:37 | Pitabeddara (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.052 |  |
| 2026-10-22 03:03:21 | Yaka Wewa (Ma Oya) | 1.50 | 🟢 Normal | -0.059 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-22 03:07:22 | Holombuwa (Kelani Ganga) | 2.40 | 🟢 Normal | -0.077 |  |
| 2026-10-22 03:03:57 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.101 |  |
| 2026-10-22 03:06:32 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.140 |  |
| 2026-10-22 03:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.209 |  |
| 2026-10-22 02:07:05 | Siyambalanduwa (Heda Oya) | 1.66 | 🟢 Normal | -0.287 |  |
| 2026-10-22 02:03:32 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.325 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)