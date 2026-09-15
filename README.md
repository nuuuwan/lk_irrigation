# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_21:04:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,873 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 21:04:57 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-15 21:04:56 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 21:04:47 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.030 |  |
| 2026-09-15 21:04:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:04:20 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 21:04:18 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.034 |  |
| 2026-09-15 21:04:16 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-15 21:04:16 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.054 |  |
| 2026-09-15 21:04:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:46 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-15 21:03:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:32 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:25 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 1.039 | 🔺 Rising |
| 2026-09-15 21:03:12 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:01 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 21:02:50 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.092 |  |
| 2026-09-15 21:02:36 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-09-15 21:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:02:23 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.106 |  |
| 2026-09-15 21:02:22 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-15 21:02:19 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-15 21:02:16 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:01:45 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-15 21:01:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:00:15 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | -0.103 |  |
| 2026-09-15 21:00:14 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 21:00:15 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | -0.103 |  |
| 2026-09-15 21:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 1.039 | 🔺 Rising |
| 2026-09-15 20:13:21 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-09-15 21:02:22 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-15 21:01:45 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-15 21:04:16 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-15 21:04:20 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 20:06:59 | Baddegama (Gin Ganga) | 3.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 21:04:56 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 21:03:01 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 20:04:27 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:02:16 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:32 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:12 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:25 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:03:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:04:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:04:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:01:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 20:09:58 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-15 21:04:57 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-15 20:18:25 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.018 |  |
| 2026-09-15 21:03:46 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-15 21:00:14 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-09-15 21:02:19 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-15 20:06:17 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-09-15 21:04:47 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.030 |  |
| 2026-09-15 21:02:36 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-09-15 21:04:18 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.034 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-15 21:04:16 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.054 |  |
| 2026-09-15 20:03:58 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.074 |  |
| 2026-09-15 20:01:38 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.083 |  |
| 2026-09-15 21:02:50 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.092 |  |
| 2026-09-15 21:02:23 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.106 |  |
| 2026-09-15 20:05:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)