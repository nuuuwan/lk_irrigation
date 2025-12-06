# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_04:13:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,284 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 04:13:21 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.009 |  |
| 2025-12-07 04:07:20 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-07 04:06:54 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2025-12-07 04:06:40 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:05:19 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-07 04:05:00 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:04:41 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:04:39 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:04:30 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:04:01 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-07 04:03:46 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:03:34 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:03:04 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:02:45 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2025-12-07 04:02:22 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2025-12-07 04:02:20 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2025-12-07 04:02:19 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:02:13 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:01:45 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:01:44 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-07 04:01:34 | Thanthirimale (Malwathu Oya) | 6.30 | 🟡 Alert | -0.040 |  |
| 2025-12-07 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.016 |  |
| 2025-12-07 04:00:53 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:00:38 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:00:23 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:34:40 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-07 03:26:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2025-12-07 03:23:25 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2025-12-07 03:23:04 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2025-12-07 03:20:35 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 04:01:34 | Thanthirimale (Malwathu Oya) | 6.30 | 🟡 Alert | -0.040 |  |
| 2025-12-07 03:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2025-12-07 04:07:20 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-07 03:34:40 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-07 04:01:44 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-07 04:05:19 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-07 04:00:23 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:02:13 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:04:39 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:03:46 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:04:30 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:02:19 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:01:45 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:47 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:16 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:05:00 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:06:40 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:01 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.005 |  |
| 2025-12-07 04:13:21 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.009 |  |
| 2025-12-07 04:04:41 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:03:04 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:00:38 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:00:53 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:04:00 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-07 04:04:01 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-07 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.016 |  |
| 2025-12-07 03:26:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2025-12-07 04:06:54 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 04:02:45 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2025-12-07 04:02:20 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2025-12-07 04:02:22 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2025-12-07 03:11:12 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.038 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-07 03:03:55 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)