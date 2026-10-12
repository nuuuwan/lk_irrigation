# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_02:11:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 02:11:44 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-10-13 02:11:17 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-10-13 02:10:07 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-10-13 02:09:48 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.088 |  |
| 2026-10-13 02:09:10 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-13 02:08:57 | Urawa (Nilwala Ganga) | 2.79 | 🟡 Alert | -0.158 |  |
| 2026-10-13 02:08:48 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:08:07 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-10-13 02:07:05 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-13 02:04:31 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-13 02:04:03 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-10-13 02:03:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:03:31 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-13 02:03:16 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-13 02:03:12 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:03:02 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.026 |  |
| 2026-10-13 02:02:40 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-13 02:02:35 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.043 |  |
| 2026-10-13 02:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-13 02:02:20 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.142 |  |
| 2026-10-13 02:02:04 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 02:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-13 02:01:32 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:01:18 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.104 |  |
| 2026-10-13 02:01:13 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:01:02 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 02:00:53 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:00:36 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 00:09:32 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-10-13 02:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-13 02:08:57 | Urawa (Nilwala Ganga) | 2.79 | 🟡 Alert | -0.158 |  |
| 2026-10-13 00:17:28 | Pitabeddara (Nilwala Ganga) | 3.01 | 🟢 Normal | 23.220 | 🔺 Rising |
| 2026-10-13 02:11:44 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-13 02:03:16 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-13 02:03:31 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-13 02:07:05 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-13 02:04:31 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-13 01:18:47 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-13 02:09:10 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-13 02:02:04 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 02:01:02 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:01:13 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:08:48 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:03:12 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:00:53 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:03:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-13 01:06:12 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:01:32 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:04:03 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-10-13 02:02:40 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-13 01:05:27 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-13 01:03:43 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-13 01:00:24 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.011 |  |
| 2026-10-13 02:10:07 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-10-13 02:08:07 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-10-13 02:00:36 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.024 |  |
| 2026-10-13 02:03:02 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.026 |  |
| 2026-10-13 02:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-13 02:02:35 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.043 |  |
| 2026-10-13 02:09:48 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.088 |  |
| 2026-10-13 02:01:18 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.104 |  |
| 2026-10-13 02:02:20 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)