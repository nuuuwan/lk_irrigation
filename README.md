# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_06:21:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,582 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 06:21:28 | Panadugama (Nilwala Ganga) | 5.20 | 🟡 Alert | 0.429 | 🔺 Rising |
| 2026-11-21 06:18:14 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:08:20 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-21 06:08:17 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.037 |  |
| 2026-11-21 06:08:03 | Urawa (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.128 |  |
| 2026-11-21 06:07:10 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-11-21 06:07:09 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-11-21 06:06:51 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:06:45 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-21 06:06:04 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.081 |  |
| 2026-11-21 06:05:48 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:04:56 | Peradeniya (Mahaweli Ganga) | 4.26 | 🟢 Normal | -0.048 |  |
| 2026-11-21 06:04:41 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-21 06:04:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:04:18 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-11-21 06:04:03 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.095 |  |
| 2026-11-21 06:03:43 | Rathnapura (Kalu Ganga) | 3.19 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-21 06:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.086 |  |
| 2026-11-21 06:03:24 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-21 06:03:21 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-21 06:03:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.101 |  |
| 2026-11-21 06:03:00 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-21 06:02:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:02:41 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 06:02:28 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | 0.524 | 🔺 Rising |
| 2026-11-21 06:02:09 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-11-21 06:01:58 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-11-21 06:01:30 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-21 06:01:25 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-21 06:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:01:19 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | 1.068 | 🔺 Rising |
| 2026-11-21 06:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-21 06:01:16 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.053 |  |
| 2026-11-21 06:01:08 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-21 06:01:00 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-11-21 06:00:59 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 06:00:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-21 05:52:07 | Panadugama (Nilwala Ganga) | 4.99 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-11-21 05:44:28 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 1.068 | 🔺 Rising |
| 2026-11-21 05:44:27 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 1.068 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 06:21:28 | Panadugama (Nilwala Ganga) | 5.20 | 🟡 Alert | 0.429 | 🔺 Rising |
| 2026-11-21 06:07:10 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-11-21 06:01:19 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | 1.068 | 🔺 Rising |
| 2026-11-21 06:02:28 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | 0.524 | 🔺 Rising |
| 2026-11-21 06:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-21 06:01:30 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-21 06:02:09 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-11-21 06:03:43 | Rathnapura (Kalu Ganga) | 3.19 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-21 06:01:08 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-21 06:03:21 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-21 06:01:25 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-21 06:03:24 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-21 06:03:00 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-21 06:04:41 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-21 06:08:20 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-21 06:00:59 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 06:00:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-21 06:02:41 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 06:06:45 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-21 06:04:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:06:51 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:18:14 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:05:48 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.000 |  |
| 2026-11-21 06:02:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-21 06:04:18 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-11-21 06:01:58 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-11-21 06:08:17 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.037 |  |
| 2026-11-21 06:04:56 | Peradeniya (Mahaweli Ganga) | 4.26 | 🟢 Normal | -0.048 |  |
| 2026-11-21 06:01:00 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-11-21 06:01:16 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.053 |  |
| 2026-11-21 06:06:04 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.081 |  |
| 2026-11-21 06:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.086 |  |
| 2026-11-21 06:04:03 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.095 |  |
| 2026-11-21 06:03:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.101 |  |
| 2026-11-21 06:08:03 | Urawa (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)