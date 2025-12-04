# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_01:16:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,522 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 01:16:23 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-05 01:11:03 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 01:08:55 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:08:45 | Panadugama (Nilwala Ganga) | 4.08 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 01:07:37 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:06:21 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2025-12-05 01:05:35 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:04:53 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2025-12-05 01:04:37 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-05 01:04:30 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-05 01:04:08 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-05 01:03:44 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.050 |  |
| 2025-12-05 01:02:58 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:02:48 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:02:31 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 01:02:23 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:02:07 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-05 01:02:01 | Thanthirimale (Malwathu Oya) | 5.61 | 🟡 Alert | -0.030 |  |
| 2025-12-05 01:02:01 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-05 01:01:41 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-05 01:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-05 01:01:35 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 01:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-05 01:01:19 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 01:01:01 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 01:00:51 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | -0.118 |  |
| 2025-12-05 01:00:46 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:23:31 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-05 00:23:29 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-05 00:18:22 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.126 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 01:02:01 | Thanthirimale (Malwathu Oya) | 5.61 | 🟡 Alert | -0.030 |  |
| 2025-12-05 01:00:51 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | -0.118 |  |
| 2025-12-05 01:06:21 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2025-12-05 01:04:08 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-05 01:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-05 01:02:01 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-05 00:03:14 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-05 00:10:54 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-05 01:08:45 | Panadugama (Nilwala Ganga) | 4.08 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 01:04:30 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-05 01:16:23 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-05 01:02:07 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-05 01:01:19 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 01:01:35 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 01:01:01 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 01:02:31 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 01:11:03 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 01:00:46 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:08:55 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:02:48 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:02:23 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:05:35 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:07:37 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:12:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:10:18 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:02:58 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 01:04:37 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-05 01:04:53 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2025-12-05 01:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-05 01:01:41 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-04 23:58:54 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-05 01:03:44 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)