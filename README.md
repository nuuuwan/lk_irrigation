# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_00:20:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,752 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 00:20:28 | Panadugama (Nilwala Ganga) | 4.89 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-11-08 00:15:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:12:13 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-08 00:11:56 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:10:31 | Thanamalwila (Kirindi Oya) | 2.98 | 🟢 Normal | 0.744 | 🔺 Rising |
| 2026-11-08 00:10:12 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-08 00:09:35 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-11-08 00:08:38 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.057 |  |
| 2026-11-08 00:08:20 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.139 |  |
| 2026-11-08 00:06:52 | Peradeniya (Mahaweli Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:06:25 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-08 00:06:22 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:06:22 | Thaldena (Mahaweli Ganga) | 1.35 | 🟢 Normal | -180.000 |  |
| 2026-11-08 00:06:21 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -180.000 |  |
| 2026-11-08 00:06:14 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-08 00:06:13 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-08 00:06:01 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-11-08 00:05:44 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-11-08 00:05:19 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-08 00:04:17 | Pitabeddara (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-08 00:04:10 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 00:03:37 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:03:32 | Urawa (Nilwala Ganga) | 3.70 | 🟡 Alert | -0.101 |  |
| 2026-11-08 00:03:21 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-08 00:03:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:03:17 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-11-08 00:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:03:00 | Nakkala (Kumbukkan Oya) | 2.15 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-08 00:02:55 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-08 00:02:55 | Dunamale (Aththanagalu Oya) | 3.76 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 00:02:27 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-11-08 00:02:23 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-08 00:02:11 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:01:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-08 00:01:29 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-11-08 00:00:50 | Moraketiya (Walawe Ganga) | 4.35 | 🟡 Alert | 0.599 | 🔺 Rising |
| 2026-11-08 00:00:18 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 00:00:50 | Moraketiya (Walawe Ganga) | 4.35 | 🟡 Alert | 0.599 | 🔺 Rising |
| 2026-11-08 00:02:55 | Dunamale (Aththanagalu Oya) | 3.76 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 00:03:32 | Urawa (Nilwala Ganga) | 3.70 | 🟡 Alert | -0.101 |  |
| 2026-11-08 00:03:17 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-11-08 00:10:31 | Thanamalwila (Kirindi Oya) | 2.98 | 🟢 Normal | 0.744 | 🔺 Rising |
| 2026-11-08 00:09:35 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-11-08 00:20:28 | Panadugama (Nilwala Ganga) | 4.89 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-11-08 00:04:17 | Pitabeddara (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-08 00:02:23 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-08 00:03:00 | Nakkala (Kumbukkan Oya) | 2.15 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-08 00:02:55 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-08 00:03:21 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-08 00:12:13 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-08 00:06:13 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-08 00:06:14 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-08 00:04:10 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 00:05:19 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-08 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-08 00:10:12 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-08 00:03:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:06:22 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:01:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:02:11 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:03:37 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:06:52 | Peradeniya (Mahaweli Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:11:56 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:15:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:06:25 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 00:05:44 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-11-08 00:00:18 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.030 |  |
| 2026-11-08 00:06:01 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-11-08 00:02:27 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-11-08 00:08:38 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.057 |  |
| 2026-11-08 00:08:20 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.139 |  |
| 2026-11-08 00:06:22 | Thaldena (Mahaweli Ganga) | 1.35 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)