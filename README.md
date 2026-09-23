# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_01:32:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,236 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 01:32:25 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.018 |  |
| 2026-09-24 01:19:44 | Rathnapura (Kalu Ganga) | 4.33 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-24 01:13:02 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-09-24 01:08:55 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:08:20 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-09-24 01:08:11 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-24 01:07:03 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 01:06:38 | Nawalapitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.058 |  |
| 2026-09-24 01:06:24 | Holombuwa (Kelani Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-24 01:06:08 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:05:45 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:05:12 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 01:04:49 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-24 01:04:42 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:04:21 | Urawa (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.485 | 🔺 Rising |
| 2026-09-24 01:04:03 | Peradeniya (Mahaweli Ganga) | 4.08 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-24 01:03:48 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-09-24 01:03:46 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:33 | Thawalama (Gin Ganga) | 4.14 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-09-24 01:03:25 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-24 01:03:15 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-09-24 01:03:06 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-24 01:02:53 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:41 | Glencourse (Kelani Ganga) | 12.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 01:02:36 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:08 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 01:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.83 | 🟠 Minor Flood | -0.034 |  |
| 2026-09-24 01:01:14 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 01:00:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:00:18 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 01:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.83 | 🟠 Minor Flood | -0.034 |  |
| 2026-09-24 01:03:33 | Thawalama (Gin Ganga) | 4.14 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-09-24 01:13:02 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-09-24 01:04:21 | Urawa (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.485 | 🔺 Rising |
| 2026-09-24 01:08:20 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-09-24 01:08:11 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-24 00:09:31 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-24 01:04:03 | Peradeniya (Mahaweli Ganga) | 4.08 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-24 01:02:41 | Glencourse (Kelani Ganga) | 12.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 01:03:25 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-24 01:04:49 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-24 00:01:32 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 01:03:06 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-24 01:05:12 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 01:01:14 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 01:19:44 | Rathnapura (Kalu Ganga) | 4.33 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-24 01:07:03 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 01:02:08 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 01:02:08 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:00:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:36 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:53 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:06:08 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:02:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:05:45 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:08:55 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:04:42 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 01:03:46 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-24 01:03:48 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-09-24 01:06:24 | Holombuwa (Kelani Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-24 01:32:25 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.018 |  |
| 2026-09-24 01:03:15 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 01:00:18 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-09-24 01:06:38 | Nawalapitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)