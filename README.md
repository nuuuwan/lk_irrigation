# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_21:11:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 21:11:26 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:08:30 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-04 21:07:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:07:03 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2025-12-04 21:07:01 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-04 21:06:39 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.019 |  |
| 2025-12-04 21:06:23 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:06:21 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:06:00 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:05:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:05:13 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.012 |  |
| 2025-12-04 21:05:10 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2025-12-04 21:05:07 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-04 21:04:41 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:04:19 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2025-12-04 21:04:15 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-04 21:04:13 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2025-12-04 21:04:10 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-04 21:03:26 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.793 | 🔺 Rising |
| 2025-12-04 21:03:18 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 21:03:04 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.175 |  |
| 2025-12-04 21:02:47 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:02:35 | Urawa (Nilwala Ganga) | 2.87 | 🟡 Alert | 0.132 | 🔺 Rising |
| 2025-12-04 21:02:31 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:02:03 | Thanthirimale (Malwathu Oya) | 5.75 | 🟡 Alert | -0.032 |  |
| 2025-12-04 21:01:35 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-04 21:01:17 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-04 21:01:06 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:00:25 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:00:12 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 21:02:35 | Urawa (Nilwala Ganga) | 2.87 | 🟡 Alert | 0.132 | 🔺 Rising |
| 2025-12-04 21:02:03 | Thanthirimale (Malwathu Oya) | 5.75 | 🟡 Alert | -0.032 |  |
| 2025-12-04 21:03:26 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.793 | 🔺 Rising |
| 2025-12-04 21:04:13 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2025-12-04 21:07:03 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2025-12-04 21:08:30 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-04 21:07:01 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-04 21:01:35 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-04 21:05:07 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-04 21:01:17 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-04 21:04:10 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-04 21:04:15 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-04 21:00:25 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:25:57 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:19:13 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:05:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:01:06 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:02:47 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:04:19 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:06:00 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:11:26 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:07:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:02:31 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:04:41 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:06:23 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:03:18 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 21:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2025-12-04 21:00:12 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2025-12-04 21:05:13 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.012 |  |
| 2025-12-04 21:05:10 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2025-12-04 21:06:39 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.019 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-04 21:03:04 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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