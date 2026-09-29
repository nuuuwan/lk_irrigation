# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_17:06:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 17:06:36 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.076 |  |
| 2026-09-29 17:05:40 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 17:05:37 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:04:47 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.024 |  |
| 2026-09-29 17:04:38 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 17:04:13 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:04:04 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:03:52 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:03:38 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 17:03:30 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 17:03:05 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | -0.040 |  |
| 2026-09-29 17:03:03 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-09-29 17:03:00 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:02:54 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.042 |  |
| 2026-09-29 17:02:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:02:39 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-29 17:02:12 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:02:12 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:02:12 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-09-29 17:01:48 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-09-29 17:01:45 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-29 17:01:38 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:01:34 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.167 |  |
| 2026-09-29 17:01:23 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:00:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.092 |  |
| 2026-09-29 17:00:52 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:00:46 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:00:20 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 17:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 17:01:45 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-29 17:02:39 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-29 17:04:38 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 17:05:40 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 17:03:38 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 17:03:30 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 17:00:20 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 17:00:52 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:02:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:15:01 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:01:23 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:08:21 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:53 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:11:36 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:02:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:00:46 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:04:13 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:02:12 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:03:00 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:08:01 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:10:28 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:06:20 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:02:12 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:03:52 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:04:04 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:05:37 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-29 17:04:47 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.024 |  |
| 2026-09-29 16:11:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.027 |  |
| 2026-09-29 17:02:12 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-09-29 16:05:43 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.038 |  |
| 2026-09-29 17:03:05 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | -0.040 |  |
| 2026-09-29 17:03:03 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-09-29 17:01:48 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-09-29 17:02:54 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.042 |  |
| 2026-09-29 17:06:36 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.076 |  |
| 2026-09-29 17:00:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.092 |  |
| 2026-09-29 17:01:34 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)