# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_14:11:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,140 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 14:11:21 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:11:20 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:10:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.069 |  |
| 2025-12-04 14:10:16 | Thanthirimale (Malwathu Oya) | 6.01 | 🟡 Alert | -0.063 |  |
| 2025-12-04 14:09:52 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:08:55 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:08:38 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:06:56 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-04 14:06:34 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:06:23 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.070 |  |
| 2025-12-04 14:06:11 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-04 14:05:22 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2025-12-04 14:04:55 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:04:48 | Weraganthota (Mahaweli Ganga) | 1.05 | 🟢 Normal | 2.192 | 🔺 Rising |
| 2025-12-04 14:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2025-12-04 14:04:21 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:03:48 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:03:28 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:03:08 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:02:58 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 14:02:58 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | -0.050 |  |
| 2025-12-04 14:02:46 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.041 |  |
| 2025-12-04 14:02:18 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:02:15 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:01:50 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.035 |  |
| 2025-12-04 14:01:32 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-04 14:01:32 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2025-12-04 14:01:30 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:30 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:29 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:16 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:01:09 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:00:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:00:50 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:00:47 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.073 |  |
| 2025-12-04 14:00:14 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 14:10:16 | Thanthirimale (Malwathu Oya) | 6.01 | 🟡 Alert | -0.063 |  |
| 2025-12-04 14:04:48 | Weraganthota (Mahaweli Ganga) | 1.05 | 🟢 Normal | 2.192 | 🔺 Rising |
| 2025-12-04 14:06:56 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-04 14:06:11 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-04 14:02:58 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 14:01:16 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:09:52 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:06:34 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:04:55 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:00:50 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:01:50 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:03:48 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:02:15 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:11:21 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:11:20 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:03:28 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2025-12-04 14:08:55 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:03:08 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:08:38 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:02:18 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:04:21 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:30 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:29 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:09 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:30 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:00:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:01:32 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2025-12-04 14:05:22 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2025-12-04 14:01:32 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-04 14:00:14 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.021 |  |
| 2025-12-04 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.035 |  |
| 2025-12-04 14:02:46 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.041 |  |
| 2025-12-04 14:02:58 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | -0.050 |  |
| 2025-12-04 14:10:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.069 |  |
| 2025-12-04 14:06:23 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.070 |  |
| 2025-12-04 14:00:47 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)