# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_23:35:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,973 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 23:35:50 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:32:03 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:25:48 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-07 23:20:21 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.054 |  |
| 2025-12-07 23:18:09 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:16:43 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.008 |  |
| 2025-12-07 23:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2025-12-07 23:08:22 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:07:35 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2025-12-07 23:07:16 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.028 |  |
| 2025-12-07 23:06:48 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 2160.000 | 🔺 Rising |
| 2025-12-07 23:06:47 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 2160.000 | 🔺 Rising |
| 2025-12-07 23:04:20 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-07 23:04:02 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2025-12-07 23:03:57 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-07 23:03:42 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.089 |  |
| 2025-12-07 23:03:41 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:03:30 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:03:28 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:03:27 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.041 |  |
| 2025-12-07 23:03:19 | Rathnapura (Kalu Ganga) | 2.94 | 🟢 Normal | 0.412 | 🔺 Rising |
| 2025-12-07 23:02:58 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-07 23:02:56 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-07 23:02:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:02:33 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 23:02:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.059 |  |
| 2025-12-07 23:02:12 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:01:59 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-07 23:01:51 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.021 |  |
| 2025-12-07 23:01:40 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-07 23:01:08 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:00:50 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 23:00:34 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:56:17 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 22:16:45 | Thanthirimale (Malwathu Oya) | 5.26 | 🟡 Alert | -0.048 |  |
| 2025-12-07 23:06:48 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 2160.000 | 🔺 Rising |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-07 23:03:19 | Rathnapura (Kalu Ganga) | 2.94 | 🟢 Normal | 0.412 | 🔺 Rising |
| 2025-12-07 23:04:02 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2025-12-07 23:07:35 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2025-12-07 23:02:58 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-07 23:03:57 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-07 23:04:20 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-07 23:25:48 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-07 23:02:33 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 23:02:56 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-07 23:01:40 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 23:00:50 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 23:35:50 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:01:08 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:32:03 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:02:12 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:03:28 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:00:34 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:08:22 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:01:11 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:18:09 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:03:30 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:03:41 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:16:43 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.008 |  |
| 2025-12-07 23:01:59 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-07 23:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2025-12-07 23:01:51 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.021 |  |
| 2025-12-07 23:07:16 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.028 |  |
| 2025-12-07 23:03:27 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.041 |  |
| 2025-12-07 23:20:21 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.054 |  |
| 2025-12-07 23:02:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.059 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |
| 2025-12-07 23:03:42 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)