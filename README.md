# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_17:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 17:03:46 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.060 |  |
| 2026-09-27 17:03:42 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:03:23 | Dunamale (Aththanagalu Oya) | 2.13 | 🟢 Normal | -0.040 |  |
| 2026-09-27 17:03:18 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:03:02 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:03:00 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -0.022 |  |
| 2026-09-27 17:02:55 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-27 17:02:53 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:02:25 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-27 17:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:02:12 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:01:52 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-09-27 17:01:50 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:01:31 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.020 |  |
| 2026-09-27 17:01:29 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.015 |  |
| 2026-09-27 17:01:28 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-27 17:01:19 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-09-27 17:01:12 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-09-27 17:01:11 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:00:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:21:10 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 17:02:55 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-27 16:08:53 | Baddegama (Gin Ganga) | 4.58 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 16:15:25 | Panadugama (Nilwala Ganga) | 5.19 | 🟡 Alert | -0.025 |  |
| 2026-09-27 16:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.094 |  |
| 2026-09-27 17:01:12 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-09-27 17:02:25 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-27 16:04:01 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 17:00:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:45 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:03:02 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:48 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:02:53 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:03:42 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:18:27 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-27 17:01:11 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.005 |  |
| 2026-09-27 16:09:34 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-09-27 17:02:12 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:05:58 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:53 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:35 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:03:18 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:01:50 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-27 17:01:29 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.015 |  |
| 2026-09-27 16:09:10 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.018 |  |
| 2026-09-27 17:01:31 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.020 |  |
| 2026-09-27 17:01:52 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-09-27 16:02:14 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-27 17:03:00 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -0.022 |  |
| 2026-09-27 17:01:28 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-27 17:01:19 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-09-27 17:03:23 | Dunamale (Aththanagalu Oya) | 2.13 | 🟢 Normal | -0.040 |  |
| 2026-09-27 16:03:56 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.043 |  |
| 2026-09-27 16:08:30 | Ellagawa (Kalu Ganga) | 8.15 | 🟢 Normal | -0.055 |  |
| 2026-09-27 17:03:46 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.060 |  |
| 2026-09-27 16:06:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.090 |  |
| 2026-09-27 16:08:47 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)