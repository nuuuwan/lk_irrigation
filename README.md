# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_08:34:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 08:34:19 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.034 |  |
| 2025-12-04 08:18:05 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.008 |  |
| 2025-12-04 08:12:42 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.054 |  |
| 2025-12-04 08:11:07 | Thanthirimale (Malwathu Oya) | 6.28 | 🟡 Alert | -0.056 |  |
| 2025-12-04 08:10:24 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 08:08:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2025-12-04 08:07:27 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.021 |  |
| 2025-12-04 08:06:18 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | -0.079 |  |
| 2025-12-04 08:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.130 |  |
| 2025-12-04 08:05:55 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:05:54 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 08:05:30 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:04:44 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2025-12-04 08:04:34 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:04:29 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:04:20 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:04:11 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.039 |  |
| 2025-12-04 08:04:06 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:03:36 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:03:28 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:03:27 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.065 |  |
| 2025-12-04 08:03:17 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2025-12-04 08:03:03 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.012 |  |
| 2025-12-04 08:02:50 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.012 |  |
| 2025-12-04 08:02:46 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.041 |  |
| 2025-12-04 08:02:23 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:02:17 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:02:12 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:01:38 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:35 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:18 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:00:31 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:59:47 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 08:11:07 | Thanthirimale (Malwathu Oya) | 6.28 | 🟡 Alert | -0.056 |  |
| 2025-12-04 08:05:54 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 08:10:24 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 08:04:20 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:02:17 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:02:23 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:03:28 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:00:31 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:04:06 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:05:30 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:03:36 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:02:12 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:05:55 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:04:34 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:03:17 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:04:29 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:59:47 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:18:05 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.008 |  |
| 2025-12-04 08:01:35 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:38 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:18 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:03:03 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.012 |  |
| 2025-12-04 08:02:50 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.012 |  |
| 2025-12-04 08:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2025-12-04 08:04:44 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2025-12-04 08:07:27 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.021 |  |
| 2025-12-04 08:08:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2025-12-04 08:34:19 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.034 |  |
| 2025-12-04 08:04:11 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.039 |  |
| 2025-12-04 08:02:46 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.041 |  |
| 2025-12-04 08:12:42 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.054 |  |
| 2025-12-04 08:03:27 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.065 |  |
| 2025-12-04 08:06:18 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | -0.079 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-04 08:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)