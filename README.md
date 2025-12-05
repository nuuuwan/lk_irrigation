# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_15:06:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,021 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 15:06:21 | Weraganthota (Mahaweli Ganga) | -1.37 | 🟢 Normal | -0.116 |  |
| 2025-12-05 15:06:11 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2025-12-05 15:06:02 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.048 |  |
| 2025-12-05 15:05:58 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-05 15:05:46 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-05 15:05:45 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:05:21 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-05 15:05:10 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.012 |  |
| 2025-12-05 15:04:57 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:04:43 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.048 |  |
| 2025-12-05 15:03:56 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.055 |  |
| 2025-12-05 15:03:24 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.051 |  |
| 2025-12-05 15:03:20 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-05 15:03:11 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.020 |  |
| 2025-12-05 15:03:10 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 15:03:10 | Ellagawa (Kalu Ganga) | 6.06 | 🟢 Normal | -0.064 |  |
| 2025-12-05 15:03:06 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.085 |  |
| 2025-12-05 15:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.100 |  |
| 2025-12-05 15:02:28 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2025-12-05 15:02:21 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.011 |  |
| 2025-12-05 15:01:57 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2025-12-05 15:01:40 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.013 |  |
| 2025-12-05 15:01:27 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:01:24 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 15:01:14 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:00:56 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:00:29 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.041 |  |
| 2025-12-05 15:00:25 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-05 15:00:18 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:17:52 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:14:36 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.013 |  |
| 2025-12-05 14:13:00 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.012 |  |
| 2025-12-05 14:12:57 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:12:55 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:10:18 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:09:26 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.055 |  |
| 2025-12-05 14:07:09 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 14:02:54 | Thanthirimale (Malwathu Oya) | 6.44 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2025-12-05 15:05:58 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-05 15:01:24 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 15:05:21 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-05 14:01:34 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-05 15:03:10 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 15:01:14 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:00:18 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:44 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:05:45 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:00:56 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:06:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:04:57 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:01:27 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 15:06:11 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2025-12-05 15:05:46 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-05 15:03:20 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-05 15:02:21 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.011 |  |
| 2025-12-05 14:03:56 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.011 |  |
| 2025-12-05 15:05:10 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.012 |  |
| 2025-12-05 15:01:40 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.013 |  |
| 2025-12-05 15:00:25 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-05 15:01:57 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2025-12-05 15:03:11 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.020 |  |
| 2025-12-05 15:02:28 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2025-12-05 15:00:29 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.041 |  |
| 2025-12-05 15:04:43 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.048 |  |
| 2025-12-05 15:06:02 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.048 |  |
| 2025-12-05 14:02:16 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.050 |  |
| 2025-12-05 15:03:24 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.051 |  |
| 2025-12-05 15:03:56 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.055 |  |
| 2025-12-05 15:03:10 | Ellagawa (Kalu Ganga) | 6.06 | 🟢 Normal | -0.064 |  |
| 2025-12-05 14:05:18 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.080 |  |
| 2025-12-05 15:03:06 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.085 |  |
| 2025-12-05 15:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.100 |  |
| 2025-12-05 15:06:21 | Weraganthota (Mahaweli Ganga) | -1.37 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)