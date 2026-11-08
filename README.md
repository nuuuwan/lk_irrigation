# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_04:24:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,788 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 04:24:50 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | -0.115 |  |
| 2026-11-09 04:21:21 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-09 04:17:16 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-11-09 04:14:02 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.017 |  |
| 2026-11-09 04:10:55 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 04:09:33 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | -0.017 |  |
| 2026-11-09 04:08:31 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-11-09 04:08:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-11-09 04:08:12 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-09 04:08:04 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 04:06:54 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-09 04:06:51 | Dunamale (Aththanagalu Oya) | 4.15 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-11-09 04:06:29 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-09 04:05:08 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-09 04:05:05 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-09 04:04:57 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.137 |  |
| 2026-11-09 04:04:14 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 04:03:06 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | -0.446 |  |
| 2026-11-09 04:02:55 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-09 04:02:38 | Giriulla (Maha Oya) | 3.87 | 🟢 Normal | -0.184 |  |
| 2026-11-09 04:02:20 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.222 |  |
| 2026-11-09 04:02:12 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.060 |  |
| 2026-11-09 04:01:43 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.051 |  |
| 2026-11-09 04:01:23 | Moragaswewa (Deduru Oya) | 3.24 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:01:21 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.042 |  |
| 2026-11-09 04:01:21 | Holombuwa (Kelani Ganga) | 1.79 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-11-09 04:01:11 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.020 |  |
| 2026-11-09 04:00:25 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 03:21:37 | Magura (Kalu Ganga) | 5.12 | 🟡 Alert | 0.468 | 🔺 Rising |
| 2026-11-09 04:06:51 | Dunamale (Aththanagalu Oya) | 4.15 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-11-09 04:08:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-11-09 04:10:55 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 04:08:31 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-11-09 04:09:33 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | -0.017 |  |
| 2026-11-09 04:05:08 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-09 04:05:05 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 03:04:45 | Baddegama (Gin Ganga) | 3.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-09 04:06:54 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-09 04:21:21 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-09 04:06:29 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-09 04:04:14 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 04:08:04 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 04:08:12 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-09 04:02:55 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-09 04:14:02 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.017 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-09 04:01:11 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.020 |  |
| 2026-11-09 03:00:14 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-11-09 04:17:16 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-11-09 04:00:25 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-11-09 04:01:21 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.042 |  |
| 2026-11-09 04:01:43 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.051 |  |
| 2026-11-09 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-11-09 04:02:12 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.060 |  |
| 2026-11-09 03:15:26 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.078 |  |
| 2026-11-09 04:01:23 | Moragaswewa (Deduru Oya) | 3.24 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:01:21 | Holombuwa (Kelani Ganga) | 1.79 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:24:50 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | -0.115 |  |
| 2026-11-09 04:04:57 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.137 |  |
| 2026-11-09 04:02:38 | Giriulla (Maha Oya) | 3.87 | 🟢 Normal | -0.184 |  |
| 2026-11-09 04:02:20 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.222 |  |
| 2026-11-09 04:03:06 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | -0.446 |  |
| 2026-11-09 03:05:51 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -1.333 |  |
| 2026-11-09 03:44:14 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)