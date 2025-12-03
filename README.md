# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_11:05:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 11:05:47 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:05:37 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:05:05 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:04:52 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:04:49 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:04:44 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-03 11:04:43 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-03 11:04:35 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:04:13 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.012 |  |
| 2025-12-03 11:03:41 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2025-12-03 11:03:33 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 11:03:20 | Hanwella (Kelani Ganga) | 5.36 | 🟢 Normal | -0.080 |  |
| 2025-12-03 11:03:08 | Thanthirimale (Malwathu Oya) | 7.29 | 🟠 Minor Flood | -0.058 |  |
| 2025-12-03 11:03:02 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2025-12-03 11:02:56 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.59 | 🟢 Normal | -0.070 |  |
| 2025-12-03 11:02:13 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:02:07 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | -0.050 |  |
| 2025-12-03 11:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:01:52 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:01:16 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:01:13 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.012 |  |
| 2025-12-03 11:01:10 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:00:12 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:59:03 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-03 10:14:30 | Manampitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-03 10:12:39 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.012 |  |
| 2025-12-03 10:12:25 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.012 |  |
| 2025-12-03 10:12:21 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.008 |  |
| 2025-12-03 10:10:50 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2025-12-03 10:08:39 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.036 |  |
| 2025-12-03 10:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:07:57 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-03 10:07:09 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.012 |  |
| 2025-12-03 10:07:06 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.023 |  |
| 2025-12-03 10:07:04 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 11:03:08 | Thanthirimale (Malwathu Oya) | 7.29 | 🟠 Minor Flood | -0.058 |  |
| 2025-12-03 11:03:02 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2025-12-03 10:07:57 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-03 11:04:43 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-03 11:04:44 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-03 11:03:33 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 11:02:56 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:01:10 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:04:49 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:51 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:01:16 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:00:12 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:03:13 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:47 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 11:05:47 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:29 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:12:21 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.008 |  |
| 2025-12-03 10:10:50 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2025-12-03 11:04:35 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:04:52 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:05:37 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:02:13 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:03:17 | Glencourse (Kelani Ganga) | 11.01 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:01:52 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-03 11:05:05 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:59:03 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-03 11:04:13 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.012 |  |
| 2025-12-03 11:01:13 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.012 |  |
| 2025-12-03 10:07:06 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.023 |  |
| 2025-12-03 11:03:41 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2025-12-03 10:08:39 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.036 |  |
| 2025-12-03 11:02:07 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | -0.050 |  |
| 2025-12-03 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.59 | 🟢 Normal | -0.070 |  |
| 2025-12-03 11:03:20 | Hanwella (Kelani Ganga) | 5.36 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)