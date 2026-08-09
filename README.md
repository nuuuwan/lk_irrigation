# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_16:12:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,896 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 16:12:42 | Peradeniya (Mahaweli Ganga) | 3.63 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:07:59 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:07:27 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:07:24 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-08-09 16:06:39 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:06:00 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:05:57 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-08-09 16:05:53 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.041 |  |
| 2026-08-09 16:04:54 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-08-09 16:04:50 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 16:04:43 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:04:40 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:04:31 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-09 16:04:26 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:03:38 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:03:22 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-08-09 16:03:16 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-09 16:03:13 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-08-09 16:02:56 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:02:45 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:02:27 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:02:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-08-09 16:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:01:56 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:01:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:01:47 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.021 |  |
| 2026-08-09 16:01:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:01:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:01:23 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.077 |  |
| 2026-08-09 16:01:21 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.070 |  |
| 2026-08-09 16:01:21 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.183 |  |
| 2026-08-09 16:01:15 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:00:41 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:00:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 16:07:24 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-08-09 16:04:54 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-08-09 16:03:16 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-09 16:04:50 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 16:01:15 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:04:40 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:01:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:01:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 16:01:56 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:00:41 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:06:39 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:04:26 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:01:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:06:00 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:05:53 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:00:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:02:45 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:03:38 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:07:59 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:07:27 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:04:43 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:12:42 | Peradeniya (Mahaweli Ganga) | 3.63 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:05:15 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:11:59 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 16:02:56 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:27 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.005 |  |
| 2026-08-09 16:05:57 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-08-09 16:03:22 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-08-09 16:04:31 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-09 16:03:13 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-08-09 16:01:47 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.021 |  |
| 2026-08-09 16:02:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-08-09 16:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.041 |  |
| 2026-08-09 15:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.042 |  |
| 2026-08-09 16:01:21 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.070 |  |
| 2026-08-09 16:01:23 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.077 |  |
| 2026-08-09 16:01:21 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)