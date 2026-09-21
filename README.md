# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_03:31:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 03:31:33 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -72.000 |  |
| 2026-09-22 03:31:31 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -72.000 |  |
| 2026-09-22 03:09:15 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.074 |  |
| 2026-09-22 03:09:10 | Hanwella (Kelani Ganga) | 5.02 | 🟢 Normal | -0.091 |  |
| 2026-09-22 03:08:03 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-09-22 03:08:01 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 03:07:09 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-09-22 03:06:35 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 03:06:19 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-09-22 03:05:48 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-22 03:05:45 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:05:39 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-09-22 03:04:56 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-22 03:04:49 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -6.667 |  |
| 2026-09-22 03:04:47 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -180.000 |  |
| 2026-09-22 03:04:44 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | -180.000 |  |
| 2026-09-22 03:04:40 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.069 |  |
| 2026-09-22 03:04:22 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -6.667 |  |
| 2026-09-22 03:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.18 | 🟠 Minor Flood | 0.069 | 🔺 Rising |
| 2026-09-22 03:03:35 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:03:27 | Glencourse (Kelani Ganga) | 12.44 | 🟢 Normal | -0.111 |  |
| 2026-09-22 03:03:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-09-22 03:03:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:03:12 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:03:05 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:03:01 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -2.769 |  |
| 2026-09-22 03:02:35 | Deraniyagala (Kelani Ganga) | 1.49 | 🟢 Normal | -2.769 |  |
| 2026-09-22 03:02:25 | Ellagawa (Kalu Ganga) | 9.02 | 🟢 Normal | -0.010 |  |
| 2026-09-22 03:02:21 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.035 |  |
| 2026-09-22 03:02:14 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-22 03:02:12 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:01:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-22 03:01:45 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-22 03:01:33 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-09-22 03:01:28 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.023 |  |
| 2026-09-22 03:01:20 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 02:54:40 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:51:44 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 03:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.18 | 🟠 Minor Flood | 0.069 | 🔺 Rising |
| 2026-09-22 03:05:48 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-22 03:06:35 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 03:02:21 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.035 |  |
| 2026-09-22 03:04:47 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -180.000 |  |
| 2026-09-22 03:08:03 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-09-22 03:01:33 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-09-22 03:04:56 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-22 03:02:14 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-22 03:01:20 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 03:08:01 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 03:03:12 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:03:05 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:01:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:03:35 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:03:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:12 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:05:45 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:01:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-22 03:02:25 | Ellagawa (Kalu Ganga) | 9.02 | 🟢 Normal | -0.010 |  |
| 2026-09-22 03:01:45 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-22 03:07:09 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-09-22 03:06:19 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-22 03:05:39 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-22 03:01:28 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.023 |  |
| 2026-09-22 03:03:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-09-22 03:04:40 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.069 |  |
| 2026-09-22 03:09:15 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.074 |  |
| 2026-09-22 03:09:10 | Hanwella (Kelani Ganga) | 5.02 | 🟢 Normal | -0.091 |  |
| 2026-09-22 03:03:27 | Glencourse (Kelani Ganga) | 12.44 | 🟢 Normal | -0.111 |  |
| 2026-09-22 03:03:01 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -2.769 |  |
| 2026-09-22 03:04:49 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -6.667 |  |
| 2026-09-22 03:31:33 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)