# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_01:01:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,012 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 01:01:49 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:01:22 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-08 01:01:16 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:01:10 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2025-12-08 01:00:47 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-08 01:00:43 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:00:32 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:16:45 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:12:01 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:11:32 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-08 00:10:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-08 00:09:13 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:08:12 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2025-12-08 00:06:51 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:06:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:06:22 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:06:15 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:06:05 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-08 00:05:59 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2025-12-08 00:05:30 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:04:50 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:04:49 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2025-12-08 00:04:28 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-08 00:04:25 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:04:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.068 |  |
| 2025-12-08 00:04:17 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-08 00:03:50 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.130 |  |
| 2025-12-08 00:03:23 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-08 00:03:21 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 00:02:46 | Thanthirimale (Malwathu Oya) | 5.14 | 🟡 Alert | -9.818 |  |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-07 23:03:19 | Rathnapura (Kalu Ganga) | 2.94 | 🟢 Normal | 0.412 | 🔺 Rising |
| 2025-12-08 00:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2025-12-07 23:04:02 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2025-12-08 00:06:05 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-08 00:04:49 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2025-12-08 01:00:47 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-08 01:01:22 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-08 00:04:28 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-08 00:10:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-08 00:11:32 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-08 00:02:33 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-08 00:03:23 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-08 00:04:17 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 00:00:39 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 01:00:32 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:01:49 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:04:25 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:03:21 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:00:43 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:01:16 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:06:15 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2025-12-07 22:01:11 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:06:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:05:30 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:12:01 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:09:13 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-08 00:01:11 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-08 01:01:10 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2025-12-08 00:05:59 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-08 00:04:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.068 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |
| 2025-12-08 00:03:50 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.130 |  |

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)