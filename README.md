# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_00:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,725 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 00:03:00 | Nakkala (Kumbukkan Oya) | 2.15 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-08 00:02:55 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-08 00:02:55 | Dunamale (Aththanagalu Oya) | 3.76 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 00:02:27 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-11-08 00:02:23 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-08 00:02:11 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:01:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-08 00:01:29 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:00:50 | Moraketiya (Walawe Ganga) | 4.35 | 🟡 Alert | 0.599 | 🔺 Rising |
| 2026-11-08 00:00:18 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.030 |  |
| 2026-11-07 23:37:30 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-07 23:23:41 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:23:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 00:00:50 | Moraketiya (Walawe Ganga) | 4.35 | 🟡 Alert | 0.599 | 🔺 Rising |
| 2026-11-08 00:02:55 | Dunamale (Aththanagalu Oya) | 3.76 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 23:04:19 | Urawa (Nilwala Ganga) | 3.80 | 🟡 Alert | -0.020 |  |
| 2026-11-07 23:03:37 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | 0.669 | 🔺 Rising |
| 2026-11-07 23:01:54 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-11-07 23:02:16 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-11-07 23:08:05 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-07 23:08:28 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-08 00:02:23 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 23:07:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-08 00:03:00 | Nakkala (Kumbukkan Oya) | 2.15 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-08 00:02:55 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-07 23:01:43 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-07 23:08:52 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-07 23:03:55 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-07 23:05:09 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-07 23:02:56 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-07 23:05:07 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-07 23:02:52 | Peradeniya (Mahaweli Ganga) | 3.97 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-07 21:05:32 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 00:01:29 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:23:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:01:46 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:01:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 00:02:11 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:04:36 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:23:41 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:02:29 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:01:44 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-07 23:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 23:06:27 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 00:00:18 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.030 |  |
| 2026-11-08 00:02:27 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-11-07 23:03:48 | Wellawaya (Kirindi Oya) | 2.80 | 🟢 Normal | -0.239 |  |
| 2026-11-07 22:07:58 | Thaldena (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)