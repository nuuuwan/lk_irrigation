# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_11:13:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,263 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 11:13:52 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:12:27 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.126 |  |
| 2026-11-07 11:11:45 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:11:14 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | -0.018 |  |
| 2026-11-07 11:08:42 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-11-07 11:08:06 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | -0.024 |  |
| 2026-11-07 11:07:30 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.084 |  |
| 2026-11-07 11:06:59 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.096 |  |
| 2026-11-07 11:05:42 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-11-07 11:05:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-07 11:05:29 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:05:11 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:05:09 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.235 |  |
| 2026-11-07 11:05:07 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.050 |  |
| 2026-11-07 11:04:19 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.216 |  |
| 2026-11-07 11:03:39 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.030 |  |
| 2026-11-07 11:03:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:03:30 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:03:29 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.059 |  |
| 2026-11-07 11:03:18 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:03:16 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-11-07 11:03:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 11:03:11 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.013 |  |
| 2026-11-07 11:03:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:02:57 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.135 |  |
| 2026-11-07 11:02:52 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | -0.088 |  |
| 2026-11-07 11:02:49 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.081 |  |
| 2026-11-07 11:02:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.020 |  |
| 2026-11-07 11:02:22 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-07 11:02:06 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 11:02:01 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:01:48 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-07 11:01:36 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 11:01:35 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:01:26 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:01:10 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-11-07 11:00:41 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 11:11:14 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | -0.018 |  |
| 2026-11-07 11:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.020 |  |
| 2026-11-07 11:05:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-07 11:01:48 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-07 11:03:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 11:01:36 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 11:02:06 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 11:01:35 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:11:45 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:03:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:02:01 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:05:29 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:03:18 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:00:41 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:03:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:05:11 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:13:52 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:03:30 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:01:26 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:02:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:03:11 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.013 |  |
| 2026-11-07 11:05:42 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-11-07 11:08:42 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-11-07 11:08:06 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | -0.024 |  |
| 2026-11-07 11:02:22 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-07 11:03:16 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-11-07 11:03:39 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.030 |  |
| 2026-11-07 11:01:10 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-11-07 11:05:07 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.050 |  |
| 2026-11-07 11:03:29 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.059 |  |
| 2026-11-07 11:02:49 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.081 |  |
| 2026-11-07 11:07:30 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.084 |  |
| 2026-11-07 11:02:52 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | -0.088 |  |
| 2026-11-07 11:06:59 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.096 |  |
| 2026-11-07 11:12:27 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.126 |  |
| 2026-11-07 11:02:57 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.135 |  |
| 2026-11-07 11:04:19 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.216 |  |
| 2026-11-07 11:05:09 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.235 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)