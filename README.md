# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_05:22:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,556 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 05:22:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-09-22 05:18:10 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2026-09-22 05:18:00 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 05:14:53 | Holombuwa (Kelani Ganga) | 2.45 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-22 05:13:18 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 05:12:56 | Rathnapura (Kalu Ganga) | 4.80 | 🟢 Normal | -0.068 |  |
| 2026-09-22 05:10:37 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.034 |  |
| 2026-09-22 05:09:20 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-22 05:08:18 | Panadugama (Nilwala Ganga) | 5.14 | 🟡 Alert | -0.040 |  |
| 2026-09-22 05:07:06 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.039 |  |
| 2026-09-22 05:06:35 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | -0.028 |  |
| 2026-09-22 05:05:54 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-22 05:05:15 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.464 |  |
| 2026-09-22 05:04:44 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.069 |  |
| 2026-09-22 05:04:36 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.032 |  |
| 2026-09-22 05:04:23 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-22 05:04:09 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.030 |  |
| 2026-09-22 05:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:19 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.122 |  |
| 2026-09-22 05:03:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:06 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.119 |  |
| 2026-09-22 05:02:53 | Siyambalanduwa (Heda Oya) | 0.00 | 🟢 Normal | -0.157 |  |
| 2026-09-22 05:02:45 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:02:16 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | -0.102 |  |
| 2026-09-22 05:02:15 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-22 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-09-22 05:01:44 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:31 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.005 |  |
| 2026-09-22 05:01:22 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-22 05:01:21 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:00:59 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.000 |  |
| 2026-09-22 05:00:51 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.045 |  |
| 2026-09-22 05:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:00:34 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 05:22:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-09-22 05:13:18 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 05:00:59 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.000 |  |
| 2026-09-22 05:18:00 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 05:08:18 | Panadugama (Nilwala Ganga) | 5.14 | 🟡 Alert | -0.040 |  |
| 2026-09-22 05:14:53 | Holombuwa (Kelani Ganga) | 2.45 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-22 05:05:54 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-22 05:01:22 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-22 05:09:20 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-22 05:04:23 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-22 05:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:02:45 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:21 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:44 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:31 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.005 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-22 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-09-22 05:06:35 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | -0.028 |  |
| 2026-09-22 05:04:09 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.030 |  |
| 2026-09-22 05:02:15 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-22 05:18:10 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2026-09-22 05:04:36 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.032 |  |
| 2026-09-22 05:10:37 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.034 |  |
| 2026-09-22 05:07:06 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.039 |  |
| 2026-09-22 05:00:51 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.045 |  |
| 2026-09-22 05:12:56 | Rathnapura (Kalu Ganga) | 4.80 | 🟢 Normal | -0.068 |  |
| 2026-09-22 05:04:44 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.069 |  |
| 2026-09-22 05:00:10 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.081 |  |
| 2026-09-22 05:02:16 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | -0.102 |  |
| 2026-09-22 05:03:06 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.119 |  |
| 2026-09-22 05:03:19 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.122 |  |
| 2026-09-22 05:02:53 | Siyambalanduwa (Heda Oya) | 0.00 | 🟢 Normal | -0.157 |  |
| 2026-09-22 05:05:15 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.464 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)