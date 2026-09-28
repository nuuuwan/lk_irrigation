# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_23:38:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,652 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 23:38:07 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.033 |  |
| 2026-09-28 23:13:43 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-09-28 23:11:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:09:18 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -0.036 |  |
| 2026-09-28 23:08:34 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.009 |  |
| 2026-09-28 23:07:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-28 23:07:37 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:07:00 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-09-28 23:06:25 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:05:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 23:04:58 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:04:56 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.065 |  |
| 2026-09-28 23:04:40 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-28 23:04:34 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-28 23:04:34 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-28 23:04:30 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-09-28 23:04:26 | Baddegama (Gin Ganga) | 3.56 | 🟡 Alert | -0.041 |  |
| 2026-09-28 23:04:25 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:04:02 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-28 23:04:01 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-28 23:03:57 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.039 |  |
| 2026-09-28 23:03:43 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:03:25 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:03:14 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | -0.022 |  |
| 2026-09-28 23:03:05 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | -0.020 |  |
| 2026-09-28 23:02:28 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-09-28 23:02:27 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:02:06 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-09-28 23:01:28 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:01:19 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | -0.030 |  |
| 2026-09-28 23:00:49 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:00:40 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 23:03:14 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | -0.022 |  |
| 2026-09-28 23:04:26 | Baddegama (Gin Ganga) | 3.56 | 🟡 Alert | -0.041 |  |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-28 23:04:40 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-28 23:07:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-28 23:04:34 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-28 22:03:23 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 23:05:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 22:30:15 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-28 23:04:01 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-28 23:00:40 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:03:25 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:00:49 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:11:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:04:25 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:03:43 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:02:27 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:04:58 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:06:25 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:07:37 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:01:28 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-28 23:07:00 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-09-28 23:08:34 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.009 |  |
| 2026-09-28 22:09:38 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-09-28 23:04:34 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-28 23:04:02 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-28 23:02:06 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 23:13:43 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-09-28 23:03:05 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | -0.020 |  |
| 2026-09-28 23:04:30 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-09-28 23:01:19 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | -0.030 |  |
| 2026-09-28 23:02:28 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-09-28 23:38:07 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.033 |  |
| 2026-09-28 23:09:18 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -0.036 |  |
| 2026-09-28 23:03:57 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.039 |  |
| 2026-09-28 23:04:56 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.065 |  |
| 2026-09-28 22:38:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)