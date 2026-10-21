# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_15:07:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,087 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 15:07:35 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:06:48 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.048 |  |
| 2026-10-21 15:06:19 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:53 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-10-21 15:05:38 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:28 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:22 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:11 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 15:05:00 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:53 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:40 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:36 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:14 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-21 15:04:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-10-21 15:03:20 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:03:16 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-21 15:03:13 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 15:03:10 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-10-21 15:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.100 |  |
| 2026-10-21 15:03:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-10-21 15:02:46 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:02:35 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-10-21 15:02:30 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-10-21 15:02:25 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.050 |  |
| 2026-10-21 15:02:19 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 15:02:15 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.010 |  |
| 2026-10-21 15:02:14 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-21 15:02:10 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-21 15:02:03 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.013 |  |
| 2026-10-21 15:01:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 15:01:16 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.089 |  |
| 2026-10-21 15:00:46 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:00:38 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:00:32 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-21 15:00:15 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.280 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 15:05:53 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-10-21 15:04:14 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-21 15:00:32 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-21 15:02:19 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 15:05:11 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 15:01:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 15:00:38 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:02:10 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:01:35 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:38 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:00:46 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:53 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:06:19 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:36 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:22 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:00 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:28 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:03:20 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:40 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:07:35 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:02:46 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-10-21 14:05:50 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.009 |  |
| 2026-10-21 15:03:16 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-21 15:02:15 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.010 |  |
| 2026-10-21 15:03:13 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 15:02:03 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.013 |  |
| 2026-10-21 15:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-21 15:03:10 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-10-21 15:03:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-10-21 15:02:30 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-10-21 14:04:12 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.037 |  |
| 2026-10-21 15:06:48 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.048 |  |
| 2026-10-21 15:02:14 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-21 15:02:35 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-10-21 15:02:25 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.050 |  |
| 2026-10-21 15:01:16 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.089 |  |
| 2026-10-21 15:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.100 |  |
| 2026-10-21 15:00:15 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.280 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)