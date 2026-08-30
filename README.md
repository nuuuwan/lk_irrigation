# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_19:22:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,414 measurements** from **39** stations.
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
| 2026-08-30 19:22:45 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-30 19:15:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.016 |  |
| 2026-08-30 19:14:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.049 |  |
| 2026-08-30 19:14:08 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.008 |  |
| 2026-08-30 19:13:57 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.008 |  |
| 2026-08-30 19:10:12 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-08-30 19:08:46 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.036 |  |
| 2026-08-30 19:06:59 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-30 19:06:38 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:06:36 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:06:12 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-08-30 19:05:51 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-30 19:05:45 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:05:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:04:36 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-30 19:04:22 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:04:00 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:03:50 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.023 |  |
| 2026-08-30 19:03:35 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:03:29 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 12.185 | 🔺 Rising |
| 2026-08-30 19:03:29 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 19:03:20 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-08-30 19:02:42 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:02:40 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:02:03 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:02:00 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:46 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-08-30 19:01:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |
| 2026-08-30 19:01:42 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-08-30 19:01:25 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:21 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:19 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 12.185 | 🔺 Rising |
| 2026-08-30 19:01:11 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:00:37 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:00:28 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 19:03:29 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 12.185 | 🔺 Rising |
| 2026-08-30 19:01:42 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-08-30 19:04:36 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-30 19:06:59 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-30 19:03:29 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 19:22:45 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-30 18:04:01 | Weraganthota (Mahaweli Ganga) | -3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 19:05:51 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-30 19:00:37 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:02:03 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:05:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:05:45 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:11 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:13 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:02:42 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:25 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:03:35 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:04:00 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:02:40 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:06:38 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:04:47 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:01:21 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:06:36 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:02:00 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:04:22 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 19:14:08 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.008 |  |
| 2026-08-30 19:13:57 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.008 |  |
| 2026-08-30 19:03:20 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-08-30 19:00:28 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-30 19:10:12 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-08-30 19:01:46 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-08-30 19:15:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.016 |  |
| 2026-08-30 19:03:50 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.023 |  |
| 2026-08-30 19:08:46 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.036 |  |
| 2026-08-30 19:06:12 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-08-30 19:14:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.049 |  |
| 2026-08-30 19:01:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)