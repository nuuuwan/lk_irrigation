# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_14:12:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,659 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 14:12:51 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.057 |  |
| 2026-08-20 14:11:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:11:23 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:10:59 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:10:01 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:09:46 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-08-20 14:09:10 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 14:08:53 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.028 |  |
| 2026-08-20 14:08:47 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 14:08:03 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:07:55 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.018 |  |
| 2026-08-20 14:07:07 | Rathnapura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-20 14:05:22 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:05:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:05:19 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -1.532 |  |
| 2026-08-20 14:04:32 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-08-20 14:04:23 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:18 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-08-20 14:04:13 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:12 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:54 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:35 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:20 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:08 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:07 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.106 |  |
| 2026-08-20 14:02:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-20 14:02:36 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 14:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-20 14:02:36 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:02:13 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-20 14:02:11 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -1.532 |  |
| 2026-08-20 14:02:09 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:01:57 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-20 14:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:00:27 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:59:53 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:31:55 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 14:04:32 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-08-20 14:07:07 | Rathnapura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-20 14:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-20 14:02:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-20 13:31:55 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-20 13:05:04 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-20 14:08:47 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 14:02:36 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 14:09:10 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 13:59:53 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:02:09 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:00:27 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:02:36 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:10:59 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:10:01 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:35 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:11:23 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:11:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:08 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:05:22 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:03:54 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:13 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:05:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:23 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:12 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:08:03 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:01:57 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 14:04:18 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-08-20 14:02:13 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-20 14:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-20 14:07:55 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.018 |  |
| 2026-08-20 13:18:12 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-08-20 14:08:53 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.028 |  |
| 2026-08-20 14:09:46 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-08-20 14:12:51 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.057 |  |
| 2026-08-20 14:03:07 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.106 |  |
| 2026-08-20 14:05:19 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -1.532 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)