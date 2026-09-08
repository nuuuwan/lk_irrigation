# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_13:29:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 13:29:30 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:14:04 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:12:50 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.008 |  |
| 2026-09-08 13:11:54 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 13:10:51 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 13:09:42 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:09:35 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:09:31 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-08 13:07:30 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:07:24 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 13:06:36 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:05:43 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:04:35 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-08 13:03:59 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:03:52 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:03:42 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:03:21 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-08 13:03:12 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 13:02:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-08 13:02:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-08 13:02:44 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 13:02:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:02:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:02:33 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.031 |  |
| 2026-09-08 13:02:28 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 13:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-08 13:02:01 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:01:35 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-08 13:01:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:01:15 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:59 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:54 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:43 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:40 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:23 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:18 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-08 13:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 13:00:18 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-08 13:02:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-08 13:04:35 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-08 13:09:31 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-08 13:01:35 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-08 13:02:44 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 13:03:12 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 13:02:28 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 12:03:18 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 13:07:24 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 13:11:54 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 13:10:51 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 13:00:23 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:14:04 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:02:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:40 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:09:42 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:05:43 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:01:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:03:59 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:29:30 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:01:15 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:43 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:02:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:06:36 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:03:52 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:59 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:00:54 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:07:30 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:09:35 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:03:42 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:02:01 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-08 13:12:50 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.008 |  |
| 2026-09-08 13:02:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-08 13:03:21 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-08 13:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-08 13:02:33 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)