# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_20:18:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,281 measurements** from **39** stations.
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
| 2026-10-21 20:18:05 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:16:47 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-10-21 20:15:37 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-21 20:13:25 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-21 20:10:20 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-10-21 20:09:33 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 20:08:52 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-21 20:08:50 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 20:07:54 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-21 20:07:41 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 20:07:31 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.009 |  |
| 2026-10-21 20:06:55 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:06:15 | Wellawaya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.165 |  |
| 2026-10-21 20:06:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-10-21 20:06:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-21 20:05:41 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.038 |  |
| 2026-10-21 20:05:36 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-21 20:04:55 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:04:44 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 20:04:39 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 20:04:11 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | -0.239 |  |
| 2026-10-21 20:04:08 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.055 |  |
| 2026-10-21 20:03:33 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:03:31 | Nawalapitiya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.236 |  |
| 2026-10-21 20:03:17 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.275 |  |
| 2026-10-21 20:03:01 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:02:56 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 20:02:49 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | -0.020 |  |
| 2026-10-21 20:02:45 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-10-21 20:02:37 | Yaka Wewa (Ma Oya) | 1.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 20:02:36 | Deraniyagala (Kelani Ganga) | 2.97 | 🟢 Normal | -0.362 |  |
| 2026-10-21 20:02:07 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.057 |  |
| 2026-10-21 20:01:17 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-21 20:01:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 20:08:52 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-21 20:16:47 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-21 20:01:17 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-21 20:13:25 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-21 20:07:54 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-21 20:15:37 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-21 20:06:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-21 20:02:37 | Yaka Wewa (Ma Oya) | 1.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 20:04:39 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 20:04:44 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 20:07:41 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 20:08:50 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 20:02:56 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 19:05:52 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 20:09:33 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 20:03:33 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:02:07 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:18:05 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:04:55 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:01:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:03:01 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 20:07:31 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.009 |  |
| 2026-10-21 20:02:45 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-10-21 20:05:36 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-21 20:10:20 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-10-21 20:02:49 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | -0.020 |  |
| 2026-10-21 20:06:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-10-21 20:05:41 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.038 |  |
| 2026-10-21 20:04:08 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.055 |  |
| 2026-10-21 20:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.057 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-21 20:06:15 | Wellawaya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.165 |  |
| 2026-10-21 20:03:31 | Nawalapitiya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.236 |  |
| 2026-10-21 20:04:11 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | -0.239 |  |
| 2026-10-21 20:03:17 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.275 |  |
| 2026-10-21 20:02:36 | Deraniyagala (Kelani Ganga) | 2.97 | 🟢 Normal | -0.362 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)