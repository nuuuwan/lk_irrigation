# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_03:31:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,150 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 03:31:15 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-05 03:21:12 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-05 03:15:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.108 |  |
| 2026-11-05 03:13:38 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.141 |  |
| 2026-11-05 03:09:49 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-05 03:08:13 | Thanamalwila (Kirindi Oya) | 2.91 | 🟢 Normal | -0.253 |  |
| 2026-11-05 03:07:19 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.144 |  |
| 2026-11-05 03:07:01 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-11-05 03:06:56 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-05 03:05:59 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.048 |  |
| 2026-11-05 03:04:56 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:04:47 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-05 03:04:36 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-05 03:04:02 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.077 |  |
| 2026-11-05 03:03:38 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 03:03:27 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:02:51 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-05 03:02:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.884 |  |
| 2026-11-05 03:02:27 | Dunamale (Aththanagalu Oya) | 3.07 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-05 03:02:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:02:01 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:01:52 | Moragaswewa (Deduru Oya) | 3.92 | 🟢 Normal | -0.070 |  |
| 2026-11-05 03:01:50 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-11-05 03:01:43 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-11-05 03:01:31 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.101 |  |
| 2026-11-05 03:01:30 | Kuda Oya (Kirindi Oya) | 3.70 | 🟢 Normal | -0.302 |  |
| 2026-11-05 03:01:10 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:00:58 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.021 |  |
| 2026-11-05 03:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 03:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.023 |  |
| 2026-11-05 02:04:19 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.578 | 🔺 Rising |
| 2026-11-05 03:09:49 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-05 03:04:47 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-05 02:11:57 | Urawa (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-05 03:02:27 | Dunamale (Aththanagalu Oya) | 3.07 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-05 03:06:56 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-05 01:07:28 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 03:21:12 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-05 03:31:15 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-05 03:03:38 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 02:06:12 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 03:03:27 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:03:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:02:01 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:01:10 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:08:57 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:02:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:04:56 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:00:28 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:07:01 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-11-05 03:04:36 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-05 03:02:51 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-05 03:01:43 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-11-05 03:00:58 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.021 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-05 03:01:50 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 03:05:59 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.048 |  |
| 2026-11-05 03:01:52 | Moragaswewa (Deduru Oya) | 3.92 | 🟢 Normal | -0.070 |  |
| 2026-11-05 03:04:02 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.077 |  |
| 2026-11-05 03:01:31 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.101 |  |
| 2026-11-05 03:15:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.108 |  |
| 2026-11-05 03:13:38 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.141 |  |
| 2026-11-05 03:07:19 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.144 |  |
| 2026-11-05 03:08:13 | Thanamalwila (Kirindi Oya) | 2.91 | 🟢 Normal | -0.253 |  |
| 2026-11-05 03:01:30 | Kuda Oya (Kirindi Oya) | 3.70 | 🟢 Normal | -0.302 |  |
| 2026-11-05 03:02:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.884 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)