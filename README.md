# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_21:18:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 21:18:10 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.000 |  |
| 2026-11-01 21:16:30 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-01 21:11:40 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-01 21:10:47 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.005 |  |
| 2026-11-01 21:10:39 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:09:44 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-11-01 21:09:11 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:08:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-01 21:08:28 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-01 21:06:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.058 |  |
| 2026-11-01 21:06:44 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-11-01 21:06:29 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-11-01 21:06:28 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:05:50 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-01 21:05:24 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-01 21:05:13 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 21:04:33 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-01 21:04:21 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-01 21:03:32 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:55 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.030 |  |
| 2026-11-01 21:02:54 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:40 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:28 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-11-01 21:02:21 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 21:02:18 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:13 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.065 |  |
| 2026-11-01 21:01:54 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.017 |  |
| 2026-11-01 21:01:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 21:01:38 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-01 21:01:28 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-01 21:01:25 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-11-01 21:01:20 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 21:00:37 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-01 21:00:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 21:18:10 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.000 |  |
| 2026-11-01 21:01:25 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-11-01 21:02:28 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-11-01 21:00:37 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-01 21:08:28 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-01 21:05:24 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-01 21:16:30 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-01 21:01:28 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-01 21:01:38 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-01 21:05:13 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 21:01:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 21:08:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-01 21:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 21:02:21 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 21:11:40 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-01 21:00:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:40 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:03:32 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:54 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:13 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:18 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:10:39 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:01:20 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:09:11 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:10:47 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.005 |  |
| 2026-11-01 21:06:29 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-11-01 21:04:21 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-01 21:05:50 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-01 21:04:33 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-01 21:01:54 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.017 |  |
| 2026-11-01 21:09:44 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-11-01 21:06:44 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-11-01 21:02:55 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 21:06:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.058 |  |
| 2026-11-01 21:01:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)