# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_03:18:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 03:18:52 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -90.000 |  |
| 2026-11-14 03:18:50 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -90.000 |  |
| 2026-11-14 03:18:49 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -90.000 |  |
| 2026-11-14 03:18:05 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 03:15:17 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.017 |  |
| 2026-11-14 03:14:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:14:40 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.054 |  |
| 2026-11-14 03:13:13 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -3.130 |  |
| 2026-11-14 03:12:50 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -3.130 |  |
| 2026-11-14 03:12:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:11:53 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-14 03:11:43 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -180.000 |  |
| 2026-11-14 03:11:42 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -180.000 |  |
| 2026-11-14 03:10:38 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.055 |  |
| 2026-11-14 03:10:18 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:10:06 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:09:25 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | -0.187 |  |
| 2026-11-14 03:05:15 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:05:13 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-11-14 03:04:41 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:04:37 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 03:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | -0.087 |  |
| 2026-11-14 03:04:08 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | -0.025 |  |
| 2026-11-14 03:04:05 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.006 |  |
| 2026-11-14 03:03:49 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-14 03:03:39 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-11-14 03:03:20 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:03:12 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 03:03:09 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:02:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-11-14 03:02:48 | Baddegama (Gin Ganga) | 3.83 | 🟡 Alert | -0.020 |  |
| 2026-11-14 03:02:47 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.013 |  |
| 2026-11-14 03:02:46 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-11-14 03:02:35 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.041 |  |
| 2026-11-14 03:02:21 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:02:11 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:02:09 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:34 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-11-14 03:01:12 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:00:16 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-14 03:00:16 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 03:18:05 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 03:02:48 | Baddegama (Gin Ganga) | 3.83 | 🟡 Alert | -0.020 |  |
| 2026-11-14 03:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | -0.087 |  |
| 2026-11-14 03:13:13 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -3.130 |  |
| 2026-11-14 03:11:53 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-14 03:03:49 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-14 03:00:16 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 03:01:12 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:02:09 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:10:18 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:03:09 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:14:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:04:05 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.006 |  |
| 2026-11-14 03:03:39 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-11-14 03:05:13 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-11-14 03:03:12 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 03:00:16 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-14 03:02:47 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.013 |  |
| 2026-11-14 03:15:17 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.017 |  |
| 2026-11-14 03:04:41 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:05:15 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:03:20 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:02:21 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:02:11 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:04:08 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | -0.025 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 03:02:46 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-11-14 03:02:35 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.041 |  |
| 2026-11-14 03:01:34 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-11-14 03:02:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-11-14 03:14:40 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.054 |  |
| 2026-11-14 03:10:38 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.055 |  |
| 2026-11-14 03:09:25 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | -0.187 |  |
| 2026-11-14 03:18:52 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -90.000 |  |
| 2026-11-14 03:11:43 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)