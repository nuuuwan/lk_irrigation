# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_10:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,558 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 10:20:37 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.018 |  |
| 2025-12-01 10:17:42 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:12:51 | Ellagawa (Kalu Ganga) | 11.18 | 🟠 Minor Flood | -0.039 |  |
| 2025-12-01 10:10:10 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:08:45 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:06:54 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2025-12-01 10:06:37 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2025-12-01 10:05:58 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.157 |  |
| 2025-12-01 10:05:22 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:05:01 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | -0.076 |  |
| 2025-12-01 10:04:17 | Putupaula (Kalu Ganga) | 4.24 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 10:04:04 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-01 10:03:47 | Hanwella (Kelani Ganga) | 9.31 | 🟠 Minor Flood | -0.111 |  |
| 2025-12-01 10:03:41 | Galgamuwa (Mee Oya) | 4.34 | 🟢 Normal | -0.295 |  |
| 2025-12-01 10:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.27 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 10:03:12 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 10:03:11 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.081 |  |
| 2025-12-01 10:03:10 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.255 |  |
| 2025-12-01 10:03:09 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:02:54 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 10:02:39 | Katharagama (Menik Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:02:29 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:02:21 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.029 |  |
| 2025-12-01 10:01:48 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:01:47 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:01:42 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:01:32 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.031 |  |
| 2025-12-01 10:01:26 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:00:52 | Horowpothana (Yan Oya) | 7.10 | 🟡 Alert | -0.040 |  |
| 2025-12-01 10:00:30 | Thanthirimale (Malwathu Oya) | 9.92 | 🔴 Major Flood | -0.096 |  |
| 2025-12-01 09:41:19 | Galgamuwa (Mee Oya) | 4.45 | 🟢 Normal | -0.295 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 10:03:12 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 10:00:30 | Thanthirimale (Malwathu Oya) | 9.92 | 🔴 Major Flood | -0.096 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 10:04:17 | Putupaula (Kalu Ganga) | 4.24 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 10:12:51 | Ellagawa (Kalu Ganga) | 11.18 | 🟠 Minor Flood | -0.039 |  |
| 2025-12-01 10:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.27 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 10:03:47 | Hanwella (Kelani Ganga) | 9.31 | 🟠 Minor Flood | -0.111 |  |
| 2025-12-01 10:00:52 | Horowpothana (Yan Oya) | 7.10 | 🟡 Alert | -0.040 |  |
| 2025-12-01 10:05:01 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | -0.076 |  |
| 2025-12-01 10:03:11 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.081 |  |
| 2025-12-01 10:04:04 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-01 10:02:54 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 10:01:42 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:10:10 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:03:09 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:02:29 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:02:39 | Katharagama (Menik Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:17:42 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:01:48 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 10:05:22 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:08:45 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:01:26 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:01:47 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-01 10:20:37 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.018 |  |
| 2025-12-01 09:06:48 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2025-12-01 10:06:37 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 10:02:21 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.029 |  |
| 2025-12-01 10:01:32 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.031 |  |
| 2025-12-01 09:09:08 | Giriulla (Maha Oya) | 3.23 | 🟢 Normal | -0.042 |  |
| 2025-12-01 10:06:54 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2025-12-01 09:22:17 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | -0.082 |  |
| 2025-12-01 10:05:58 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.157 |  |
| 2025-12-01 10:03:10 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.255 |  |
| 2025-12-01 10:03:41 | Galgamuwa (Mee Oya) | 4.34 | 🟢 Normal | -0.295 |  |

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)