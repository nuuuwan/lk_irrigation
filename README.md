# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_22:30:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 22:30:15 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-28 22:17:25 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.008 |  |
| 2026-09-28 22:16:58 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:09:38 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-09-28 22:09:30 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | -0.029 |  |
| 2026-09-28 22:07:58 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.112 |  |
| 2026-09-28 22:07:38 | Thalgahagoda (Nilwala Ganga) | 1.44 | 🟡 Alert | -0.020 |  |
| 2026-09-28 22:06:48 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-09-28 22:06:31 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:06:09 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-09-28 22:05:49 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.046 |  |
| 2026-09-28 22:05:38 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-28 22:05:11 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:04:58 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:04:32 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:04:01 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:03:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:03:23 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 22:03:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:02:43 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:02:41 | Manampitiya (Mahaweli Ganga) | -0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-28 22:02:41 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:02:40 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:02:29 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-28 22:02:17 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-28 22:02:11 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.090 |  |
| 2026-09-28 22:01:53 | Thaldena (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-09-28 22:01:51 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 22:01:51 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-09-28 22:01:47 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:01:40 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.048 |  |
| 2026-09-28 22:01:02 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:00:38 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:00:24 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 22:07:38 | Thalgahagoda (Nilwala Ganga) | 1.44 | 🟡 Alert | -0.020 |  |
| 2026-09-28 22:05:49 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.046 |  |
| 2026-09-28 22:06:48 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-28 22:05:38 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-28 22:03:23 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 22:30:15 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-28 22:02:29 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-28 22:01:51 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 22:04:58 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:00:24 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:00:38 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:01:02 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:06:31 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:03:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:02:43 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:16:58 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:04:32 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:02:40 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:03:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:04:01 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:05:11 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:02:41 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:05:28 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:01:47 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 22:17:25 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.008 |  |
| 2026-09-28 22:09:38 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-09-28 22:01:51 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-09-28 22:02:41 | Manampitiya (Mahaweli Ganga) | -0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-28 22:06:09 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-09-28 22:02:17 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 22:01:53 | Thaldena (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-09-28 22:09:30 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | -0.029 |  |
| 2026-09-28 22:01:40 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.048 |  |
| 2026-09-28 21:13:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.088 |  |
| 2026-09-28 22:02:11 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.090 |  |
| 2026-09-28 22:07:58 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)