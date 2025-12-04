# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_03:15:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,589 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 03:15:02 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -60.000 |  |
| 2025-12-05 03:14:59 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -60.000 |  |
| 2025-12-05 03:14:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 6.353 | 🔺 Rising |
| 2025-12-05 03:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 6.353 | 🔺 Rising |
| 2025-12-05 03:12:59 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:12:58 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:12:31 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-05 03:12:10 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-05 03:09:15 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 684.000 | 🔺 Rising |
| 2025-12-05 03:09:14 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 684.000 | 🔺 Rising |
| 2025-12-05 03:07:42 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:06:59 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-05 03:06:19 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-05 03:06:08 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:06:06 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-05 03:05:25 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-05 03:05:14 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.090 |  |
| 2025-12-05 03:05:08 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.075 |  |
| 2025-12-05 03:05:03 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:04:57 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:04:39 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:04:38 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:04:37 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:04:18 | Urawa (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.111 |  |
| 2025-12-05 03:04:06 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.069 |  |
| 2025-12-05 03:04:02 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-05 03:03:52 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2025-12-05 03:02:37 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-05 03:02:27 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-05 03:02:14 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-05 03:02:02 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:01:43 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:01:36 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.030 |  |
| 2025-12-05 03:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:00:30 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:00:12 | Thanthirimale (Malwathu Oya) | 5.55 | 🟡 Alert | -0.290 |  |
| 2025-12-05 03:00:11 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 02:54:00 | Thanthirimale (Malwathu Oya) | 5.58 | 🟡 Alert | -0.290 |  |
| 2025-12-05 02:21:34 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 03:00:12 | Thanthirimale (Malwathu Oya) | 5.55 | 🟡 Alert | -0.290 |  |
| 2025-12-05 03:09:15 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 684.000 | 🔺 Rising |
| 2025-12-05 03:14:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 6.353 | 🔺 Rising |
| 2025-12-05 03:06:06 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-05 03:02:37 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-05 03:04:02 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-05 03:05:25 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-05 03:12:31 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-05 03:12:10 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-05 03:06:59 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-05 03:00:30 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:02:02 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:01:43 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:00:11 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:12:59 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 02:03:24 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:07:42 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:04:57 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:06:08 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:04:39 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:05:03 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 03:06:19 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-05 03:02:27 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-05 03:02:14 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-05 03:03:52 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-05 03:01:36 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.030 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-05 03:04:06 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.069 |  |
| 2025-12-05 03:05:08 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.075 |  |
| 2025-12-05 03:05:14 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.090 |  |
| 2025-12-05 03:04:18 | Urawa (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.111 |  |
| 2025-12-05 03:15:02 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -60.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)