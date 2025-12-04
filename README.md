# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_00:12:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,492 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 00:12:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:10:54 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-05 00:10:18 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:10:10 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:06:26 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-05 00:06:09 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 00:05:54 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-05 00:05:54 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:04:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:04:58 | Urawa (Nilwala Ganga) | 2.81 | 🟡 Alert | -0.092 |  |
| 2025-12-05 00:04:42 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:04:21 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-05 00:04:11 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.049 |  |
| 2025-12-05 00:04:11 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-05 00:03:43 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-05 00:03:39 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-05 00:03:17 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.011 |  |
| 2025-12-05 00:03:14 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-05 00:02:43 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:02:23 | Thanthirimale (Malwathu Oya) | 5.64 | 🟡 Alert | -0.032 |  |
| 2025-12-05 00:02:15 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 00:02:12 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:44 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2025-12-05 00:01:42 | Pitabeddara (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-05 00:01:28 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:21 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2025-12-05 00:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:00:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-04 23:58:54 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-04 23:48:31 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-04 23:17:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2025-12-04 23:16:43 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-04 23:16:41 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 00:02:23 | Thanthirimale (Malwathu Oya) | 5.64 | 🟡 Alert | -0.032 |  |
| 2025-12-05 00:04:58 | Urawa (Nilwala Ganga) | 2.81 | 🟡 Alert | -0.092 |  |
| 2025-12-05 00:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2025-12-05 00:05:54 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-05 00:04:11 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-04 22:05:21 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-05 00:03:14 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-05 00:06:26 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-05 00:01:42 | Pitabeddara (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-05 00:03:39 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-05 00:10:54 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-05 00:04:21 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-05 00:00:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-05 00:02:15 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 00:06:09 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 00:01:28 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:21 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:02:43 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:05:54 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:04:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:04:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:02:12 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:04:42 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:12:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:10:18 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:10:10 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:03:43 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-05 00:01:44 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2025-12-05 00:03:17 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.011 |  |
| 2025-12-04 23:58:54 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-05 00:04:11 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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