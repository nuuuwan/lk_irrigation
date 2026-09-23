# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_14:31:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 14:31:29 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:12:22 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:10:47 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-09-23 14:10:32 | Baddegama (Gin Ganga) | 3.73 | 🟡 Alert | -0.019 |  |
| 2026-09-23 14:10:01 | Thawalama (Gin Ganga) | 2.62 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-23 14:09:31 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 14:06:51 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:06:50 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | 0.000 |  |
| 2026-09-23 14:06:36 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.025 |  |
| 2026-09-23 14:06:15 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.012 |  |
| 2026-09-23 14:05:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:05:34 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:05:34 | Glencourse (Kelani Ganga) | 12.72 | 🟢 Normal | -0.030 |  |
| 2026-09-23 14:05:28 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:04:36 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:04:28 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:04:24 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-23 14:04:19 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.041 |  |
| 2026-09-23 14:04:11 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-23 14:04:07 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-23 14:03:50 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:03:47 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:03:36 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:03:27 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:03:20 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:03:09 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.024 |  |
| 2026-09-23 14:02:21 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.96 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 14:02:15 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.021 |  |
| 2026-09-23 14:02:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:02:01 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:01:59 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:01:15 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:01:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:00:25 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:00:18 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:00:17 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-23 13:59:01 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.96 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 14:06:50 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | 0.000 |  |
| 2026-09-23 14:10:32 | Baddegama (Gin Ganga) | 3.73 | 🟡 Alert | -0.019 |  |
| 2026-09-23 14:10:47 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-09-23 14:10:01 | Thawalama (Gin Ganga) | 2.62 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-23 14:04:24 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-23 14:04:11 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-23 14:00:17 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-23 14:04:07 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-23 13:59:01 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-23 14:09:31 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 14:00:25 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:03:27 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:01:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:12:22 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:05:34 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:03:47 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:02:21 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:02:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:05:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:01:59 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:03:50 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 14:06:51 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:01:15 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:03:20 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:00:18 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:04:28 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-09-23 14:06:15 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.012 |  |
| 2026-09-23 14:05:28 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:03:36 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:04:36 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:02:01 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:31:29 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-23 14:02:15 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.021 |  |
| 2026-09-23 14:03:09 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.024 |  |
| 2026-09-23 14:06:36 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.025 |  |
| 2026-09-23 14:05:34 | Glencourse (Kelani Ganga) | 12.72 | 🟢 Normal | -0.030 |  |
| 2026-09-23 14:04:19 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)