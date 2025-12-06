# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_03:34:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,259 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 03:34:40 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-07 03:26:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2025-12-07 03:23:25 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:23:04 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:20:35 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:15:19 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-07 03:13:35 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -3.857 |  |
| 2025-12-07 03:13:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -3.857 |  |
| 2025-12-07 03:11:12 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.038 |  |
| 2025-12-07 03:10:02 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:09:45 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:07:39 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:07:01 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:06:20 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-07 03:05:50 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.051 |  |
| 2025-12-07 03:05:47 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:27 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-07 03:05:23 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.031 |  |
| 2025-12-07 03:05:16 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:15 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:13 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:01 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.005 |  |
| 2025-12-07 03:04:09 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:04:00 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:03:55 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.091 |  |
| 2025-12-07 03:03:51 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2025-12-07 03:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2025-12-07 03:03:06 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:02:57 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 03:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2025-12-07 03:02:22 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:02:21 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-07 03:02:13 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2025-12-07 03:02:12 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2025-12-07 03:02:02 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:01:47 | Thanthirimale (Malwathu Oya) | 6.34 | 🟡 Alert | -0.030 |  |
| 2025-12-07 03:01:27 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:01:18 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:01:07 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:01:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 03:01:47 | Thanthirimale (Malwathu Oya) | 6.34 | 🟡 Alert | -0.030 |  |
| 2025-12-07 03:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2025-12-07 03:02:21 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-07 03:34:40 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-07 03:15:19 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-07 03:01:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 03:06:20 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-07 03:02:57 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 03:01:07 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:23:25 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:02:22 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:03:06 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:02:02 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:01:18 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:47 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:10:02 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:16 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:07:39 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:01 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.005 |  |
| 2025-12-07 03:01:27 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:07:01 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:04:09 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:04:00 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-07 03:05:27 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-07 03:26:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2025-12-07 03:03:51 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 03:02:12 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2025-12-07 03:02:13 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2025-12-07 03:05:23 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.031 |  |
| 2025-12-07 03:11:12 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.038 |  |
| 2025-12-07 03:05:50 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.051 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-07 03:03:55 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.091 |  |
| 2025-12-07 03:13:35 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -3.857 |  |

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)