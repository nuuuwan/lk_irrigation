# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_23:31:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 23:31:10 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:18:46 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-01 23:12:49 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:10:30 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-11-01 23:08:40 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-01 23:08:08 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-01 23:07:04 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 23:06:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-11-01 23:06:18 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-01 23:06:15 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 23:04:32 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-11-01 23:04:31 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-11-01 23:04:13 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:03:54 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.239 |  |
| 2026-11-01 23:03:39 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:03:27 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2026-11-01 23:03:26 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-01 23:03:14 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-01 23:02:52 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-01 23:02:27 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:02:22 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-01 23:02:12 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:02:12 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-01 23:01:45 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:01:39 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-11-01 23:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-01 23:01:29 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:01:27 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-01 23:01:26 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | -0.020 |  |
| 2026-11-01 23:01:21 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-11-01 23:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.049 |  |
| 2026-11-01 23:00:53 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:00:34 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:48:42 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.055 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 23:01:39 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-11-01 23:03:27 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2026-11-01 23:03:14 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-01 23:03:26 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-01 23:02:12 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-01 23:08:40 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-01 23:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-01 22:48:42 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-01 23:01:27 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-01 23:06:15 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 23:02:22 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-01 23:18:46 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-01 23:06:18 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-01 23:07:04 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 23:00:34 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:04:13 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:01:29 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:12:49 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:31:10 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:02:27 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:02:12 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:00:53 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:03:39 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:09:09 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:01:45 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-01 23:08:08 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:02:44 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 23:02:52 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-01 23:04:32 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-11-01 23:01:26 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | -0.020 |  |
| 2026-11-01 23:10:30 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-11-01 23:01:21 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-11-01 23:04:31 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 23:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.049 |  |
| 2026-11-01 23:06:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-11-01 23:03:54 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)