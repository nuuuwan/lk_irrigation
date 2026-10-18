# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_10:08:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,168 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 10:08:52 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | -0.047 |  |
| 2026-10-18 10:07:36 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-10-18 10:06:18 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.046 |  |
| 2026-10-18 10:06:14 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:06:06 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.092 |  |
| 2026-10-18 10:06:05 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-10-18 10:05:57 | Weraganthota (Mahaweli Ganga) | -2.43 | 🟢 Normal | -65.749 |  |
| 2026-10-18 10:05:49 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 10:04:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:04:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:03:56 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-10-18 10:03:53 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.210 |  |
| 2026-10-18 10:03:51 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-10-18 10:03:42 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-18 10:03:24 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | -0.109 |  |
| 2026-10-18 10:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-18 10:03:17 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 10:03:10 | Weraganthota (Mahaweli Ganga) | 0.62 | 🟢 Normal | -65.749 |  |
| 2026-10-18 10:03:07 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.120 |  |
| 2026-10-18 10:02:27 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.119 |  |
| 2026-10-18 10:02:23 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-18 10:02:22 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.152 |  |
| 2026-10-18 10:02:19 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.106 |  |
| 2026-10-18 10:02:18 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:02:13 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-10-18 10:02:12 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 10:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:01:49 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.161 |  |
| 2026-10-18 10:01:42 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.113 |  |
| 2026-10-18 10:01:30 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-18 10:01:22 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:01:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-10-18 10:00:47 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.018 |  |
| 2026-10-18 09:28:14 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 10:01:30 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-18 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | -0.031 |  |
| 2026-10-18 10:08:52 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | -0.047 |  |
| 2026-10-18 10:03:42 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-18 10:02:23 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-18 09:04:31 | Horowpothana (Yan Oya) | 3.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-18 09:01:44 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 10:02:12 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 10:03:17 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 10:05:49 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 10:02:18 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:01:22 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:06:14 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:04:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:04:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:07:36 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-10-18 10:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-18 10:03:56 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-10-18 10:03:51 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:02:40 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-18 10:00:47 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.018 |  |
| 2026-10-18 10:02:13 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-10-18 10:06:05 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-10-18 09:05:50 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.022 |  |
| 2026-10-18 09:02:39 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-10-18 10:06:18 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.046 |  |
| 2026-10-18 10:01:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-10-18 10:06:06 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.092 |  |
| 2026-10-18 10:02:19 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.106 |  |
| 2026-10-18 10:03:24 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | -0.109 |  |
| 2026-10-18 10:01:42 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.113 |  |
| 2026-10-18 10:02:27 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.119 |  |
| 2026-10-18 10:03:07 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.120 |  |
| 2026-10-18 09:04:52 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.137 |  |
| 2026-10-18 10:02:22 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.152 |  |
| 2026-10-18 10:01:49 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.161 |  |
| 2026-10-18 10:03:53 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.210 |  |
| 2026-10-18 10:05:57 | Weraganthota (Mahaweli Ganga) | -2.43 | 🟢 Normal | -65.749 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)