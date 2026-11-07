# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_03:03:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 03:03:10 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:03:10 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.020 |  |
| 2026-11-08 03:02:58 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-08 03:02:54 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:02:52 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-11-08 03:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | -0.010 |  |
| 2026-11-08 03:02:48 | Kuda Oya (Kirindi Oya) | 2.64 | 🟢 Normal | 0.819 | 🔺 Rising |
| 2026-11-08 03:02:32 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -36.000 |  |
| 2026-11-08 03:02:31 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -36.000 |  |
| 2026-11-08 03:02:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.033 |  |
| 2026-11-08 03:01:58 | Giriulla (Maha Oya) | 3.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-08 03:01:52 | Moragaswewa (Deduru Oya) | 1.88 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-08 03:01:43 | Ellagawa (Kalu Ganga) | 6.87 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 03:01:24 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | -0.139 |  |
| 2026-11-08 03:01:14 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 02:36:30 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.371 |  |
| 2026-11-08 02:24:08 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-11-08 02:22:46 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | 0.285 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 02:24:08 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-11-08 02:00:23 | Moraketiya (Walawe Ganga) | 4.50 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-08 02:05:27 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-08 02:04:48 | Urawa (Nilwala Ganga) | 3.42 | 🟡 Alert | -0.139 |  |
| 2026-11-08 03:02:48 | Kuda Oya (Kirindi Oya) | 2.64 | 🟢 Normal | 0.819 | 🔺 Rising |
| 2026-11-08 02:22:46 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-11-08 01:10:01 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-08 03:02:58 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-08 03:01:43 | Ellagawa (Kalu Ganga) | 6.87 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 03:01:52 | Moragaswewa (Deduru Oya) | 1.88 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-08 03:01:58 | Giriulla (Maha Oya) | 3.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-08 02:03:46 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 03:01:14 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 01:18:52 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 02:06:50 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-08 02:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:16:07 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:03:10 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:07 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:02:54 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:29:19 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 03:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | -0.010 |  |
| 2026-11-08 02:05:45 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-11-08 03:03:10 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 03:02:52 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-11-08 03:02:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.033 |  |
| 2026-11-08 02:01:30 | Thawalama (Gin Ganga) | 3.54 | 🟢 Normal | -0.043 |  |
| 2026-11-08 02:03:35 | Thaldena (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.051 |  |
| 2026-11-08 02:00:45 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -0.052 |  |
| 2026-11-08 02:06:24 | Wellawaya (Kirindi Oya) | 2.50 | 🟢 Normal | -0.076 |  |
| 2026-11-08 02:07:48 | Thanamalwila (Kirindi Oya) | 2.78 | 🟢 Normal | -0.105 |  |
| 2026-11-08 03:01:24 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | -0.139 |  |
| 2026-11-08 02:03:01 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.152 |  |
| 2026-11-08 02:36:30 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.371 |  |
| 2026-11-08 03:02:32 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)