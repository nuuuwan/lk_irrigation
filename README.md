# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_01:03:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,664 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 01:03:24 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:03:22 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:02:45 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-04 01:02:44 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.010 |  |
| 2025-12-04 01:02:21 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-04 01:01:59 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:01:47 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:01:39 | Yaka Wewa (Ma Oya) | 1.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-04 01:01:18 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:01:01 | Thanthirimale (Malwathu Oya) | 6.65 | 🟡 Alert | -0.030 |  |
| 2025-12-04 00:16:44 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:16:20 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.008 |  |
| 2025-12-04 00:15:46 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.034 |  |
| 2025-12-04 00:14:50 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.059 |  |
| 2025-12-04 00:11:55 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:09:59 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:09:50 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:09:18 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:08:17 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.029 |  |
| 2025-12-04 00:07:36 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:06:26 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:06:18 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:06:13 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:06:09 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2025-12-04 00:06:06 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.005 |  |
| 2025-12-04 00:06:00 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.077 |  |
| 2025-12-04 00:05:53 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2025-12-04 00:05:38 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-04 00:05:16 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:05:15 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:04:58 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.040 |  |
| 2025-12-04 00:04:51 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:04:44 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.125 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 01:01:01 | Thanthirimale (Malwathu Oya) | 6.65 | 🟡 Alert | -0.030 |  |
| 2025-12-04 00:04:44 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-04 00:05:38 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-04 01:01:39 | Yaka Wewa (Ma Oya) | 1.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-04 00:00:36 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 01:01:59 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:01:18 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:09:50 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:09:59 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:03:24 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:03:30 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:06:18 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:03:22 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:07:36 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-04 01:01:47 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-04 00:06:06 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.005 |  |
| 2025-12-03 20:18:19 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.008 |  |
| 2025-12-04 00:16:20 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.008 |  |
| 2025-12-04 00:05:15 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:05:16 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:06:13 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:02:54 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-04 00:03:04 | Giriulla (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2025-12-04 01:02:44 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.010 |  |
| 2025-12-04 01:02:21 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-04 00:06:09 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2025-12-04 01:02:45 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-04 00:08:17 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.029 |  |
| 2025-12-04 00:15:46 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.034 |  |
| 2025-12-04 00:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.040 |  |
| 2025-12-04 00:14:50 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.059 |  |
| 2025-12-04 00:06:00 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.077 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-03 18:03:18 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)