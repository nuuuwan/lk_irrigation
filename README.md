# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_17:35:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,883 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 17:35:03 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | -0.032 |  |
| 2026-11-13 17:10:23 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-13 17:09:20 | Magura (Kalu Ganga) | 3.15 | 🟢 Normal | -0.046 |  |
| 2026-11-13 17:08:37 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.040 |  |
| 2026-11-13 17:07:29 | Moraketiya (Walawe Ganga) | 3.73 | 🟡 Alert | 0.000 |  |
| 2026-11-13 17:07:25 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.023 |  |
| 2026-11-13 17:07:13 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:06:12 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.029 |  |
| 2026-11-13 17:05:58 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.012 |  |
| 2026-11-13 17:05:24 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-11-13 17:05:24 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:05:14 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.068 |  |
| 2026-11-13 17:05:00 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.038 |  |
| 2026-11-13 17:04:50 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-13 17:04:41 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-13 17:04:13 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-11-13 17:04:07 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.032 |  |
| 2026-11-13 17:03:59 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-11-13 17:03:46 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.072 |  |
| 2026-11-13 17:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:02:54 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:02:49 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-13 17:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.030 |  |
| 2026-11-13 17:02:44 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.068 |  |
| 2026-11-13 17:02:40 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-11-13 17:02:35 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.035 |  |
| 2026-11-13 17:02:30 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-13 17:02:18 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.118 |  |
| 2026-11-13 17:02:03 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2026-11-13 17:01:36 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-13 17:01:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:01:21 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-13 17:01:20 | Ellagawa (Kalu Ganga) | 7.64 | 🟢 Normal | -0.050 |  |
| 2026-11-13 17:01:14 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-11-13 17:01:08 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-13 17:01:06 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 17:00:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-13 17:00:10 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:59:40 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 17:04:50 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-13 17:04:41 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-13 17:35:03 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | -0.032 |  |
| 2026-11-13 17:07:29 | Moraketiya (Walawe Ganga) | 3.73 | 🟡 Alert | 0.000 |  |
| 2026-11-13 17:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.030 |  |
| 2026-11-13 17:10:23 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-13 17:01:36 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-13 17:01:08 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-13 17:01:06 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 17:02:49 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-13 17:00:10 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-13 17:07:13 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:02:54 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:01:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:05:24 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-13 17:05:58 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.012 |  |
| 2026-11-13 17:04:13 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-11-13 17:02:30 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-13 17:01:21 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-13 17:02:03 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2026-11-13 17:01:14 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-11-13 17:07:25 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.023 |  |
| 2026-11-13 17:06:12 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.029 |  |
| 2026-11-13 17:05:24 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-11-13 17:00:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-13 17:02:40 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-11-13 17:04:07 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.032 |  |
| 2026-11-13 16:20:29 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.032 |  |
| 2026-11-13 17:02:35 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.035 |  |
| 2026-11-13 17:05:00 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.038 |  |
| 2026-11-13 17:08:37 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.040 |  |
| 2026-11-13 17:09:20 | Magura (Kalu Ganga) | 3.15 | 🟢 Normal | -0.046 |  |
| 2026-11-13 17:03:59 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-11-13 17:01:20 | Ellagawa (Kalu Ganga) | 7.64 | 🟢 Normal | -0.050 |  |
| 2026-11-13 17:02:44 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.068 |  |
| 2026-11-13 17:05:14 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.068 |  |
| 2026-11-13 17:03:46 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.072 |  |
| 2026-11-13 17:02:18 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)