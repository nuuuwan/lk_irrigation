# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_18:13:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,829 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 18:13:11 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:11:02 | Ellagawa (Kalu Ganga) | 10.80 | 🟠 Minor Flood | -0.009 |  |
| 2025-12-01 18:10:25 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:07:55 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2025-12-01 18:06:57 | Hanwella (Kelani Ganga) | 8.61 | 🟠 Minor Flood | -0.090 |  |
| 2025-12-01 18:06:19 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-01 18:06:04 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.029 |  |
| 2025-12-01 18:05:15 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | -0.096 |  |
| 2025-12-01 18:04:48 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:44 | Nagalagam Street (Kelani Ganga) | 2.50 | 🔴 Major Flood | -0.031 |  |
| 2025-12-01 18:04:44 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:42 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-01 18:04:22 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:04:12 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:06 | Badalgama (Maha Oya) | 3.95 | 🟢 Normal | -0.014 |  |
| 2025-12-01 18:04:05 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:00 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-01 18:03:50 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:03:25 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:02:35 | Glencourse (Kelani Ganga) | 12.22 | 🟢 Normal | -0.090 |  |
| 2025-12-01 18:02:29 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-01 18:02:13 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:02:07 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2025-12-01 18:01:53 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.022 |  |
| 2025-12-01 18:01:51 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | -0.070 |  |
| 2025-12-01 18:01:43 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:01:42 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.031 |  |
| 2025-12-01 18:01:40 | Thanthirimale (Malwathu Oya) | 9.28 | 🔴 Major Flood | -0.041 |  |
| 2025-12-01 18:01:08 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-01 18:00:47 | Putupaula (Kalu Ganga) | 4.15 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 18:00:38 | Horowpothana (Yan Oya) | 6.51 | 🟡 Alert | -0.010 |  |
| 2025-12-01 18:00:11 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-01 17:22:39 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 18:04:44 | Nagalagam Street (Kelani Ganga) | 2.50 | 🔴 Major Flood | -0.031 |  |
| 2025-12-01 18:01:40 | Thanthirimale (Malwathu Oya) | 9.28 | 🔴 Major Flood | -0.041 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 18:11:02 | Ellagawa (Kalu Ganga) | 10.80 | 🟠 Minor Flood | -0.009 |  |
| 2025-12-01 18:00:47 | Putupaula (Kalu Ganga) | 4.15 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-01 18:06:57 | Hanwella (Kelani Ganga) | 8.61 | 🟠 Minor Flood | -0.090 |  |
| 2025-12-01 18:00:38 | Horowpothana (Yan Oya) | 6.51 | 🟡 Alert | -0.010 |  |
| 2025-12-01 18:05:15 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | -0.096 |  |
| 2025-12-01 18:06:19 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-01 18:04:42 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-01 18:04:00 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-01 17:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:10:25 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:05 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:48 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:12 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:02:29 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:44 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:07:55 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2025-12-01 18:13:11 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:01:08 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:03:25 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:02:13 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:00:11 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:04:22 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:01:43 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-01 18:04:06 | Badalgama (Maha Oya) | 3.95 | 🟢 Normal | -0.014 |  |
| 2025-12-01 18:02:07 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-01 18:01:53 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.022 |  |
| 2025-12-01 18:06:04 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.029 |  |
| 2025-12-01 18:01:42 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.031 |  |
| 2025-12-01 18:01:51 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | -0.070 |  |
| 2025-12-01 18:02:35 | Glencourse (Kelani Ganga) | 12.22 | 🟢 Normal | -0.090 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)