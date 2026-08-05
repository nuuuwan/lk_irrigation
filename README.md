# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_20:12:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,873 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 20:12:59 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:11:19 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.035 |  |
| 2026-08-05 20:10:11 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:10:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.045 |  |
| 2026-08-05 20:09:38 | Rathnapura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.103 |  |
| 2026-08-05 20:09:30 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.018 |  |
| 2026-08-05 20:06:59 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-08-05 20:06:04 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:06:00 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:05:50 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:05:25 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.037 |  |
| 2026-08-05 20:05:16 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-08-05 20:05:10 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:05:04 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:04:42 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:03:58 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-05 20:03:57 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.051 |  |
| 2026-08-05 20:03:40 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-05 20:03:37 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:03:37 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.048 |  |
| 2026-08-05 20:03:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-05 20:03:30 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:03:24 | Kithulgala (Kelani Ganga) | 2.62 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-08-05 20:03:21 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.072 |  |
| 2026-08-05 20:03:19 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:03:01 | Peradeniya (Mahaweli Ganga) | 6.24 | 🟡 Alert | -0.213 |  |
| 2026-08-05 20:02:58 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:02:42 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:02:21 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-08-05 20:02:16 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 20:01:56 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 20:01:51 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-05 20:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:01:20 | Nawalapitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:00:22 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 20:03:01 | Peradeniya (Mahaweli Ganga) | 6.24 | 🟡 Alert | -0.213 |  |
| 2026-08-05 20:03:24 | Kithulgala (Kelani Ganga) | 2.62 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-08-05 20:03:58 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-05 20:01:56 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 20:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 20:01:51 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-05 20:03:30 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:06:04 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:02:16 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:03:37 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:12:59 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:03:19 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:04:42 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:05:10 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:10:11 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:06:00 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:02:58 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:05:50 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 20:06:59 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-08-05 20:03:40 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 20:03:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-05 20:02:21 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-08-05 20:09:30 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.018 |  |
| 2026-08-05 20:01:20 | Nawalapitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:02:42 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:05:04 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:00:22 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:05:16 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-08-05 20:11:19 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.035 |  |
| 2026-08-05 20:05:25 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.037 |  |
| 2026-08-05 20:10:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.045 |  |
| 2026-08-05 20:03:37 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.048 |  |
| 2026-08-05 20:03:57 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.051 |  |
| 2026-08-05 20:03:21 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.072 |  |
| 2026-08-05 20:09:38 | Rathnapura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)