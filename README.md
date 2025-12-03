# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_13:05:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,263 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 13:05:50 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.031 |  |
| 2025-12-03 13:05:28 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-03 13:05:23 | Hanwella (Kelani Ganga) | 5.21 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:05:21 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:05:13 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:05:09 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | -0.025 |  |
| 2025-12-03 13:05:06 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:04:30 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:04:09 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2025-12-03 13:04:06 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:37 | Hanwella (Kelani Ganga) | 5.21 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:25 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | -0.140 |  |
| 2025-12-03 13:03:22 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:21 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:10 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:08 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-03 13:02:46 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-03 13:02:24 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | -0.016 |  |
| 2025-12-03 13:02:22 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:02:19 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.075 |  |
| 2025-12-03 13:02:17 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.011 |  |
| 2025-12-03 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | -0.060 |  |
| 2025-12-03 13:01:54 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-03 13:01:35 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2025-12-03 13:01:20 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.199 |  |
| 2025-12-03 13:00:43 | Thanthirimale (Malwathu Oya) | 7.22 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-03 13:00:33 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.013 |  |
| 2025-12-03 13:00:12 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:42:03 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:13:42 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.013 |  |
| 2025-12-03 12:11:14 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:10:27 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:09:28 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:07:36 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.031 |  |
| 2025-12-03 12:07:24 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.020 |  |
| 2025-12-03 12:07:18 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2025-12-03 12:07:13 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 13:00:43 | Thanthirimale (Malwathu Oya) | 7.22 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-03 13:02:24 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | -0.016 |  |
| 2025-12-03 13:05:28 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-03 13:04:30 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:11:14 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:09:28 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:42:03 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:10 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:05:23 | Hanwella (Kelani Ganga) | 5.21 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:05:21 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:01:35 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:02:22 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:05:13 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:05:06 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:21 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:03:22 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:10:27 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:06:14 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:02:59 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:04:06 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:02:46 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-03 13:00:12 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-03 13:01:54 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-03 13:04:09 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2025-12-03 13:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2025-12-03 13:02:17 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.011 |  |
| 2025-12-03 13:00:33 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.013 |  |
| 2025-12-03 12:07:24 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.020 |  |
| 2025-12-03 13:03:08 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-03 13:05:09 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | -0.025 |  |
| 2025-12-03 12:03:15 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.026 |  |
| 2025-12-03 13:05:50 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.031 |  |
| 2025-12-03 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | -0.060 |  |
| 2025-12-03 13:02:19 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.075 |  |
| 2025-12-03 13:03:25 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | -0.140 |  |
| 2025-12-03 13:01:20 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.199 |  |

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)