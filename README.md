# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_15:07:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 15:07:01 | Hanwella (Kelani Ganga) | 5.06 | 🟢 Normal | -0.075 |  |
| 2025-12-03 15:06:32 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:05:50 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | -0.009 |  |
| 2025-12-03 15:05:32 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:05:17 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:05:15 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | -0.067 |  |
| 2025-12-03 15:04:41 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:04:41 | Nagalagam Street (Kelani Ganga) | 1.31 | 🟡 Alert | -0.059 |  |
| 2025-12-03 15:04:04 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:03:59 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:03:56 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:03:50 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:03:44 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.129 |  |
| 2025-12-03 15:03:41 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:03:24 | Manampitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.030 |  |
| 2025-12-03 15:03:21 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.092 |  |
| 2025-12-03 15:02:46 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-03 15:02:41 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 15:02:33 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.024 |  |
| 2025-12-03 15:02:31 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:02:18 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:02:01 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:01:40 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:01:36 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:01:10 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:01:08 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | -0.151 |  |
| 2025-12-03 15:01:03 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:00:30 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:23:39 | Manampitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.030 |  |
| 2025-12-03 14:15:44 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-03 14:12:50 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:11:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 14:11:34 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 14:07:48 | Thanthirimale (Malwathu Oya) | 7.16 | 🟠 Minor Flood | -0.054 |  |
| 2025-12-03 15:04:41 | Nagalagam Street (Kelani Ganga) | 1.31 | 🟡 Alert | -0.059 |  |
| 2025-12-03 15:02:41 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 15:02:46 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-03 14:11:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 15:01:03 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:53 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:04:41 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:02:18 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:06:32 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:03:51 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:05:15 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:01:40 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:03:50 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:03:41 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:05:32 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:00:30 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-03 15:05:50 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | -0.009 |  |
| 2025-12-03 14:03:52 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:03:59 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:04:04 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:01:10 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-03 15:02:01 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:15:44 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-03 15:02:31 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:05:17 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:01:36 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:03:56 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-03 15:02:33 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.024 |  |
| 2025-12-03 15:03:24 | Manampitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.030 |  |
| 2025-12-03 15:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | -0.067 |  |
| 2025-12-03 15:07:01 | Hanwella (Kelani Ganga) | 5.06 | 🟢 Normal | -0.075 |  |
| 2025-12-03 15:03:21 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.092 |  |
| 2025-12-03 15:03:44 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.129 |  |
| 2025-12-03 15:01:08 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | -0.151 |  |

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)