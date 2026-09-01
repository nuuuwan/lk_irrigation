# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_17:21:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,113 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 17:21:35 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:20:03 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:16:48 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-01 17:13:31 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-01 17:12:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:10:58 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 17:08:20 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:07:42 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.026 |  |
| 2026-09-01 17:06:30 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:06:25 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:06:23 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-01 17:06:04 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 17:05:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:04:56 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:04:44 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | -0.012 |  |
| 2026-09-01 17:04:41 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:04:35 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:04:13 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:04:02 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-09-01 17:03:40 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-01 17:03:28 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:03:14 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:03:12 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.030 |  |
| 2026-09-01 17:02:59 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:56 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.052 |  |
| 2026-09-01 17:02:36 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:15 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:02:00 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.013 |  |
| 2026-09-01 17:01:57 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:01:43 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:38 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:36 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.060 |  |
| 2026-09-01 17:01:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:04 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:51 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 17:13:31 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-01 17:16:48 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-01 17:03:40 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-01 17:06:23 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-01 17:10:58 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 17:06:04 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 17:05:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:04:13 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:38 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:03:28 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:57 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:20:03 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:59 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:03:12 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:04 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:21:35 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:04:41 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:12:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:04:56 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:06:25 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:51 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:02:36 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:43 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:03:14 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:02:15 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:06:30 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:04:35 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-01 17:04:44 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | -0.012 |  |
| 2026-09-01 17:02:00 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.013 |  |
| 2026-09-01 17:04:02 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-09-01 17:07:42 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.026 |  |
| 2026-09-01 17:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.030 |  |
| 2026-09-01 17:02:56 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.052 |  |
| 2026-09-01 17:01:36 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)