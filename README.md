# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_17:13:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,343 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 17:13:49 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:11:09 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-09 17:10:05 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.032 |  |
| 2026-10-09 17:08:01 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-10-09 17:07:43 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.028 |  |
| 2026-10-09 17:07:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-09 17:07:10 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 17:06:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:06:10 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.109 |  |
| 2026-10-09 17:06:08 | Urawa (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-09 17:05:53 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2026-10-09 17:05:28 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-09 17:04:59 | Giriulla (Maha Oya) | 2.92 | 🟢 Normal | -0.059 |  |
| 2026-10-09 17:04:58 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-10-09 17:04:46 | Norwood (Kelani Ganga) | 1.58 | 🟡 Alert | 0.551 | 🔺 Rising |
| 2026-10-09 17:04:42 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.070 |  |
| 2026-10-09 17:04:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-09 17:03:55 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | -0.051 |  |
| 2026-10-09 17:03:52 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-10-09 17:03:46 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.061 |  |
| 2026-10-09 17:03:36 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-09 17:03:27 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-10-09 17:02:55 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:02:36 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:02:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:02:20 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.137 |  |
| 2026-10-09 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | -0.080 |  |
| 2026-10-09 17:02:15 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-09 17:02:14 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-09 17:02:07 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 17:02:04 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:01:50 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-09 17:01:17 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 17:01:08 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.568 | 🔺 Rising |
| 2026-10-09 17:01:04 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-09 17:00:32 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-09 17:00:32 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.011 |  |
| 2026-10-09 17:00:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:58:26 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 17:04:46 | Norwood (Kelani Ganga) | 1.58 | 🟡 Alert | 0.551 | 🔺 Rising |
| 2026-10-09 17:01:08 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.568 | 🔺 Rising |
| 2026-10-09 17:03:27 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-10-09 17:08:01 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-10-09 17:05:28 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-09 17:02:14 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-09 17:02:15 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-09 17:03:36 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-09 17:06:08 | Urawa (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-09 17:07:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-09 17:01:04 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-09 17:01:50 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-09 17:00:32 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-09 17:11:09 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-09 17:01:17 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 17:07:10 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 17:02:07 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 17:02:36 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:00:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:02:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:13:49 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:02:04 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:06:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:02:55 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-09 17:04:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-09 17:00:32 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.011 |  |
| 2026-10-09 17:05:53 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2026-10-09 17:07:43 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.028 |  |
| 2026-10-09 17:03:52 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-10-09 17:10:05 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.032 |  |
| 2026-10-09 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.039 |  |
| 2026-10-09 17:04:58 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-10-09 17:03:55 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | -0.051 |  |
| 2026-10-09 17:04:59 | Giriulla (Maha Oya) | 2.92 | 🟢 Normal | -0.059 |  |
| 2026-10-09 17:03:46 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.061 |  |
| 2026-10-09 17:04:42 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.070 |  |
| 2026-10-09 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | -0.080 |  |
| 2026-10-09 17:06:10 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.109 |  |
| 2026-10-09 17:02:20 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)