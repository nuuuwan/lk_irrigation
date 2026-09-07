# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_14:18:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,411 measurements** from **39** stations.
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
| 2026-09-07 14:18:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:15:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-09-07 14:11:00 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:10:30 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-09-07 14:10:15 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:10:08 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:08:30 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-07 14:07:58 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:07:56 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:07:50 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2026-09-07 14:07:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.075 |  |
| 2026-09-07 14:06:25 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:06:01 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:05:26 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:05:10 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:04:55 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 14:04:44 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:04:30 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:04:07 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:03:30 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:03:27 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:03:26 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:03:23 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-09-07 14:02:57 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 14:02:50 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:42 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-07 14:02:36 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:02:26 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:23 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:01:56 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:01:22 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.060 |  |
| 2026-09-07 14:00:57 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:56 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:45 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:41 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:21 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 14:08:30 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-07 14:02:42 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-07 14:02:57 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 14:04:55 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 14:03:27 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:26 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:10:15 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:01:56 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:56 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:04:30 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:11:00 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:21 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:23 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:10:08 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:07:56 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:06:25 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:05:10 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:03:30 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:50 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:02:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:04:07 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:45 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:00:57 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:04:44 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:06:01 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:18:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:05:26 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 14:15:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-09-07 14:03:26 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:02:36 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:07:58 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | -0.010 |  |
| 2026-09-07 14:10:30 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-09-07 14:03:23 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-09-07 14:07:50 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2026-09-07 14:01:22 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.060 |  |
| 2026-09-07 14:07:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)