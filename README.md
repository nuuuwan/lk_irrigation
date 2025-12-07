# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_03:15:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,096 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 03:15:15 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2025-12-08 03:12:11 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.089 |  |
| 2025-12-08 03:09:40 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 14.087 | 🔺 Rising |
| 2025-12-08 03:09:17 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 14.087 | 🔺 Rising |
| 2025-12-08 03:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2025-12-08 03:06:38 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-08 03:06:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2025-12-08 03:06:14 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.005 |  |
| 2025-12-08 03:06:02 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2025-12-08 03:05:56 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:05:20 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-08 03:05:13 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-08 03:05:01 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.111 |  |
| 2025-12-08 03:04:32 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:04:16 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-08 03:04:13 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2025-12-08 03:04:00 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:03:37 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:03:14 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-08 03:03:09 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.069 |  |
| 2025-12-08 03:03:07 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:03:04 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-08 03:02:37 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:02:37 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.070 |  |
| 2025-12-08 03:02:36 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:01:58 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.024 |  |
| 2025-12-08 03:01:18 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-08 03:01:17 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:00:47 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.031 |  |
| 2025-12-08 03:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 03:00:46 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:00:09 | Thanthirimale (Malwathu Oya) | 4.96 | 🟢 Normal | -0.042 |  |
| 2025-12-08 02:45:31 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.070 |  |
| 2025-12-08 02:45:29 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.070 |  |
| 2025-12-08 02:41:59 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-08 02:36:52 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 02:21:31 | Magura (Kalu Ganga) | 3.01 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2025-12-08 03:09:40 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 14.087 | 🔺 Rising |
| 2025-12-08 03:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-08 03:04:13 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2025-12-08 02:01:07 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2025-12-08 03:15:15 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2025-12-08 03:03:04 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-08 03:05:13 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-08 03:01:18 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-08 03:04:16 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-08 03:05:20 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-08 03:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 03:06:38 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-08 03:00:46 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:02:37 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:05:56 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:02:36 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:00:43 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:04:32 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:03:37 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:03:07 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:04:00 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:06:14 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.005 |  |
| 2025-12-08 03:03:14 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-08 03:06:02 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2025-12-08 00:01:11 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-08 03:01:58 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.024 |  |
| 2025-12-08 03:00:47 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.031 |  |
| 2025-12-08 03:00:09 | Thanthirimale (Malwathu Oya) | 4.96 | 🟢 Normal | -0.042 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |
| 2025-12-08 03:03:09 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.069 |  |
| 2025-12-08 03:02:37 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.070 |  |
| 2025-12-08 03:12:11 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.089 |  |
| 2025-12-08 03:05:01 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)