# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_22:26:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 22:26:39 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-11-13 22:23:16 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:19:48 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | -0.025 |  |
| 2026-11-13 22:17:50 | Kuda Oya (Kirindi Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:15:29 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.057 |  |
| 2026-11-13 22:15:16 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.026 |  |
| 2026-11-13 22:08:03 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:06:36 | Thanamalwila (Kirindi Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:05:54 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 22:05:52 | Baddegama (Gin Ganga) | 3.97 | 🟡 Alert | -0.024 |  |
| 2026-11-13 22:05:41 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:05:22 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-11-13 22:05:15 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.019 |  |
| 2026-11-13 22:04:13 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-11-13 22:04:09 | Ellagawa (Kalu Ganga) | 7.28 | 🟢 Normal | -0.136 |  |
| 2026-11-13 22:03:54 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:03:44 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:03:14 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:59 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-11-13 22:02:45 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 22:02:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:27 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-13 22:02:23 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:22 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-11-13 22:02:19 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:16 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:12 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | -0.100 |  |
| 2026-11-13 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | -0.041 |  |
| 2026-11-13 22:01:51 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.052 |  |
| 2026-11-13 22:01:47 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:01:37 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:01:37 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.030 |  |
| 2026-11-13 22:01:18 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.071 |  |
| 2026-11-13 22:00:47 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:00:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 22:05:54 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 22:05:52 | Baddegama (Gin Ganga) | 3.97 | 🟡 Alert | -0.024 |  |
| 2026-11-13 22:19:48 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | -0.025 |  |
| 2026-11-13 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | -0.041 |  |
| 2026-11-13 22:02:12 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | -0.100 |  |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 22:02:45 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 22:00:47 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:16 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:03:54 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:01:37 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:08:03 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:00:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:23:16 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:03:44 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:17:50 | Kuda Oya (Kirindi Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:26:39 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-11-13 22:05:41 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:01:47 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:06:36 | Thanamalwila (Kirindi Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:23 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:03:14 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:05:15 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.019 |  |
| 2026-11-13 22:02:59 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-11-13 22:15:16 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.026 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-13 22:01:37 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.030 |  |
| 2026-11-13 22:04:13 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-11-13 22:05:22 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-11-13 22:02:27 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-13 22:02:22 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-11-13 22:01:51 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.052 |  |
| 2026-11-13 22:15:29 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.057 |  |
| 2026-11-13 22:01:18 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.071 |  |
| 2026-11-13 21:09:43 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.103 |  |
| 2026-11-13 22:04:09 | Ellagawa (Kalu Ganga) | 7.28 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)