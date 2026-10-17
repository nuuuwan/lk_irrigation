# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_15:05:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,460 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 15:05:03 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-17 15:04:44 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-17 15:04:37 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.067 |  |
| 2026-10-17 15:04:36 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-17 15:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.67 | 🟡 Alert | -0.029 |  |
| 2026-10-17 15:04:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.108 |  |
| 2026-10-17 15:04:22 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.021 |  |
| 2026-10-17 15:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-17 15:04:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 15:04:05 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-10-17 15:03:36 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-17 15:03:20 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-17 15:03:15 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.099 |  |
| 2026-10-17 15:03:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-17 15:03:07 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 15:02:52 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-10-17 15:02:46 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-17 15:02:42 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-17 15:02:36 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-10-17 15:02:18 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-10-17 15:02:06 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-10-17 15:01:59 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 15:01:44 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-10-17 15:01:41 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-10-17 15:01:26 | Thanthirimale (Malwathu Oya) | 2.51 | 🟢 Normal | -0.030 |  |
| 2026-10-17 15:01:25 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 15:01:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 15:01:08 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 15:01:00 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 15:01:00 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 15:04:44 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-17 15:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.67 | 🟡 Alert | -0.029 |  |
| 2026-10-17 15:03:36 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-17 15:04:36 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-17 15:02:42 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-17 15:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-17 15:01:59 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 15:03:07 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 15:01:08 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 15:04:05 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-10-17 15:01:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 15:01:25 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 15:03:20 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-17 15:02:46 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:02:16 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-17 15:03:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:00:49 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:04:41 | Baddegama (Gin Ganga) | 3.36 | 🟢 Normal | -0.011 |  |
| 2026-10-17 15:02:52 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-10-17 14:05:41 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-17 15:02:36 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-10-17 14:05:37 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-10-17 15:02:06 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-10-17 15:04:22 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.021 |  |
| 2026-10-17 15:05:03 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-17 15:01:26 | Thanthirimale (Malwathu Oya) | 2.51 | 🟢 Normal | -0.030 |  |
| 2026-10-17 15:02:18 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-10-17 15:01:41 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-10-17 14:01:38 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-17 15:04:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 14:01:04 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-10-17 15:01:44 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-10-17 14:04:24 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.053 |  |
| 2026-10-17 15:04:37 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.067 |  |
| 2026-10-17 14:10:32 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.070 |  |
| 2026-10-17 15:03:15 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.099 |  |
| 2026-10-17 15:04:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.108 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)