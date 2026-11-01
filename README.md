# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_22:26:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,246 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 22:26:59 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:17:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:17:48 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | -0.030 |  |
| 2026-11-01 22:12:31 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:12:16 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.008 |  |
| 2026-11-01 22:11:32 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.028 |  |
| 2026-11-01 22:10:46 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 22:09:09 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:08:35 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-01 22:07:51 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-11-01 22:06:59 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-11-01 22:06:21 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:06:08 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-01 22:06:08 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 22:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-01 22:04:59 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:04:47 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-01 22:04:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:04:27 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:03:46 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 22:03:42 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-11-01 22:03:17 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:02:58 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-11-01 22:02:52 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:02:44 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:02:21 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-01 22:02:18 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 22:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:01:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:01:12 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.021 |  |
| 2026-11-01 22:01:03 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-01 22:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.061 |  |
| 2026-11-01 22:00:23 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 22:17:48 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | -0.030 |  |
| 2026-11-01 22:02:58 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-11-01 22:06:59 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-11-01 22:03:42 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-11-01 22:04:47 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-01 22:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-01 21:16:30 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-01 22:06:08 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-01 22:08:35 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 22:06:08 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 22:02:18 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 22:02:21 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-01 22:03:46 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 21:02:21 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 22:10:46 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 22:02:52 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:26:59 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:17:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:04:27 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:03:17 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:12:31 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:04:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:09:09 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:06:21 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:10:39 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:04:59 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:12:16 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.008 |  |
| 2026-11-01 22:02:44 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:01:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:01:03 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-01 22:01:12 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.021 |  |
| 2026-11-01 22:11:32 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.028 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 22:07:51 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-11-01 22:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.061 |  |
| 2026-11-01 22:00:23 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)