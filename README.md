# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_17:22:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,795 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 17:22:39 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | -0.014 |  |
| 2025-12-01 17:07:32 | Ellagawa (Kalu Ganga) | 10.81 | 🟠 Minor Flood | -0.066 |  |
| 2025-12-01 17:06:46 | Hanwella (Kelani Ganga) | 8.70 | 🟠 Minor Flood | -0.069 |  |
| 2025-12-01 17:06:22 | Nagalagam Street (Kelani Ganga) | 2.53 | 🔴 Major Flood | -0.015 |  |
| 2025-12-01 17:06:18 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:05:41 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-01 17:05:40 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:05:07 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-01 17:04:43 | Rathnapura (Kalu Ganga) | 5.08 | 🟢 Normal | -0.072 |  |
| 2025-12-01 17:04:01 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.031 |  |
| 2025-12-01 17:03:40 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.197 |  |
| 2025-12-01 17:03:39 | Galgamuwa (Mee Oya) | 3.60 | 🟢 Normal | -0.070 |  |
| 2025-12-01 17:03:30 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.034 |  |
| 2025-12-01 17:03:28 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:03:26 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:03:20 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:02:58 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.094 |  |
| 2025-12-01 17:02:40 | Putupaula (Kalu Ganga) | 4.16 | 🟠 Minor Flood | -0.021 |  |
| 2025-12-01 17:02:38 | Thanthirimale (Malwathu Oya) | 9.32 | 🔴 Major Flood | -0.048 |  |
| 2025-12-01 17:02:34 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | -0.099 |  |
| 2025-12-01 17:02:32 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-01 17:02:32 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:02:30 | Horowpothana (Yan Oya) | 6.52 | 🟡 Alert | -0.143 |  |
| 2025-12-01 17:02:30 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | -0.090 |  |
| 2025-12-01 17:02:29 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.030 |  |
| 2025-12-01 17:02:15 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:02:09 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-01 17:01:49 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.160 |  |
| 2025-12-01 17:01:45 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-01 17:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:01:26 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2025-12-01 17:01:17 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:00:12 | Nakkala (Kumbukkan Oya) | 1.61 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 17:06:22 | Nagalagam Street (Kelani Ganga) | 2.53 | 🔴 Major Flood | -0.015 |  |
| 2025-12-01 17:02:38 | Thanthirimale (Malwathu Oya) | 9.32 | 🔴 Major Flood | -0.048 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 17:02:40 | Putupaula (Kalu Ganga) | 4.16 | 🟠 Minor Flood | -0.021 |  |
| 2025-12-01 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-01 17:07:32 | Ellagawa (Kalu Ganga) | 10.81 | 🟠 Minor Flood | -0.066 |  |
| 2025-12-01 17:06:46 | Hanwella (Kelani Ganga) | 8.70 | 🟠 Minor Flood | -0.069 |  |
| 2025-12-01 17:02:30 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | -0.090 |  |
| 2025-12-01 17:02:30 | Horowpothana (Yan Oya) | 6.52 | 🟡 Alert | -0.143 |  |
| 2025-12-01 17:01:45 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-01 17:05:07 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-01 17:01:17 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:06:18 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:02:15 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:14:06 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:02:09 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:03:28 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:02:32 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:03:20 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-01 17:05:41 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:08:20 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-01 17:02:32 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-01 17:00:12 | Nakkala (Kumbukkan Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-01 17:22:39 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | -0.014 |  |
| 2025-12-01 17:01:26 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2025-12-01 17:02:29 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.030 |  |
| 2025-12-01 17:04:01 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.031 |  |
| 2025-12-01 17:03:30 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.034 |  |
| 2025-12-01 17:03:39 | Galgamuwa (Mee Oya) | 3.60 | 🟢 Normal | -0.070 |  |
| 2025-12-01 17:04:43 | Rathnapura (Kalu Ganga) | 5.08 | 🟢 Normal | -0.072 |  |
| 2025-12-01 17:02:58 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.094 |  |
| 2025-12-01 17:02:34 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | -0.099 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-01 17:01:49 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.160 |  |
| 2025-12-01 17:03:40 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)