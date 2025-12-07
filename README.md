# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_23:02:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2025-12-07 22:27:24 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-07 22:16:45 | Thanthirimale (Malwathu Oya) | 5.26 | 🟡 Alert | -0.048 |  |
| 2025-12-07 22:12:36 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.035 |  |
| 2025-12-07 22:09:47 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-07 22:09:41 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:09:15 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.028 |  |
| 2025-12-07 22:09:14 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-07 22:06:47 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-07 22:06:20 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:06:01 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-07 22:05:28 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-07 22:05:09 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.051 |  |
| 2025-12-07 22:05:07 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2025-12-07 22:04:35 | Dunamale (Aththanagalu Oya) | 2.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 22:04:09 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 22:16:45 | Thanthirimale (Malwathu Oya) | 5.26 | 🟡 Alert | -0.048 |  |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-07 22:05:07 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2025-12-07 21:04:49 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2025-12-07 23:02:58 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-07 22:06:47 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-07 22:06:01 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-07 22:09:47 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-07 23:02:33 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 23:02:56 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-07 23:01:40 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 22:27:24 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-07 23:00:50 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 22:00:25 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:01:08 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:02:12 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:00:34 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:06:20 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:01:11 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 23:02:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:09:41 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:01:56 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-07 23:01:59 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-07 22:05:28 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-07 22:02:26 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 23:01:51 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.021 |  |
| 2025-12-07 22:01:16 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2025-12-07 22:09:15 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.028 |  |
| 2025-12-07 22:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.035 |  |
| 2025-12-07 22:03:12 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2025-12-07 22:05:09 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.051 |  |
| 2025-12-07 22:02:55 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.052 |  |
| 2025-12-07 23:02:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.059 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)