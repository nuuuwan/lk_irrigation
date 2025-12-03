# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_12:13:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 12:13:42 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:11:14 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:10:27 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:09:28 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:07:36 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:07:24 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.020 |  |
| 2025-12-03 12:07:18 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:07:13 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:06:30 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:06:14 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:06:02 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2025-12-03 12:05:58 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:05:56 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2025-12-03 12:05:31 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:05:30 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:05:26 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:05:19 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:04:38 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2025-12-03 12:03:47 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.079 |  |
| 2025-12-03 12:03:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.050 |  |
| 2025-12-03 12:03:36 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.060 |  |
| 2025-12-03 12:03:22 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-03 12:03:20 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:03:15 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.026 |  |
| 2025-12-03 12:03:07 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:02:59 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:02:42 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:02:26 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -0.060 |  |
| 2025-12-03 12:02:07 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:01:58 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-03 12:01:57 | Thanthirimale (Malwathu Oya) | 7.26 | 🟠 Minor Flood | -0.031 |  |
| 2025-12-03 12:01:53 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2025-12-03 12:01:07 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.356 |  |
| 2025-12-03 12:00:08 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 12:01:57 | Thanthirimale (Malwathu Oya) | 7.26 | 🟠 Minor Flood | -0.031 |  |
| 2025-12-03 12:04:38 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2025-12-03 11:14:50 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-03 12:05:19 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:04:49 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:11:14 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:09:28 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:07:55 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:05:31 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:03:20 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:02:07 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:05:26 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:05:58 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:06:30 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:10:27 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:06:14 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:02:59 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:13:42 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-03 12:03:22 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-03 12:03:07 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:07:18 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:07:13 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:07:36 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:02:42 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:00:08 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-03 12:01:53 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2025-12-03 12:01:58 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-03 12:06:02 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2025-12-03 12:07:24 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.020 |  |
| 2025-12-03 12:05:56 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2025-12-03 12:03:15 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.026 |  |
| 2025-12-03 12:03:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.050 |  |
| 2025-12-03 12:03:36 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.060 |  |
| 2025-12-03 12:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -0.060 |  |
| 2025-12-03 12:03:47 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.079 |  |
| 2025-12-03 12:01:07 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.356 |  |

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)