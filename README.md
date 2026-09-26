# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_17:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,643 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 17:03:06 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-09-26 17:03:04 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 17:02:58 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.060 |  |
| 2026-09-26 17:02:57 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.050 |  |
| 2026-09-26 17:02:50 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.111 |  |
| 2026-09-26 17:02:49 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:02:47 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-26 17:02:44 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-26 17:02:43 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:02:40 | Ellagawa (Kalu Ganga) | 8.93 | 🟢 Normal | -0.020 |  |
| 2026-09-26 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-26 17:02:21 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-09-26 17:02:02 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-26 17:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:01:48 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-26 17:01:36 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 17:01:19 | Glencourse (Kelani Ganga) | 13.10 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:59:43 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.061 |  |
| 2026-09-26 16:21:28 | Magura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 16:05:40 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 17:03:04 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-26 16:09:38 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.010 |  |
| 2026-09-26 17:02:02 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-26 16:07:35 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-26 16:01:05 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 16:06:34 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-26 17:01:36 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 16:02:54 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 16:01:31 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-09-26 16:00:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:02:33 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:04:42 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:04:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:01:19 | Glencourse (Kelani Ganga) | 13.10 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:02:49 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:02:43 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:08:13 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:01:56 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:08:34 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-26 16:03:18 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 17:02:47 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-26 17:02:44 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-26 17:02:21 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-09-26 17:02:40 | Ellagawa (Kalu Ganga) | 8.93 | 🟢 Normal | -0.020 |  |
| 2026-09-26 17:03:06 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-09-26 17:01:48 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-26 16:03:48 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-26 16:03:15 | Hanwella (Kelani Ganga) | 5.33 | 🟢 Normal | -0.031 |  |
| 2026-09-26 16:01:11 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.034 |  |
| 2026-09-26 16:21:28 | Magura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.041 |  |
| 2026-09-26 16:01:53 | Thawalama (Gin Ganga) | 2.81 | 🟢 Normal | -0.045 |  |
| 2026-09-26 17:02:57 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.050 |  |
| 2026-09-26 17:02:58 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.060 |  |
| 2026-09-26 16:59:43 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.061 |  |
| 2026-09-26 17:02:50 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.111 |  |
| 2026-09-26 16:00:54 | Kithulgala (Kelani Ganga) | 2.42 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)