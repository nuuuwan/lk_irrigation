# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_09:41:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 09:41:19 | Galgamuwa (Mee Oya) | 4.45 | 🟢 Normal | -0.019 |  |
| 2025-12-01 09:22:17 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | -0.082 |  |
| 2025-12-01 09:18:32 | Dunamale (Aththanagalu Oya) | 4.16 | 🟡 Alert | -0.054 |  |
| 2025-12-01 09:16:09 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:14:30 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.019 |  |
| 2025-12-01 09:11:00 | Ellagawa (Kalu Ganga) | 11.22 | 🟠 Minor Flood | -0.055 |  |
| 2025-12-01 09:09:29 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:09:24 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.056 |  |
| 2025-12-01 09:09:08 | Giriulla (Maha Oya) | 3.23 | 🟢 Normal | -0.042 |  |
| 2025-12-01 09:09:07 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:08:32 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 09:06:53 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.072 |  |
| 2025-12-01 09:06:48 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2025-12-01 09:05:17 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.101 |  |
| 2025-12-01 09:04:54 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:04:52 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:04:50 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.155 |  |
| 2025-12-01 09:04:32 | Thanthirimale (Malwathu Oya) | 10.01 | 🔴 Major Flood | -0.071 |  |
| 2025-12-01 09:04:19 | Hanwella (Kelani Ganga) | 9.42 | 🟠 Minor Flood | -0.086 |  |
| 2025-12-01 09:03:36 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 09:03:32 | Katharagama (Menik Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:03:28 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2025-12-01 09:02:55 | Yaka Wewa (Ma Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:02:55 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:02:52 | Putupaula (Kalu Ganga) | 4.26 | 🟠 Minor Flood | -0.021 |  |
| 2025-12-01 09:02:46 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:02:35 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.31 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 09:02:17 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:02:03 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.023 |  |
| 2025-12-01 09:01:20 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:01:15 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-01 09:00:42 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.022 |  |
| 2025-12-01 09:00:24 | Horowpothana (Yan Oya) | 7.14 | 🟡 Alert | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 09:03:36 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 09:04:32 | Thanthirimale (Malwathu Oya) | 10.01 | 🔴 Major Flood | -0.071 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 09:02:52 | Putupaula (Kalu Ganga) | 4.26 | 🟠 Minor Flood | -0.021 |  |
| 2025-12-01 09:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.31 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 09:11:00 | Ellagawa (Kalu Ganga) | 11.22 | 🟠 Minor Flood | -0.055 |  |
| 2025-12-01 09:04:19 | Hanwella (Kelani Ganga) | 9.42 | 🟠 Minor Flood | -0.086 |  |
| 2025-12-01 09:00:24 | Horowpothana (Yan Oya) | 7.14 | 🟡 Alert | -0.020 |  |
| 2025-12-01 09:18:32 | Dunamale (Aththanagalu Oya) | 4.16 | 🟡 Alert | -0.054 |  |
| 2025-12-01 09:09:24 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.056 |  |
| 2025-12-01 09:08:32 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 09:09:07 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:02:17 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:04:54 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:01:20 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:02:46 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:16:09 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:02:35 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 09:04:52 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:03:32 | Katharagama (Menik Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:02:55 | Yaka Wewa (Ma Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:02:55 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-01 09:01:15 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-01 09:06:48 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2025-12-01 09:41:19 | Galgamuwa (Mee Oya) | 4.45 | 🟢 Normal | -0.019 |  |
| 2025-12-01 09:14:30 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.019 |  |
| 2025-12-01 09:03:28 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 09:00:42 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.022 |  |
| 2025-12-01 09:02:03 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.023 |  |
| 2025-12-01 09:09:08 | Giriulla (Maha Oya) | 3.23 | 🟢 Normal | -0.042 |  |
| 2025-12-01 09:06:53 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.072 |  |
| 2025-12-01 09:22:17 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | -0.082 |  |
| 2025-12-01 09:05:17 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.101 |  |
| 2025-12-01 09:04:50 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.155 |  |

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)