# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_03:17:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 03:17:14 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-08-24 03:14:32 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:12:22 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:10:58 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-08-24 03:08:21 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:08:21 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 03:07:56 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-24 03:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-24 03:07:28 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:06:29 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:05:50 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-08-24 03:05:28 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.132 |  |
| 2026-08-24 03:04:52 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-24 03:04:40 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 03:04:35 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-24 03:04:24 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:04:24 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:04:01 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:03:58 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:03:25 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-24 03:03:19 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:03:15 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-08-24 03:02:58 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:02:49 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-24 03:02:46 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:02:44 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.005 |  |
| 2026-08-24 03:02:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:56 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:49 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:27 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 03:01:03 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:00:18 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 02:56:00 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 03:02:49 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-24 03:07:56 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-24 02:01:42 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-24 03:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-24 03:04:52 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-24 03:04:40 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 03:01:27 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 03:08:21 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 03:08:21 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:00:18 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:49 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:04:57 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:07:28 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:02:46 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:02:58 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:12:22 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:03:19 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:02:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 02:01:53 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:56 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:03 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:03:58 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:06:29 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:01:26 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:04:24 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:14:32 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 02:08:30 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:03:15 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:02:44 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.005 |  |
| 2026-08-24 03:17:14 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-08-24 03:10:58 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-08-24 03:03:25 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-24 03:04:35 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-24 03:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-08-24 03:05:50 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-08-24 03:05:28 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)