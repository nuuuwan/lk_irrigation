# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_19:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,863 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 19:13:08 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-01 19:11:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:10:21 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | -3312.000 |  |
| 2025-12-01 19:10:19 | Giriulla (Maha Oya) | 4.69 | 🟢 Normal | -3312.000 |  |
| 2025-12-01 19:10:14 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:10:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | -0.044 |  |
| 2025-12-01 19:09:13 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2025-12-01 19:08:54 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.018 |  |
| 2025-12-01 19:08:06 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:07:59 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:06:40 | Hanwella (Kelani Ganga) | 8.53 | 🟠 Minor Flood | -0.080 |  |
| 2025-12-01 19:05:23 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-01 19:05:04 | Putupaula (Kalu Ganga) | 4.14 | 🟠 Minor Flood | -0.009 |  |
| 2025-12-01 19:04:57 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:04:53 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-01 19:04:38 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:04:36 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-01 19:04:08 | Nagalagam Street (Kelani Ganga) | 2.47 | 🔴 Major Flood | -0.031 |  |
| 2025-12-01 19:03:47 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:03:41 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2025-12-01 19:03:29 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 19:03:14 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2025-12-01 19:02:55 | Glencourse (Kelani Ganga) | 12.13 | 🟢 Normal | -0.090 |  |
| 2025-12-01 19:02:47 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:02:27 | Horowpothana (Yan Oya) | 6.43 | 🟡 Alert | -0.078 |  |
| 2025-12-01 19:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -2.250 |  |
| 2025-12-01 19:02:16 | Thanthirimale (Malwathu Oya) | 9.25 | 🔴 Major Flood | -0.030 |  |
| 2025-12-01 19:02:10 | Ellagawa (Kalu Ganga) | 10.72 | 🟠 Minor Flood | -0.094 |  |
| 2025-12-01 19:01:54 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | -0.042 |  |
| 2025-12-01 19:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -2.250 |  |
| 2025-12-01 19:01:31 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:01:13 | Nakkala (Kumbukkan Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:00:24 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2025-12-01 19:00:17 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 19:02:16 | Thanthirimale (Malwathu Oya) | 9.25 | 🔴 Major Flood | -0.030 |  |
| 2025-12-01 19:04:08 | Nagalagam Street (Kelani Ganga) | 2.47 | 🔴 Major Flood | -0.031 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 19:05:04 | Putupaula (Kalu Ganga) | 4.14 | 🟠 Minor Flood | -0.009 |  |
| 2025-12-01 19:10:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | -0.044 |  |
| 2025-12-01 19:06:40 | Hanwella (Kelani Ganga) | 8.53 | 🟠 Minor Flood | -0.080 |  |
| 2025-12-01 19:02:10 | Ellagawa (Kalu Ganga) | 10.72 | 🟠 Minor Flood | -0.094 |  |
| 2025-12-01 19:01:54 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | -0.042 |  |
| 2025-12-01 19:02:27 | Horowpothana (Yan Oya) | 6.43 | 🟡 Alert | -0.078 |  |
| 2025-12-01 19:04:36 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-01 19:13:08 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-01 19:03:29 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 19:00:17 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:11:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:10:14 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:12 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:04:38 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:07:59 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:04:57 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:08:06 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-01 19:01:13 | Nakkala (Kumbukkan Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:01:31 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:03:47 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:02:47 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-01 19:09:13 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2025-12-01 19:08:54 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.018 |  |
| 2025-12-01 19:04:53 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-01 19:03:41 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2025-12-01 19:03:14 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2025-12-01 19:00:24 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2025-12-01 19:05:23 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-01 19:02:55 | Glencourse (Kelani Ganga) | 12.13 | 🟢 Normal | -0.090 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-01 19:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -2.250 |  |
| 2025-12-01 19:10:21 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | -3312.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)